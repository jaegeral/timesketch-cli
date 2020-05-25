#!/usr/bin/env python3

from timesketch_api_client.client import TimesketchApi
import configparser
import logging
import argparse
import datetime
from prettytable import PrettyTable
import sys
# Hack to disable warning...
import urllib3
from pytaxonomies import Taxonomies


urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)


logger = logging.getLogger('timesketch')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s() - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


config = configparser.ConfigParser()
#config.read("config_demo.config")
config.read("config_local.config")

TIMESKETCH_BASEURL = config.get('TIMESKETCH', 'BASEURL')
TIMESKETCH_USERNAME = config.get('TIMESKETCH', 'USERNAME')
TIMESKETCH_PASSWORD = config.get('TIMESKETCH', 'PASSWORD')
TIMESKETCH_HTTPS_VERIFY = config.getboolean('TIMESKETCH', 'HTTPS_VERIFY')
TIMESKETCH_TOOLS_VERSION = config.get('TIMESKETCH', 'version')


def login():
    """

    :return: api_client object with a valid session
    """
    try:
        c_api_client = TimesketchApi(TIMESKETCH_BASEURL, username=TIMESKETCH_USERNAME, password=TIMESKETCH_PASSWORD)

        return c_api_client
    except:
        logger.error("Error while login %s",str(sys.exc_info()[0]))
        print("Error while login"+str(sys.exc_info()[0]))
        sys.exit()

def list_sketches(a_api_client=None):
    """
    Lists all sketches in a Timesketch instance
    :param a_api_client: login needed before
    """
    if a_api_client is None:
        a_api_client = login()

    sketches = a_api_client.list_sketches()
    t = PrettyTable(['id', 'Name'])
    for current_sketch in sketches:
        t.add_row([current_sketch.id, current_sketch.name])
    print(t)

def list_timelines_in_sketch(a_api_client=None,sketch_id=None):
    if a_api_client is None:
        a_api_client = login()

    sketch = a_api_client.get_sketch(int(sketch_id))
    timelines = sketch.list_timelines()

    t = PrettyTable(['id', 'Name'])
    for current_timeline in timelines:
        t.add_row([current_timeline.id, current_timeline.name])
    print(t)

def get_sketch(a_api_client=None, a_sketch_id=None):
    """

    :param a_api_client: valid session needed
    :param a_sketch_id: sketch id that is requested
    :return: returns a sketch object
    """

    if a_api_client is None:
        a_api_client = login()

    c_sketch = a_api_client.get_sketch(int(a_sketch_id))
    return c_sketch


def search_in_sketch(a_api_client=None, a_sketch=None, a_search_term=None):
    """

    :param a_api_client:
    :param a_sketch: not a sketch ID
    :param a_search_term:
    """
    if isinstance(a_sketch, int):
        # it is most likely the sketch id, not the sketch instance
        a_sketch = a_api_client.get_sketch(a_sketch)

        #explore_sketch()
    explore_sketch(api_client=a_api_client,a_sketchid=a_sketch.id,a_searchterm=a_search_term)

    #a_sketch.search(a_search_term)
    #a_sketch.explore()
    #logger.error("Not yet implemented")


def console():
    logger.error("Not implemented yet")
    raise NotImplementedError


def add_comment_to_event(c_api_client, a_sketch_id, a_event_id, a_index_id, a_comment_text):
    """
    Adds a comment to a single event
    :param c_api_client:
    :param a_sketch_id:
    :param a_event_id:
    :param a_index_id:
    :param a_comment_text:
    """
    current_sketch = c_api_client.get_sketch(a_sketch_id)
    current_sketch.comment_event(event_id=a_event_id, index=a_index_id, comment_text=a_comment_text)


def add_label_to_event(c_api_client,a_sketch_id,a_event_id,a_index_id,a_label_text):
    """
    Add a label to a single event

    :param c_api_client:
    :param a_sketch_id:
    :param a_event_id:
    :param a_index_id:
    :param a_label_text:
    """

    if (a_label_text is None) or (len(a_label_text) == 0):
        explore_pytaxonomies()
        a_label_text = input("Give label")


    current_sketch = c_api_client.get_sketch(a_sketch_id)
    current_sketch.label_event(event_id=a_event_id, index=a_index_id, label_text=a_label_text)

