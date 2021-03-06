# DB
import pymysql

# Conexion
# //////////////////////////////////////
from Settings import Conexion

# Add Tweet
def AddTweet (GUID, DateTweet, IdTweet, user, Tweet, Parameter, retweeted, retweet_count, lang):
  
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `TweetData` ( `GUID`, `DateTweet`, `IdTweet`, `user`, `Tweet`,  `Parameter`,  `retweeted`,  `retweet_count`, `lang`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (GUID, DateTweet, IdTweet, user, Tweet, Parameter, retweeted, retweet_count, lang))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("*******************************************************************")
            print ("   --  Registro Insertado corectamente")
            print ("*******************************************************************")
    except:
        print ('Error en Conexion...')        

    finally:
        connection.close()

# Add Tweet
def OldTweet (Guid, createdtweet, idtweet, usertweet, TweetMsg, SearchParameter, retweeted, retweet_count, lang):
  
    # Connect to the database
    connection = pymysql.connect(host=Conexion[0],
                            user=Conexion[1],
                            password=Conexion[2],
                            db=Conexion[3],
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
        # Create a new record
                         
            sql = "INSERT INTO `OldData` ( `GUID`, `createdtweet`, `idtweet`, `usertweet`, `TweetMsg`,  `SearchParameter`,  `retweeted`,  `retweet_count`, `lang`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, (Guid, createdtweet, idtweet, usertweet, TweetMsg, SearchParameter, retweeted, retweet_count, lang))
            
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
            print ("*******************************************************************")
            print ("   --  Registro Insertado corectamente")
            print ("*******************************************************************")
    except:
        print ('Error en Conexion...')        

    finally:
        connection.close()