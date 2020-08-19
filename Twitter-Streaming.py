import tweepy
# Setting.py
from Settings import APIKey, APISecret, AccessSecret, AccessToken
# GUID
import uuid

#///////////////////////////////////////////
# Generamos Un GUID 
#///////////////////////////////////////////
IdUnico = uuid.uuid4()
Guid = str(IdUnico)

#///////////////////////////////////////////
#Search Parameter
#///////////////////////////////////////////
SearchParameter = "correa"

class TweetsListener (tweepy.StreamListener):

    def on_connect(self):
        print ('Conexion estabecida')

    def on_status(self, status):
        # verificar campos disponibles dentro de  en staus
        # https://www.geeksforgeeks.org/python-status-object-in-tweepy/#:~:text=The%20Status%20object%20in%20Tweepy,time%20the%20status%20was%20posted.
        print('New Tweet')
        print ('id : ', status.id )
        print ('created : ', status.created_at)
        print ('user : ', status.user.name)
        print ('Tweet: ', status.text)
        print ('retweeted : ', status.retweeted )
        print ('retweet_count : ', status.retweet_count )
        
        # save Resultado        
        from SaveTweet import AddTweet
        AddTweet (Guid, status.created_at, status.id, status.user.name, status.text, SearchParameter, status.retweeted, status.retweet_count)
        
        
    def on_error(self, status_code):
        print ('Error: ', status_code)

#///////////////////////////////////////////
# Setting Autentificaion
#///////////////////////////////////////////
consumer_key = APIKey
consumer_secret = APISecret
access_token = AccessToken
access_token_secret = AccessSecret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit_notify=True, wait_on_rate_limit=True)

stream = TweetsListener()
streamingApi = tweepy.Stream(auth=api.auth,
                            listener=stream)

#///////////////////////////////////////////
# Metodo Streaming
#///////////////////////////////////////////
streamingApi.filter(
    # follow=["dsd1295057766126624773"] # Por UserId (Famoso)
     track=[SearchParameter] # Por palabra clave
    # site para get zone https://boundingbox.klokantech.com/ 
    #locations=[-92.20723923,-5.01593148,-75.19250402,1.88359633] # por zona geografica
    
)