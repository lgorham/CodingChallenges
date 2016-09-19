from bs4 import BeautifulSoup
from selenium import webdriver

def find_album(html):

    all_html = BeautifulSoup(html, 'html.parser')
    album = all_html.findAll("div", {"class" : "_XWk"})
    album = album[0].text

    return album


def find_track(html):

    all_html = BeautifulSoup(html, 'html.parser')
    tracks = all_html.findAll("div", {"class" : "_wjf"})
    return tracks[2].text


def parse_lyrics(html):

    all_html = BeautifulSoup(html, 'html.parser')
    lyrics = all_html.findAll("div", {"class" : "_G1d _wle _xle"})

    return lyrics[0].text
    

def find_lyrics(artist):

    print "Starting search"

    driver = webdriver.Firefox()

    driver.get("https://www.google.com/search?q=most+recent+david+bowie+album&oq=most+recent+david+bowie+album&aqs=chrome..69i57.4199j0j9&sourceid=chrome&ie=UTF-8")

    album = driver.page_source

    latest_album = find_album(album)

    latest_album.replace(" ", "+")

    driver.get("https://www.google.com/search?q=track+list+{}&oq=track+list+{}&aqs=chrome..69i57.3559j0j9&sourceid=chrome&ie=UTF-8".format(latest_album, latest_album))

    third_track = driver.page_source

    track = find_track(third_track)

    track.replace(" ", "+")

    driver.get("https://www.google.com/search?q=lyrics+{}+bowie&oq=lyrics+{}+bowie&aqs=chrome..69i57.4592j0j1&sourceid=chrome&ie=UTF-8".format(track, track))

    song = driver.page_source

    lyrics = parse_lyrics(song)

    print lyrics




find_green_day()