# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users ;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist; "
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY , start_time TIME, user_id INT, level VARCHAR, songid VARCHAR, artistid VARCHAR, session_id INT,location VARCHAR,
                              user_agent VARCHAR) """)

user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id INT, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR) """)

song_table_create = (""" CREATE TABLE IF NOT EXISTS song (songid VARCHAR, title VARCHAR, artistid VARCHAR, year INT, duration NUMERIC) """)

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artist (artistid VARCHAR, artist_name VARCHAR, location VARCHAR, latitude NUMERIC, longitude NUMERIC) """)

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time TIME, hour INT, day INT, week INT, month int, year INT, weekday INT) """)

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (songplay_id, start_time, user_id, level, songid, artistid, session_id, location, user_agent)  VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)  """ )


user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)  VALUES (%s, %s, %s, %s, %s) """ ) 
                   


song_table_insert = (""" INSERT INTO song (songid, title, artistid, year, duration)  VALUES (%s, %s, %s, %s, %s)  """ )
                       


artist_table_insert = (""" INSERT INTO artist (artistid, artist_name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)  """) 
                          


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) """ )
                          
# FIND SONGS

song_select = (""" SELECT song.songid, artist.artistid FROM song join artist ON song.artistid = artist.artistid WHERE song.songid = %s AND artist.artistid = %s AND song.duration = %s """)
# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]