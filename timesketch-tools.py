from timesketch_api_client.client import TimesketchApi
import configparser
import logging
import argparse


logger = logging.getLogger('timesketch')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


config = configparser.ConfigParser()
config.read("config.config")

TIMESKETCH_BASEURL = config.get('TIMESKETCH', 'BASEURL')
TIMESKETCH_USERNAME = config.get('TIMESKETCH', 'USERNAME')
TIMESKETCH_PASSWORD = config.get('TIMESKETCH', 'PASSWORD')
TIMESKETCH_HTTPS_VERIFY = config.getboolean('TIMESKETCH', 'HTTPS_VERIFY')

def login():
    api_client = TimesketchApi(TIMESKETCH_BASEURL,username = TIMESKETCH_USERNAME, password = TIMESKETCH_PASSWORD,verify=TIMESKETCH_HTTPS_VERIFY)
    TimesketchApi
    return api_client

def list_sketches(api_client=None):
    sketches =  api_client.list_sketches()
    from prettytable import PrettyTable
    t = PrettyTable(['id', 'Name'])
    for sketch in sketches:
        t.add_row([sketch.id, sketch.name])
    print t

def getSketch(api_client = None, a_sketch_id = None):
    sketch = api_client.get_sketch(int(a_sketch_id))
    return sketch

def search_in_sketch(api_client = None, a_sketch = None, search_term = None):
    a_sketch.search(search_term)
    logger.error("Not yet implemented")



if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="increase output verbosity",
                        action="store_true")
    parser.add_argument("-ls", "--list_sketches", help="list sketches",
                        action="store_true")
    parser.add_argument("-sk", "--sketch", help="get sketch")
    parser.add_argument("-s", "--search", help="search for the term in sketch")

    args = parser.parse_args()

    if args.verbose:
        logger.setLevel(logging.NOTSET)

    if args.list_sketches:
        api_client = login()
        list_sketches(api_client)
    elif args.sketch:
        api_client = login()
        sketch = getSketch(api_client, args.sketch)
        if args.search:
            search_in_sketch(api_client,sketch,search_term=args.search)

    else:
        print "no command given"

