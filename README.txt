This is the culmination of the entire class.

We have created a simple page utilizing the fresh_tomatoes.py to create and then display a .html page also called fresh_tomatoes.html.

File Layout:

media.py
-Creates the overall close Movie in order to allow us to create instances in following files.  Includes title, storyLine, posterImageURL, trailer_youtube_url and defines the method showTrailer, calling it on self.

entertainment_center.py
-Imports necessary files (media, fresh_tomatoes)
-Creates the instances of Movie (from file Media) and assigns variables therein
-Directly calls the fresh_tomatoes.open_movies_page function with the array movies as the arguments

fresh_tomatoes.py
-Precreated HTML template page
-Modified to add Synopsis for each movie beneat the title

Minimum System Requirements:
Python 2.7.9 Shell (for execution)

Preferred System Requirements:
Python IDLE

Execution Instructions:
1) Unzip entire directory into preferred folder on preferred machine
2) Open 'entertainment_center.py' in your preferred Python IDE
3) Execute 'entertainment_center.py' utilizing your IDE's run command

Support:
For support, please contact mbussinger@networkfactor.net or call 727-260-5000 (ext 5015)