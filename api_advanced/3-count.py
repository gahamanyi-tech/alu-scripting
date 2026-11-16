#!/usr/bin/python3
"""Recursively count keywords in the hot article titles of a subreddit."""
import requests


def print_counts(word_list, counts):
    """Print keyword counts sorted by count (desc), then word (asc)."""
    lowered = [word.lower() for word in word_list]
    totals = {}
    for word, number in counts.items():
        total = number * lowered.count(word)
        if total > 0:
            totals[word] = total
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(word, total))


def count_words(subreddit, word_list, after=None, counts=None):
    """Query hot articles recursively and print keyword counts.

    Print nothing if the subreddit is invalid or nothing matches.
    """
    if counts is None:
        counts = {word.lower(): 0 for word in word_list}

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
            return
        data = response.json().get("data", {})
    except (requests.RequestException, ValueError):
        return

    for post in data.get("children", []):
        title = post.get("data", {}).get("title") or ""
        for token in title.lower().split():
            if token in counts:
                counts[token] += 1

    next_page = data.get("after")
    if next_page:
        return count_words(subreddit, word_list, next_page, counts)
    print_counts(word_list, counts)
