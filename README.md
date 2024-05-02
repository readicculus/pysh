# Pysh - a phish.net API client in Python
Pysh is a Python wrapper for the [phish.net](phish.net) API that can be used to query for Phish songs, 
setlists, shows, venues, and other phish related data.  This project is not associated with phish.net and you must 
follow their API's terms of service while using this project.

This wraps the API described in the [phish.net API v5 Docs](https://docs.phish.net/).

## Requirements
#### API Key
You will need to setup an API key which requires you have a phish.net account.  
This library gets the key from the `PHISH_API_KEY` environment variable.  
Once you have your API key run the following before you can use this library.
```
export PHISH_API_KEY=xxx
```
You can alternatively pass the API key to the client when constructing it like this:
```
from pysh import Client
c = Client(apikey=xxx)
```


## Usage 
#### Filtering
There are a few ways to filter in your query calls.  Filtering is optional.
1. You can filter by id, for example if trying to get a show by the show id you can specify `get_shows(id=123)`
2. OR, you can filter by a category and value, the category being one of the attributes in the schema of that method. For 
example `get_shows(column='showyear', value='1995')` which returns all shows in 1995.

#### Additional Parameters
There are additional parameters you can define for all client methods defined by the `Parameters` class that allows you to 
define the following optional parameters if desired:
1. `order_by`: name of column to sort by
2. `direction`: direction to sort, either asc or desc (default asc)
3. `limit`: number, maximum number of results to return
4. `no_header`: if requesting data in HTML format, the argument _noheader will suppress the Phish.net banner
5. `callback`: if requesting data in JSON format, sending a callback will wrap the resulting JSON file in a callback function call
```
from pysh import Parameters, Client
c = Client()
c.get_shows(parameters=Parameters(order_by='showdate', direction='desc'))
```
You can read more about each of these parameters in the [Parameters Docs](https://docs.phish.net/#parameters)


## Client API Methods
Below are the currently available API methods usable via this client.  I've not yet added the three 
[special methods](https://docs.phish.net/special-methods) (attendance, reviews, and users) but will at some point.

Each pysh client method below corresponds to the phish.net api method and the return value is always a list 
of dictionaries with the below dictionary schema.

#### Shows (v5/shows)
```
get_shows(...) -> 
List[Dict{'showid', 'showyear', 'showmonth', 'showday', 'showdate', 'permalink', 'exclude_from_stats',
'venueid', 'setlist_notes', 'venue', 'city', 'state', 'country', 'artistid', 'artist_name',
'tourid', 'tour_name', 'created_at', 'updated_at'}]
```
#### Venues  (v5/venues)
```
get_venues(...) -> 
List[Dict{'venueid', 'venuename', 'city', 'state', 'country', 'venuenotes', 'alias', 'short_name'}]
```
#### Songs  (v5/songs)
```
get_songs(...) -> 
List[Dict{'songid', 'song', 'slug', 'abbr', 'artist', 'debut', 'last_played', 'times_played',
                      'last_permalink', 'debut_permalink', 'gap'}]
```
#### Songdata  (v5/songdata)
```
get_songdata(...) -> 
List[Dict{'songid', 'song', 'nickname', 'slug', 'lyrics', 'history', 'historian'}]
```
#### Setlists  (v5/setlists)
```
get_setlists(...) -> 
List[Dict{'showid', 'showdate', 'permalink', 'showyear', 'uniqueid', 'meta', 'reviews', 'exclude',
                  'setlistnotes', 'soundcheck', 'songid', 'position', 'transition', 'footnote', 'set', 'isjam',
                  'isreprise', 'isjamchart', 'jamchart_description', 'tracktime', 'gap', 'tourid', 'tourname',
                  'tourwhen', 'song', 'nickname', 'slug', 'is_original', 'venueid', 'venue', 'city', 'state',
                  'country', 'trans_mark', 'artistid', 'artist_slug', 'artist_name'}]
```
#### Artists  (v5/artists)
```
get_artists(...) -> 
List[Dict{'id', 'artist', 'slug'}]
```

#### Jamcharts  (v5/jamcharts)
```
get_jamcharts(...) -> 
List[Dict{'showid', 'showdate', 'permalink', 'showyear', 'uniqueid', 'meta', 'reviews', 'exclude',
                   'setlistnotes', 'soundcheck', 'songid', 'position', 'transition', 'footnote', 'set', 'isjam',
                   'isreprise', 'isjamchart', 'jamchart_description', 'tracktime', 'gap', 'tourid', 'tourname',
                   'tourwhen', 'song', 'nickname', 'slug', 'is_original', 'venueid', 'venue', 'city', 'state',
                   'country', 'trans_mark', 'artistid', 'artist_slug', 'artist_name'}]
```

---

## Examples

**Get all shows**
```
c.get_shows()
```

**Get a Show by Year**
```
c.get_shows(column="showyear", value="2020")
```

**Get a song by name**
```
c.get_songs(column="slug", value="bug")
```

**Get a setlist for a show by date**
```
c.get_setlists(column="showdate", value="1984-10-23")
```
