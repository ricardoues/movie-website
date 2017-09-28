import webbrowser

class Movie(object):
      """This class is for storing movie information """

      def __init__(self, movie_title, movie_storyline, 
                   poster_image, trailer_youtube):
          """ 
          Initialize the movie instance. 
          Arguments:
          self: refers to the current instance
          movie_title: title of the movie 
          movie_storyline: the plot of the movie 
          poster_image: poster of the movie 
          trailer_youtube: url of the trailer movie 
          Returns:
          None 
          """ 

          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_youtube

      def show_trailer(self):
          """
          Show the movie trailer. 
          Arguments: 
          self: refers to the current instance
          Returns:
          None
          """ 
          webbrowser.open(self.trailer_youtube_url)


