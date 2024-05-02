from enum import Enum


# TODO add special methods
class ApiMethod(Enum):
    ARTISTS = 'artists'
    JAMCHARTS = 'jamcharts'
    SETLISTS = 'setlists'
    SHOWS = 'shows'
    SONGDATA = 'songdata'
    SONGS = 'songs'
    VENUES = 'venues'


API_METHOD_SCHEMA = {
    ApiMethod.ARTISTS: ['id', 'artist', 'slug'],
    ApiMethod.JAMCHARTS: ['showid', 'showdate', 'permalink', 'showyear', 'uniqueid', 'meta', 'reviews', 'exclude',
                          'setlistnotes', 'soundcheck', 'songid', 'position', 'transition', 'footnote', 'set', 'isjam',
                          'isreprise', 'isjamchart', 'jamchart_description', 'tracktime', 'gap', 'tourid', 'tourname',
                          'tourwhen', 'song', 'nickname', 'slug', 'is_original', 'venueid', 'venue', 'city', 'state',
                          'country', 'trans_mark', 'artistid', 'artist_slug', 'artist_name'],
    ApiMethod.SETLISTS: ['showid', 'showdate', 'permalink', 'showyear', 'uniqueid', 'meta', 'reviews', 'exclude',
                         'setlistnotes', 'soundcheck', 'songid', 'position', 'transition', 'footnote', 'set', 'isjam',
                         'isreprise', 'isjamchart', 'jamchart_description', 'tracktime', 'gap', 'tourid', 'tourname',
                         'tourwhen', 'song', 'nickname', 'slug', 'is_original', 'venueid', 'venue', 'city', 'state',
                         'country', 'trans_mark', 'artistid', 'artist_slug', 'artist_name'],
    ApiMethod.SHOWS: ['showid', 'showyear', 'showmonth', 'showday', 'showdate', 'permalink', 'exclude_from_stats',
                      'venueid', 'setlist_notes', 'venue', 'city', 'state', 'country', 'artistid', 'artist_name',
                      'tourid', 'tour_name', 'created_at', 'updated_at'],
    ApiMethod.SONGDATA: ['songid', 'song', 'nickname', 'slug', 'lyrics', 'history', 'historian'],
    ApiMethod.SONGS: ['songid', 'song', 'slug', 'abbr', 'artist', 'debut', 'last_played', 'times_played',
                      'last_permalink', 'debut_permalink', 'gap'],
    ApiMethod.VENUES: ['venueid', 'venuename', 'city', 'state', 'country', 'venuenotes', 'alias', 'short_name']
}
