from timesketch_api_client.client import TimesketchApi
import configparser
import logging
import argparse
import datetime


# Hack to disable warning...
import urllib3

urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)


logger = logging.getLogger('timesketch')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s() - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)


config = configparser.ConfigParser()
config.read("config_demo.config")
# config.read("config_prod.config")

TIMESKETCH_BASEURL = config.get('TIMESKETCH', 'BASEURL')
TIMESKETCH_USERNAME = config.get('TIMESKETCH', 'USERNAME')
TIMESKETCH_PASSWORD = config.get('TIMESKETCH', 'PASSWORD')
TIMESKETCH_HTTPS_VERIFY = config.getboolean('TIMESKETCH', 'HTTPS_VERIFY')
TIMESKETCH_TOOLS_VERSION = config.get('TIMESKETCH', 'version')


def login():
    """

    :return: api_client object with a valid session
    """
    logger.debug("Login attampt to " + TIMESKETCH_BASEURL)
    c_api_client = TimesketchApi(TIMESKETCH_BASEURL, username=TIMESKETCH_USERNAME, password=TIMESKETCH_PASSWORD)
    logger.debug("Login attampt status")

    return c_api_client


def list_sketches(a_api_client=None):
    """
    Lists all sketches in a Timesketch instance
    :param a_api_client: login needed before
    """
    if a_api_client is None:
        a_api_client = login()

    sketches = a_api_client.list_sketches()
    from prettytable import PrettyTable
    t = PrettyTable(['id', 'Name'])
    for current_sketch in sketches:
        t.add_row([current_sketch.id, current_sketch.name])
    print t


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
    a_sketch.search(a_search_term)
    logger.error("Not yet implemented")


def console():
    logger.error("Not implemented yet")
    raise NotImplementedError


def add_label_to_event():
    """
    TODO Implement
    """
    c_api_client = TimesketchApi(TIMESKETCH_BASEURL, username=TIMESKETCH_USERNAME, password=TIMESKETCH_PASSWORD)
    current_sketch = c_api_client.get_sketch(3)
    return_value = current_sketch.label_events(145, "aaa")
    logger.debug("test")


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
    print "Sorry - Date %s is not in expected format - Try again" % (a_date)
    return False


def logo():

        print("""     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _ \
         
        /_/ /_/_/_/_/\__/___/_/\_\\__/\__/\__/_//_/-tools v{}

            """.format(TIMESKETCH_TOOLS_VERSION))


def again(user_input):
    # raw_input returns the empty string for "enter"
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
            timestamp = raw_input(
                ("Timestamp (use Format: YYYY-mm-ddTHH:MM:SS+00:00 2018-01-15T10:45:50+00:00) use c for current time "))

            if timestamp == 'c':
                timestamp = '{0:%Y-%m-%dT%H:%M:%S+00:00}'.format(datetime.datetime.now())
            timestamp = get_date(timestamp)

        timestamp_desc = raw_input("timestamp_desc ")

        message = raw_input("message ")

        return_value = current_sketch.add_event(timestamp=timestamp, message=message, timestamp_desc=timestamp_desc)
        objects = return_value.get("objects")
        first_element = objects[0]
        element_id = first_element.get("id")
        print("Event added, ID: "+str(element_id)+" Date:" + timestamp +" timestamp desc "+str(timestamp_desc)+" message"+message)
        logger.debug("Event added, ID: "+str(element_id)+" Date:" + timestamp +" timestamp desc "+str(timestamp_desc)+" message"+message)

        again_input_value = raw_input("Add another event? (y/n)")

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
        a_sketch_name = raw_input("What is the name of your new sketch? ")

    a_sketch_description = raw_input("What is the description of your new sketch? ")

    return_value = a_api_client.create_sketch(a_sketch_name, description=a_sketch_description)

    element_id = return_value.id

    print("Created sketch "+a_sketch_name+" URL :"+TIMESKETCH_BASEURL+"/sketch/"+str(element_id)+"/")


if __name__ == "__main__":

    logo()

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-ls", "--list_sketches", help="list sketches",
                        action="store_true")
    parser.add_argument("-ae", "--add_events", help="add events to a sketch", action="store_true")
    parser.add_argument("-cs", "--create_sketch", help="create a sketch", action="store_true")
    parser.add_argument("-name", "--name",nargs='?', help="name if needed")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.DEBUG)

    if args.list_sketches:
        api_client = login()
        list_sketches(api_client)
    elif args.add_events:
        api_client = login()
        sketch = None
        interact_add_events(api_client, sketch)
    elif args.create_sketch:
        api_client = login()
        if args.name is None:
            create_sketch(a_api_client=api_client, a_sketch_name=None)
        else:
            create_sketch(a_api_client=api_client, a_sketch_name=args.name)

    else:
        print("no command given")
