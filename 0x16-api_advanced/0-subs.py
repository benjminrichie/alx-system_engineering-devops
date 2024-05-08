#!/usr/bin/python3
"""
This script queries subscribers on a given Reddit subreddit
"""

import requests

def number_of_subscribers(subreddit):
    # Reddit API URL to get information about the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/1.0'}
    
    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers)
    
    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract and return the number of subscribers
        return data['data']['subscribers']
    else:
        # If the subreddit is invalid, return 0
        return 0

# Test the function
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
