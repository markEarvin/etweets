from django.db import models

# Create your models here.
  
class Article(models.Model):  
    title = models.CharField(max_length = 64)  
    content = models.TextField()

class TwitterTweet(models.Model):
	id = None
	user = None
	text = None
	created_at = None
	geo = None
	contributors = None
	coordinates = None
	favorited = None
	in_reply_to_screen_name = None
	in_reply_to_status_id = None
	in_reply_to_status_id_str = None
	in_reply_to_user_id = None
	in_reply_to_user_id_str = None
	place = None
	retweeted = None
	retweet_count = None
	source = None
	truncated = None

class TwitterOAuthCreds(models.Model):
	consumer_key = 'GeX90o2Tzb0f97QE3QIw'
	consumer_secret = 'RMHukHKBl8ntPz4wrBHoQHz6jBklU6GR5vE5hZwuk'
	access_token = '201619714-ZBtgVIDYfl5GLIeCjQi5EnwV8GwtFPAfv3fwiXWN'
	access_token_secret = 'NuN2QyNvWU6e3DH9tCLcbj5vnOOlHCCRUjGHXbKvGem46'