def explore_pytaxonomies():
    """
    the tool should go in an endless loop asking for user input with auto complete until the right taxonomy is choosen
    example:
    PAP<enter>
    PAP:AMBER
     PAP:WHITE
     PAP:GREEN
     PAP:RED
     PAP:RED<enter> --> finished
    https://github.com/MISP/PyTaxonomies
    """
    from pytaxonomies import Taxonomies

    taxonomies = Taxonomies()
    again_user_input = input("do you want to search within the pyTaxonomies? (y/n) ")
    if again_user_input.lower() == 'y':
        again = True
    else:
        again = False

    while again:
        try:
            char = input("Term you want to search for e.g. PAP, TLP, ...")  # read 1 character from stdin
            # try autocomplete
            print("Suggestions")
            if (char is "") or (len(char) == 0):
                search_results = taxonomies.keys()
            else:
                #search_results = taxonomies.get(char).machinetags_expanded()
                all = taxonomies.all_machinetags()

                resultarray = []

                for iterm in all:
                    for item2 in iterm:
                        if char in item2.lower():  # lower to be able to find PAP if you look for p
                            resultarray.append(item2)

                for resultitem in resultarray:
                    print(resultitem)


            # print(search_results)
            again_user_input = input("again?")
            if again_user_input.lower() == 'n':
                again = False
            else:
                again = True
        except AttributeError as e:
            print("Seems we did not find the value "+str(e))


def explore_sketch(api_client, a_sketchid,a_searchterm):
    """
    Searches for a given string in a fiven sketch and prints the output as a table
    :param api_client:
    :param a_sketchid:
    :param a_searchterm:
    """
    current_sketch = api_client.get_sketch(int(a_sketchid))
    print("Searching for: '"+a_searchterm+"' in sketch '"+current_sketch.name+"'")

    search_results = current_sketch.explore(a_searchterm)

    if api_client is None:
        api_client = login()

    t = PrettyTable(['datetime', 'message','labels','_id', "_index"])
    for current_sketch in search_results['objects']:
        source = current_sketch.get('_source')
        t.add_row([source.get('datetime'), source.get('message'), ('[%s]' % ', '.join(map(str, source.get('label')))),current_sketch.get("_id"), current_sketch.get("_index")])
    print(t)


def get_date(a_date):
    """
    Little helper method to check for valid date format
    :param a_date:
    :return: false if format was wrong

    """

    logger.debug("To check date:" + a_date)
    date_patterns = ["%Y-%m-%dT%H:%M:%S+00:00", "%Y-%m-%dT%H:%M:%S"]

    for pattern in date_patterns:
        try:
            return_value = datetime.datetime.strptime(a_date, pattern).date()
            logger.debug(a_date)
            return a_date
        except:
            pass

    logger.error("Given timestamp %s does not match the Timesketch formats", a_date)
    print("Sorry - Date %s is not in expected format - Try again" % (a_date))
    return False


def logo():
        """
        Prints the logo of timesketch as ascii art and the current version
        """
        print("""     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _ \
         
        /_/ /_/_/_/_/\__/___/_/\_\\__/\__/\__/_//_/-tools v{}

            """.format(TIMESKETCH_TOOLS_VERSION))


def again(user_input):
    # input returns the empty string for "enter"
    yes = {'yes', 'y', 'ye', ''}
    no = {'no', 'n'}

    choice = user_input.lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print("Please respond with 'yes' or 'no'")


def interact_add_events(a_api_client, a_sketch_id):
    """

    :param a_api_client:
    :param a_sketch_id:
    """

    if a_sketch_id is None:
        a_sketch_id = int(input("Please provide the sketch id you want to add events to as (an integer): "))

    current_sketch = a_api_client.get_sketch(a_sketch_id)

    do_again = True

    while do_again is True:
        print("Please provide informations to the event you would like to add timestamp, timestamp_desc, message will be promted\n")

        # TODO add a quit option when pressing q

        # this is an loop as long as the timestamp format is still wrong to not mess up.

        timestamp = False

        while timestamp is False:
            timestamp = input(
                ("Timestamp (use Format: YYYY-mm-ddTHH:MM:SS+00:00 2018-01-15T10:45:50+00:00) use c for current time "))

            if timestamp == 'c':
                timestamp = '{0:%Y-%m-%dT%H:%M:%S+00:00}'.format(datetime.datetime.now())
            timestamp = get_date(timestamp)

        timestamp_desc = input("timestamp_desc ")

        message = input("message ")

        return_value = current_sketch.add_event(timestamp=timestamp, message=message, timestamp_desc=timestamp_desc)
        objects = return_value.get("objects")
        first_element = objects[0]
        element_id = first_element.get("id")
        print("Event added, ID: "+str(element_id)+" Date:" + timestamp +" timestamp desc "+str(timestamp_desc)+" message"+message)
        logger.debug("Event added, ID: "+str(element_id)+" Date:" + timestamp +" timestamp desc "+str(timestamp_desc)+" message"+message)
        logger.debug(objects[0])

        again_input_value = input("Add another event? (y/n)")

        do_again = again(again_input_value)


