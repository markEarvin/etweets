from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.

#from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from feeds.models import TwitterOAuthCreds

import tweepy
from tweepy import StreamListener, Stream

#tweets streamer
class StdOutListener(StreamListener):
 
	def on_data(self, data):
		print data
		return True

	def on_error(self, status):
		print status


def TwitterFeedsView(request):
	return HttpResponse("Hello, world. You're at twitter feed view")

def index(request):
	auth = tweepy.OAuthHandler(TwitterOAuthCreds.consumer_key, TwitterOAuthCreds.consumer_secret)
	auth.set_access_token(TwitterOAuthCreds.access_token, TwitterOAuthCreds.access_token_secret)

	api = tweepy.API(auth, retry_count=3, retry_delay=5, retry_errors = set([401, 404, 500, 503]))
	res = api.search(q="rudy gay")
	search_results = {}
	for result in res:
		#print result.text
		search_results[str(result.id)] = result.text

	print "# of results: " + str(len(search_results))
	#print "search: " + str(search_results)
	context = {'search_results': res}

	return render(request, 'twitter/index.html', context)
