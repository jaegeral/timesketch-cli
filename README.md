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
timesketch-tools.py --help
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.1

            
usage: timesketch-tools.py [-h] [-v] [-ls] [-ae] [-cs] [-name [NAME]]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         increase output verbosity
  -ls, --list_sketches  list sketches
  -ae, --add_events     add events to a sketch
  -cs, --create_sketch  create a sketch
  -name [NAME], --name [NAME]
                        name if needed

```

## add Event

You can add an event to a Sketch with:
 
```
timesketch-tools.py sketch -o addevent -sid 1
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
Please provide informations to the event you would like to add timestamp, timestamp_desc, message will be promted

Timestamp (use Format: YYYY-mm-ddTHH:MM:SS+00:00 2018-01-15T10:45:50+00:00) use c for current time c
timestamp_desc this is a description
message message test
Event added, ID: 41 Date:2018-11-09T09:46:46+00:00 timestamp desc this is a description messagemessage test
```

## list sketches

You can list sketches in your timesketch instance

```
timesketch-tools.py -ls
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.2

            
+-----+-----------------------------+
|  id |             Name            |
+-----+-----------------------------+
| 130 |     test1Untitled sketch    |
|  3  | The Greendale investigation |
+-----+-----------------------------+

```

## List searchindice

```
timesketch-tools.py searchindices -o list
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
+----+--------------------------+
| id |     Searchindex name     |
+----+--------------------------+
| 1  |       redline_test       |
| 2  |       redline_test       |
| 3  |          sample          |
| 4  |       redline_test       |
| 5  |       redline_test       |
| 6  |       redline_test       |
| 39 |         test123          |
| 40 |         test123          |
| 41 |         test1234         |
| 42 | sketch specific timeline |
| 43 |       my_timeline        |
+----+--------------------------+

```


## Create a new sketch



```
timesketch-tools.py sketch -o create -n testsketch
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
What is the description of your new sketch? this is a description
Created sketch testsketch URL :http://127.0.0.1:5000/sketch/2/

```

## list timelines in a sketch

```
timesketch-tools.py sketch -o list -sid 1
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
+----+--------------------------+
| id |           Name           |
+----+--------------------------+
| 39 |         test123          |
| 40 |         test1234         |
| 41 | sketch specific timeline |
| 42 |       my_timeline        |
+----+--------------------------+

```


# Open issues

* add Labels to events
* search in Sketches
* create sketches
* get the new api_client version merged

# Contributing

Feel free to make pull requests or open issues to contribute to that repository