def create_sketch(a_api_client=None, a_sketch_name=None):
    """
    Creates a new sketch and if ok print the URL to the sketch

    :param a_api_client:
    :param a_sketch_name:
    """
    logger.debug("create a sketch")
    if a_api_client is None:
        a_api_client = login()
    if a_sketch_name is None:
        a_sketch_name = input("What is the name of your new sketch? ")

    a_sketch_description = input("What is the description of your new sketch? ")

    return_value = a_api_client.create_sketch(a_sketch_name, description=a_sketch_description)

    element_id = return_value.id

    print("Created sketch "+a_sketch_name+" URL :"+TIMESKETCH_BASEURL+"/sketch/"+str(element_id)+"/")

def print_timelines(c_timelines):
    """
    prints a table by given timeline(s)
    :param c_timelines:
    """
    t = PrettyTable(['datetime', 'timestamp_desc','message', 'labels', '_id', "_index"])
    for current_sketch in c_timelines['objects']:
        source = current_sketch.get('_source')
        t.add_row([source.get('datetime'), source.get('timestamp_desc'), source.get('message'), ('[%s]' % ', '.join(map(str, source.get('label')))),
                   current_sketch.get("_id"), current_sketch.get("_index")])
    print(t)


def sketch(c_args):
    """
    Interaction with a dedicated sketch
    :param c_args:
    """
    c_api_client = login()
    #print(c_args)
    if c_args.option == 'list':
        if c_args.sketchid is not None:
            list_timelines_in_sketch(c_api_client, c_args.sketchid)
    elif c_args.option == 'search':
        if c_args.searchterm is not None:
            if c_args.sketchid is not None:
                c_sketch = c_api_client.get_sketch(int(c_args.sketchid))
                # not yet implemented
                search_result = search_in_sketch(c_api_client,a_sketch=c_sketch,a_search_term=c_args.searchterm)
            else:
                logger.error("no sketch ID given")
                print("no sketch ID given")
        else:
            logger.error("no searchterm given")
            print("no searchterm given")
    elif c_args.option == 'create':
        create_sketch(c_api_client,a_sketch_name=c_args.name)
    elif c_args.option == 'addevent':
        if c_args.sketchid is not None:
            interact_add_events(c_api_client,a_sketch_id=int(c_args.sketchid))
        else:
            logger.error("no sketch ID given")
            print("no sketch ID given")
    elif c_args.option == 'explore':
        if c_args.sketchid is not None:
            current_sketch = c_api_client.get_sketch(int(c_args.sketchid))
            explore_result = current_sketch.explore(query_string="*")
            print_timelines(explore_result)
        else:
            logger.error("no sketch ID given")
            print("no sketch ID given")
    elif c_args.option == 'analyze':
        if c_args.sketchid is not None:
            current_sketch = c_api_client.get_sketch(int(c_args.sketchid))
            if c_args.analyzer is not None:
                current_sketch = c_api_client.get_sketch(int(c_args.sketchid))
                if c_args.timeline is not None:
                    sketch = c_api_client.get_sketch(int(c_args.sketchid))
                    result = sketch.run_analyzer(c_args.analyzer, timeline_id=int(c_args.timeline))
                    print(result)
                    result2 = sketch.get_analyzer_status() # will give all the ran analyzers, so need to filter
                    for job in result2:
                        #print(job['index'])
                        #print(job)
                        if (job['analyzer'] == c_args.analyzer):
                            if (job['timeline_id'] == int(c_args.timeline)):
                                import pprint
                                pp = pprint.PrettyPrinter(indent=4)
                                pp.pprint(job)
                else:
                    logger.error("no timeline given")
            else:
                    logger.error("no analyzer name given")
        else:
            logger.error("no sketch ID given")
            print("no sketch ID given")




def sketches(args):
    """
    Here is a lot of work to do in order to get more functionality

    :param args:
    """
    api_client = login()
    print(args)
    list_sketches(api_client)


def searchindices(c_args):
    """

    :param c_args: provide all args given in the command line
    """
    api_client = login()

    if c_args.option == 'list':
        search_results = api_client.list_searchindices()
        t = PrettyTable(['id', "name", "Searchindex name"])
        for current_element in search_results:
            t.add_row([current_element.id, current_element.name, current_element.index_name])
        print(t)

    if c_args.option == 'merge': # DOES NOT WORK RIGHT NOW

        print("before")
        search_results = api_client.list_searchindices()
        t = PrettyTable(['id', "Searchindex name"])
        for current_element in search_results:
            t.add_row([current_element.id, current_element.name])
        print(t)

        if args.index_id1 is None:
            args.index_id1 = input("please provide index_id1")
        if args.index_id2 is None:
            args.index_id2 = input("please provide index_id2")
        print("going to merge two indices...")
        logger.debug(args.index_id1)
        logger.debug(args.index_id2)
        merge_results = api_client.merge_searchindex(args.index_id1,args.index_id2)

        print("after:")

        search_results = api_client.list_searchindices()
        t = PrettyTable(['id', "name", "Searchindex name" ])
        for current_element in search_results:
            t.add_row([current_element.id, current_element.name,current_element.index_name])
        print(t)



