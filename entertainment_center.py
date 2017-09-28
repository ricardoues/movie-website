import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toy come to life",
                        "https://goo.gl/LndV7F",
                        "https://www.youtube.com/watch?v=nCqtQLmJTl0")

thor_ragnarok = media.Movie("Thor Ragnarok",
                            "I don't know yet",
                            "https://goo.gl/r7MpL7",
                            "https://www.youtube.com/watch?v=v7MGUNV8MxU")

imitation_game = media.Movie("Imitation Game",
                             "A computer scientist needs \
                              to break the codes of the \
                              enigma machine",
                             "https://goo.gl/1x78fT",
                             "https://www.youtube.com/watch?v=S5CjKEFb-sM")

dunkirk = media.Movie("Dunkirk",
                      "This movie recreates the events \
                       behind the battle of dunkirk \
                       in the World War II",
                      "https://goo.gl/3VS61H",
                      "https://www.youtube.com/\
                       watch?v=F-eMt3SrfFU")

war_for_planet_apes = media.Movie("War for the Planet of the Apes",
                                  "Cesar and his apes fight \
                                   against an Human Army",
                                  "https://goo.gl/51cijY",
                                  "https://www.youtube.com/\
                                   watch?v=JDcAlo8i2y8")

rogue_one = media.Movie("Rogue One",
                        "The Death Star plans were \
                         captured by the Rebel Alliance",
                        "https://goo.gl/7EJJEx",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

movies = [toy_story, thor_ragnarok, imitation_game,
          dunkirk, war_for_planet_apes, rogue_one]

fresh_tomatoes.open_movies_page(movies)

