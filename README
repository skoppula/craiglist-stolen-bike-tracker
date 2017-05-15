## Craiglist Stolen Bike Checker

After losing my bike, and losing my patience to check Craiglist everyday for my bike's sellers, I decided to write a script to do this job. Automation!

This script surveys the current Boston bike frontpage (`https://boston.craigslist.org/search/bia`). It filters posts based on a required keyword check and an optional keyword check. To run the script every hour, and accumulate matches in a `matches.txt` file, you can use a crontab on Unix machines: 

```
crontab -e
```

And select the desired editor to edit the crontab. Add the following line to the file:


```
0 * * * * python /path/to/craiglist-stolen-bike-tracker.py
```

### Adjust the filter config

Edit `craiglist-stolen-bike-tracker.py` to select where to output the results, and the filters.

The required keyword check filters posts on whether each posting has everyone of a set of required keywords:

```
required_keywords = [['bike','bicycle'], ['male','unisex']]
```

will match posts that have ('bike' OR 'bicycle') AND ('male' OR 'unisex').

The optional keyword check filters posts on whether the number of hits with the `optional_keywords` array matches or exceeds the threshold `num_opt_keywords_required`.


```
optional_keywords = ['vintage',['2008','2009']]
num_opt_keywords_required = 1
```
will match posts that have ('vintage' OR ('2008' or '2009))

This software is released with an MIT license.
