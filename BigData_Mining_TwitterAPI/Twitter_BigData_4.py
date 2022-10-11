'''
Jesus Macias

This program gets and displays the ID, name, screen name and 
description of the Marvel Studios Twitter account.
'''
import tweepy
import keys

# accessing the twitter account
auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)

# initializing api
api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.get_user('MarvelStudios')
print("User ID:",user.id) # account number
print("\nScreen Name:", user.screen_name) # screen name
print("\nAccount Name:", user.name) # name of account
print("\nDescription of Account:", user.description) # bio
print("\nMost Recent Tweet from User:", user.status.text) # last tweet
print("\nUser Follower Count:", user.followers_count) # followers
print("\nUser Following Count:", user.friends_count) # following

'''
OUTPUT:
User ID: 750751206427860992

Screen Name: MarvelStudios

Account owner name: Marvel Studios

Description of Account: The official Twitter account for Marvel Studios. Experience Marvel Studios’ Eternals only in theaters NOW. 💫
GET TICKETS NOW ↙️

Most Recent Tweet from User: Don’t miss the #1 Movie in the World that changes the Marvel 
Universe FOREVER. 🤯 Experience Marvel Studios’… https://t.co/NyBRWyEPRM

User Follower Count: 7354290

User Following Count: 102
'''
