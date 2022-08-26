# Sparkify Song Analytics

This project is to build a **Database Model** to analyze the users song choice from the ***Sparkify****music streaming app* and also perform **ETL** opoeration on the build database.

This project includes various files which are used to build the database model and perform ETL process, each of which are described as follows.

### Files

 > **sql_queries.py** contains all your sql queries, which are further imported into the files below and this files has the query to build the database.
 > **create_tables.py** file drops and creates tables which are modeled and are specified in the above file, this file can be run to create the database for analytics.
 > **etl.ipynd** this file is a notebook which has the process to perform etl on the database.
 >**etl.py** this program file can be used to run to intiate the etl process directly.
 >**test.ipynb** is to verify if the etl process and the table creation are performed successfully by the program files above.
 
 >***Note***
 >
  >> users will not be able to run ***test.ipynb***,***etl.ipynb*** and ***etl.py*** until the ***create_tables.py*** is executed atleast once.


# Executing python scripts

>All the *.py* extension files can be executed using the command
>>***%run -i file_name.py***
  
## Database Model

The schema model used in this database is a **Star Schema**, *songplays* is the fact table in this database model, All the data collected in this fact table has referential integrity with the dimension tables in terms of *foriegn keys*.

The Dimension table in are:
-users
-song
-artist
-time

