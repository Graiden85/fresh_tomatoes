#import webbrowser to access trailer open function
import webbrowser
#overclass for each instance defined in the other file
class Movie():
    """Here ye shall find general formatting for yonder class"""
    def __init__(self, title, storyLine, posterImageURL, trailer_youtube_url):
        self.title = title
        self.storyLine = storyLine
        self.posterImageURL = posterImageURL
        self.trailer_youtube_url = trailer_youtube_url

    def showTrailer(self):
        webbrowser.open(self.trailer_youtube_url)
