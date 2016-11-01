import requests

"""
    This app uses the Requests http client library. So first ensure to `pip install Requests`
    
    Search for all songs of a given artist on itunes
    Just Change the artist name to your preferred artist
"""
#artist_name = {'term':'jack johnson'}
#artist_name = {'term':'michael jackson'}
#artist_name = {'term':'Beyonce'}
artist_name = {'term':'chris brown'}

itunes_request = requests.get('https://itunes.apple.com/search?', params = artist_name)

# we check that the response status is 200
if itunes_request.status_code != requests.codes.ok:

    # in case of a typo in the url for instance
    print 'Search unsuccesful'
    print 'HTTP Status Code: ' + str(itunes_request.status_code)

else:
    print 'Search successful. Displaying data in json format'
    results_text = itunes_request.text
    print results_text

    # we are not done yet
    # let's create a new txt file and write this data onto our hard drive
    itune_song_results = open("itunes.txt", "w")
    itune_song_results.write(results_text)

    itune_song_results.close()


