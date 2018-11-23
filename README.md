# timesketch-tools
A dedicated repo to interact with the API of Timesketch

This is an unofficial tool and is in no way supported by Google / Timesketch team.

Use on your own risk, might break stuff...

# Installation

````
git clone https://github.com/deralexxx/timesketch-tools/
````

This repo is coming with a dedicated timesketch_api_client version 
to add some more functionality (but will be removed as soon as every PR is merged).


# Usage

```
timesketch-tools.py -h
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.4

            
usage: timesketch-tools.py [-h]
                           {sketch,sketches,modify_event,searchindices,upload}
                           ...

positional arguments:
  {sketch,sketches,modify_event,searchindices,upload}

optional arguments:
  -h, --help            show this help message and exit

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

## Comment an event

```
timesketch-tools.py modify_event -o addComment --event_id AWQw5_NpeBLZMUY_lr62 --index_id ae92d77b677b43c7802a2ebe767d947d
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
please provide sketch id1
Please provide your comment Textthis is a wonderful comment
```

## Display a single event

```
timesketch-tools.py modify_event -o display --event_id AWQw5_NpeBLZMUY_lr62 --sketchid 1
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.3

            
+---------------------+-------------------------------+--------------------------------------------------------------------+---------------------------------------+----------------------+----------------------------------+
|       datetime      |         timestamp_desc        |                              message                               |                 labels                |         _id          |              _index              |
+---------------------+-------------------------------+--------------------------------------------------------------------+---------------------------------------+----------------------+----------------------------------+
| 2013-05-15T18:38:24 | File/PEInfo/PETimestamp Files | C:\Windows\System32\qlco10011.dll e7c984669e9e22c7d8ba55a101a07fcb | [__ts_comment, foo_label, labeltest2] | AWQw5_NpeBLZMUY_lr62 | ae92d77b677b43c7802a2ebe767d947d |
+---------------------+-------------------------------+--------------------------------------------------------------------+---------------------------------------+----------------------+----------------------------------+
```

## Add a tag from pyTaxonomie to Timesketch

```
python3 timesketch-tools.py modify_event -o addLabel --event_id AWc19oPsqgYnbgC2IIEH --index_id 1f9d42fd839a4324b0c4dcc1d47b55d2
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.4

            
please provide sketch id1
Please provide your Text
do you want to search within the pyTaxonomies? (y/n) y
Term you want to search for e.g. PAP, TLP, ...tlp
Suggestions
tlp:amber
tlp:white
tlp:green
tlp:ex:chr
tlp:red
again?y
Term you want to search for e.g. PAP, TLP, ...TLP
Suggestions
Seems we did not find the value 'NoneType' object has no attribute 'machinetags_expanded'
Term you want to search for e.g. PAP, TLP, ...pap
Suggestions
Seems we did not find the value 'NoneType' object has no attribute 'machinetags_expanded'
Term you want to search for e.g. PAP, TLP, ...PAP
Suggestions
PAP:AMBER
PAP:WHITE
PAP:GREEN
PAP:RED
again?n
Give labelPAP:WHITE

```

## Search in a sketch

The searchterm can be used with "*" in front or back to have every character.
The search is not case sensitive.

````
timesketch-tools.py sketch -o search -sid 1 -st *win*
     
         _______               __       __      __ 
        /_  __(_)_ _  ___ ___ / /_____ / /_____/ / 
         / / / /  ' \/ -_|_-</  '_/ -_) __/ __/ _          
        /_/ /_/_/_/_/\__/___/_/\_\__/\__/\__/_//_/-tools v0.4

            
Searching for: '*win*' in sketch 'aaaUntitled sketch'
+---------------------------+----------------------------------------------------------+--------+----------------------+----------------------------------+
|          datetime         |                         message                          | labels |         _id          |              _index              |
+---------------------------+----------------------------------------------------------+--------+----------------------+----------------------------------+
| 2018-10-15T18:52:06+00:00 |                           win                            |   []   | AWc__lO_IUecPZLawtVa | 524f5e7b530a16eba408968369e5a716 |
| 2018-10-15T18:52:06+00:00 | Windows Domain admin credentials gone away to the hacker |   []   | AWdAAExzIUecPZLawtVb | 524f5e7b530a16eba408968369e5a716 |
+---------------------------+----------------------------------------------------------+--------+----------------------+----------------------------------+

````

# timesketch-tools vs tsctl

tsctl is the tool used locally on the timesketch machine.
timesketch-tools is made to be used with the API from any machine that has network connection to the timesketch instance.

# Open issues

* add Labels to events
* search in Sketches
* create sketches
* get the new api_client version merged

# Contributing

Feel free to make pull requests or open issues to contribute to that repository