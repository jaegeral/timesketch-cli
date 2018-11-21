=Idea=

From time to time you might need to convert certain date strings or even multiple dates.

E.g. you have a Excel file where you have a timestamp and want to export it to an csv to import it to timesketch.

Now you can copy the column from your excel file date to input.txt:

```
2018-10-15 15:35:19
2018-10-15 17:39:00
2018-10-15 18:52:06
2018-11-02 10:25:58
2018-11-13 17:58:41
2018-11-14 01:48:34
2018-11-14 08:23:10
```

Then start date_converter.py:
```
python3 date_converter.py
```

That will create two files, datetime.txt and timestamp.txt

datetime.txt:
```
2018-10-15T15:35:19+00:00
2018-10-15T17:39:00+00:00
2018-10-15T18:52:06+00:00
2018-11-02T10:25:58+00:00
2018-11-13T17:58:41+00:00
2018-11-14T01:48:34+00:00
2018-11-14T08:23:10+00:00
```

and timestamp.txt:
```
1539610519000
1539617940000
1539622326000
1541150758000
1542128321000
1542156514000
1542180190000
```

Not you can simply create two new columns in your excel file, copy all the calues and you are good to go.