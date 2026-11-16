#!/usr/bin/python3
"""Query the Reddit API for the number of subscribers of a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers of a given subreddit.

    Return 0 if the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/user)"}

    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return 0
        return response.json().get("data", {}).get("subscribers", 0)
    except (requests.RequestException, ValueError):
        return 0
