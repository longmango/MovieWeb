#!/usr/bin/python

import media
import fresh_tomatoes

Carol = media.Movie("Carol", "Therese Belivet (Rooney Mara) spots the beautiful, elegant Carol (Cate Blanchett) perusing the doll displays in a 1950s Manhattan department store. The two women develop a fast bond that becomes a love with complicated consequences.", "http://t0.gstatic.com/images?q=tbn:ANd9GcRpZ1zAKQT79-Eta6cTswgUPsB2R7hfxzIcxxowkpLr9xixJDj2", "https://www.youtube.com/watch?v=H4z7Px68ywk")

High_School_Musical = media.Movie("High School Musical", "Troy and Gabriella - two teens who are worlds apart - meet at a karaoke contest and discover their mutual love for music.", "http://www.gstatic.com/tv/thumb/movieposters/160369/p160369_p_v8_aa.jpg", "https://www.youtube.com/watch?v=9Q30yFZz4J8")

Silicon_Valley = media.Movie("Silicon Valley", "The series focuses on five young men who founded a startup company in Silicon Valley.", "http://www.gstatic.com/tv/thumb/tvbanners/13806643/p13806643_b_v8_aa.jpg", "https://www.youtube.com/watch?v=69V__a49xtw")

movies = [Carol, High_School_Musical, Silicon_Valley]
fresh_tomatoes.open_movies_page(movies)