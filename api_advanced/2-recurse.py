#!/usr/bin/python3
"""Recursively query the Reddit API for the hot article titles."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of the titles of all hot articles of a subreddit.

    Return None if the subreddit is invalid or has no results.
    """
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/user)"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10)
        if response.status_code != 200:
            return hot_list or None
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return hot_list or None

    for post in data.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    next_page = data.get("after")
    if next_page:
        return recurse(subreddit, hot_list, next_page)
    return hot_list or None
