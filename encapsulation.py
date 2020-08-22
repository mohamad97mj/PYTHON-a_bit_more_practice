import oauth2
import urllib.parse as urlparse


class TwitterConsoleLogin:

    def __init__(self, consumer_key, consumer_secret):
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)

    def perform_twitter_login(self):
        request_token = self.get_request_token()
        verifier = self.get_oauth_verifier(request_token)
        return self.get_access_token(request_token, verifier)

    def __get_request_token(self):
        client = oauth2.Client(consumer)

        response, content = client.request("https://api.twitter.com/oauth/request_token", 'POST')
        if response.status != 200:
            print("An error occurred getting the request token from Twitter!")

        return dict(urlparse.parse_qsl(content.decode('utf-8')))

    def __get_oauth_verifier(self, request_token):
        print("Go to the following site in your browser:")
        print(get_oauth_verifier_url(request_token))

        return input("What is the PIN? ")

    def __get_oauth_verifier_url(self, request_token):
        return "{}?oauth_token={}".format("https://api.twitter.com/oauth/authorize", request_token['oauth_token'])

    def __get_access_token(self, request_token, oauth_verifier):
        token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
        token.set_verifier(oauth_verifier)

        client = oauth2.Client(consumer, token)

        response, content = client.request("https://api.twitter.com/oauth/access_token", 'POST')
        return dict(urlparse.parse_qsl(content.decode('utf-8')))


twitter_login = TwitterConsoleLogin("my_key", 'my_secret')
twitter_login.perform_twitter_login()
