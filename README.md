# timesketch-tools
A dedicated repo to interact with the API of Timesketch

This is an unofficial tool and is iin no way supported by Google / Timesketch team.

Use on your own risk, might brake stuff...

# Installation

````
git clone https://github.com/deralexxx/timesketch-tools/
````

This repo is coming with a dedicated timesketch_api_client version 
to add some more functionality (but will be removed as soon as every PR is merged).


# Usage

```
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.1

            
usage: timesketch-tools.py [-h] [-v] [-ls] [-ae]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -ls, --list_sketches  list sketches
  -ae, --add_events     add events to a sketch

```

## add Event

You can add an event to a Sketch with:
 
```
timesketch-tools.py --add_events
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.1

            
Please provide the sketch id you want to add events to as (an integer): 3
Please provide informations to the event you would like to add timestamp, timestamp_desc, message will be promted

Timestamp (use Format: YYYY-mm-ddTHH:MM:SS+00:00 2018-01-15T10:45:50+00:00) use c for current time c
timestamp_desc this is the description
message something was hacked
Event added, ID: 18 Date:2018-10-31T14:49:41+00:00 timestamp desc this is the description messagesomething was hacked
Add another event? (y/n)n
```

## list sketches

You can list sketches in your timesketch instance

```
timesketch-tools.py -ls
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.1

            
+-----+-----------------------------+
|  id |             Name            |
+-----+-----------------------------+
| 130 |     test1Untitled sketch    |
|  3  | The Greendale investigation |
+-----+-----------------------------+

```


# Open issues

* add Labels to events
* search in Sketches
* create sketches
* get the new api_client version merged

# Contributing

Feel free to make pull requests or open issues to contribute to that repository