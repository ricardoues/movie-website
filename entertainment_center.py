import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", 
                        "A story of a boy and his toy come to life", 
                        "https://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg", 
                        "https://www.youtube.com/watch?v=nCqtQLmJTl0"
                       )


thor_ragnarok = media.Movie("Thor Ragnarok", 
                            "I don't know yet", 
                            "https://upload.wikimedia.org/wikipedia/en/7/7d/Thor_Ragnarok_poster.jpg", 
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU") 

imitation_game = media.Movie("Imitation Game", 
                             "A computer scientist needs to break the codes of the enigma machine", 
                             "https://upload.wikimedia.org/wikipedia/en/5/5e/The_Imitation_Game_poster.jpg", 
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")

dunkirk = media.Movie("Dunkirk",
                      "This movie recreates the events behind the battle of dunkirk in the World War II",
                      "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",
                      "https://www.youtube.com/watch?v=F-eMt3SrfFU")

war_for_planet_apes = media.Movie("War for the Planet of the Apes", 
                                  "Cesar and his apes fight against an Human Army",
                                  "https://upload.wikimedia.org/wikipedia/en/d/d7/War_for_the_Planet_of_the_Apes_poster.jpg", 
                                  "https://www.youtube.com/watch?v=JDcAlo8i2y8")


rogue_one = media.Movie("Rogue One",
                        "The Death Star plans were captured by the Rebel Alliance", 
                        "https://upload.wikimedia.org/wikipedia/en/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY&t=57s")


movies = [toy_story, thor_ragnarok, imitation_game, dunkirk, war_for_planet_apes, rogue_one]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)