def event(c_args):
    """
        Interaction with a single event within a sketch.

        Add comment
        Add label
        display an event


    :param c_args:
    :return:
    """
    api_client = login()

    if args.sketchid is None:
        args.sketchid = input("please provide sketch id")

    if c_args.option == 'display':
        current_sketch = api_client.get_sketch(int(c_args.sketchid))
        query_string = "_id:"+args.event_id
        explore_result = current_sketch.explore(query_string=query_string)
        print_timelines(explore_result)
        return

    if args.event_id is None:
        args.event_id = input("please provide event_id")
    if args.index_id is None:
        args.index_id = input("please provide index_id")
    if args.text is None:
        args.text = input("Please provide your Text")

    if c_args.option == 'addComment':
        add_comment_to_event(c_api_client=api_client, a_sketch_id=int(args.sketchid), a_event_id=args.event_id,
                             a_index_id=args.index_id,a_comment_text=args.text)
    elif c_args.option == 'addLabel':
        add_label_to_event(c_api_client=api_client, a_sketch_id=int(args.sketchid), a_event_id=args.event_id,
                           a_index_id=args.index_id,a_label_text=args.text)
    else:
        print("no command given")
def upload(args):
    api_client = login()

    if args.sketchid is None:
        args.sketchid = input("please provide sketch id")

    if args.path is None:
        logger.error("No filepath given")
        args.path = input("please provide filepath to your file to upload ")

    if args.option == 'csv':
        current_sketch = api_client.get_sketch(int(args.sketchid))
        current_sketch.upload(timeline_name=args.name,file_path=args.path)


if __name__ == "__main__":

    logo()

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    # sketch
    parser_sketch = subparser.add_parser('sketch', description="Interact with a particular sketch")
    parser_sketch.add_argument('-sid', '--sketchid', help='output result value', action='store', required=False)
    parser_sketch.add_argument('-o', '--option', help='output result value', action='store', required=False,
                                     choices=['list','search','create','addevent','explore','analyze'],
                                     default='list')
    parser_sketch.add_argument('-st', '--searchterm', help='output result value', action='store', required=False)
    parser_sketch.add_argument('-n', '--name', help='name of the (potential) sketch', action='store', required=False)
    parser_sketch.add_argument('-tl', '--timeline', help='timeline value', action='store', required=False)
    parser_sketch.add_argument('-a', '--analyzer', help='analyser name', action='store', required=False)



    parser_sketch.set_defaults(func=sketch)

    # sketches
    parser_sketches = subparser.add_parser('sketches', description="Interact with sketches")
    parser_sketches.add_argument('-o', '--option', help='output result value', action='store', required=False,
                                     choices=['list'],
                                     default='list')
    parser_sketches.set_defaults(func=sketches)

    # modify event
    parser_modify_event = subparser.add_parser('modify_event', description="Interact with an event")
    parser_modify_event.add_argument('-o', '--option', help='output result value', action='store', required=False,
                                 choices=['addComment', 'addLabel','display'],
                                 default='display')
    parser_modify_event.add_argument("-eid","--event_id",nargs='?', help="event_id")
    parser_modify_event.add_argument("-iid", "--index_id", nargs='?', help="index_id")
    parser_modify_event.add_argument('-sid', '--sketchid', help='Sketch id', action='store', required=False)
    parser_modify_event.add_argument('-txt', '--text', help='text to be added', action='store', required=False)
    parser_modify_event.set_defaults(func=event)

    # searchindices
    parser_searchindices = subparser.add_parser('searchindices', description="Interact with an event")
    parser_searchindices.add_argument('-o', '--option', help='output result value', action='store', required=False,
                                     choices=['list','merge'],
                                     default='list')
    parser_searchindices.add_argument("-iid1", "--index_id1", nargs='?', help="index_id1")
    parser_searchindices.add_argument("-iid2", "--index_id2", nargs='?', help="index_id1")
    parser_searchindices.set_defaults(func=searchindices)

    # upload
    parser_sketch = subparser.add_parser('upload', description="Upload something")
    parser_sketch.add_argument('-sid', '--sketchid', help='output result value', action='store', required=False)
    parser_sketch.add_argument('-o', '--option', help='output result value', action='store', required=False,
                               choices=['csv'],
                               default='csv')
    parser_sketch.add_argument('-n', '--name', help='name of the (potential) sketch', action='store', required=False)
    parser_sketch.add_argument('-p', '--path', help='path to the file', action='store', required=False)

    parser_sketch.set_defaults(func=upload)



    args = parser.parse_args()

    args.func(args)



