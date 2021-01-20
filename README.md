# spotify-songlist-by-date-musical-time-machine

App to create a top 100 songlist from your chosen year on your Spotify.
Have a particular summer you would like to reminisce about? 
Just enter the date and it will make a songlist from that era.

- Scrapes the Billboard Hot 100 site ("https://www.billboard.com/charts/hot-100") using Beatiful Soup,
    for all the songtitles from the date you enter when prompted.
    Enter date in YYYY-MM-DD format.
     
- Makes a list, extracts song titles

-Authenticates your Spotify account info, uses the spotify API to create a new playlist for that particular date.

    All imports included in main.py
    
    Get your spotify API key. -   https://developer.spotify.com/documentation/web-api/
    
    You will get an "access_token", make a file named 'token.txt' in your project. Place your access_token in that file so it 
    gets passed as a parameter with the "sp" object in main.py as "cache_path="token.txt" ..(It's there in main.py you'll see it..;)
    
    Use in conjunction with spotipy. -   https://spotipy.readthedocs.io/
    
    Spotipy is a lightweight Python library for the Spotify Web API. 
    With Spotipy you get full access to all of the music data provided by the Spotify platform.
    
    
 Log onto your Spotify account and enjoy your playlist! 
            
           
