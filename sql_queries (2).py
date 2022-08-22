# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplay;"
user_table_drop = "DROP TABLE IF EXISTS users ;"
song_table_drop = "DROP TABLE IF EXISTS song;"
artist_table_drop = "DROP TABLE IF EXISTS artist; "
time_table_drop = "DROP TABLE IF EXISTS time;"



# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY NOT NULL , start_time TIME,\
                                user_id INT REFERENCES users, level VARCHAR, songid VARCHAR REFERENCES song,\
                                artistid VARCHAR REFERENCES artist, session_id INT, location VARCHAR, user_agent VARCHAR) """)


user_table_create = (""" CREATE TABLE IF NOT EXISTS users (user_id BIGINT PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR) """)


song_table_create = (""" CREATE TABLE IF NOT EXISTS song (songid VARCHAR PRIMARY KEY, title VARCHAR, artistid VARCHAR, year INT, duration NUMERIC) """)


artist_table_create = (""" CREATE TABLE IF NOT EXISTS artist (artistid VARCHAR PRIMARY KEY, name VARCHAR NOT NULL, location VARCHAR, \
                            latitude DOUBLE PRECISION, longitude DOUBLE PRECISION) """)


time_table_create = (""" CREATE TABLE IF NOT EXISTS time (start_time TIMESTAMPTZ NOT NULL, hour INT NOT NULL, day INT, week INT, month int, year INT, weekday INT) """)


songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY NOT NULL , start_time TIME,\
                                user_id INT REFERENCES users, level VARCHAR, songid VARCHAR REFERENCES song,\
                                artistid VARCHAR REFERENCES artist, session_id INT, location VARCHAR, user_agent VARCHAR) """)




# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays ( start_time, user_id, level, songid, artistid, session_id, location, user_agent) \
                                VALUES( %s, %s, %s, %s, %s, %s, %s, %s)  """ )


user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)  VALUES (%s, %s, %s, %s, %s) \
                          ON CONFLICT DO NOTHING      """ ) 
                   

song_table_insert = (""" INSERT INTO song (songid, title, artistid, year, duration)  VALUES (%s, %s, %s, %s, %s) \
                            ON CONFLICT DO NOTHING """ )
                       

artist_table_insert = (""" INSERT INTO artist (artistid, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) \
                            ON CONFLICT DO NOTHING""") 
                          

time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) """ )
                          



# FIND SONGS

song_select = (""" SELECT song.songid, artist.artistid FROM song join artist ON\
                    song.artistid = artist.artistid WHERE song.songid = %s AND artist.artistid = %s AND song.duration = %s """)



# QUERY LISTS

create_table_queries = [user_table_create, song_table_create, artist_table_create, time_table_create, songplay_table_create,]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]