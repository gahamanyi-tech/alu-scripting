# api_advanced

Scripts that query the Reddit API.

## Files

- `0-subs.py`: `number_of_subscribers(subreddit)` returns the total
  number of subscribers for a subreddit, or 0 if the subreddit is invalid.

## Usage

    python3 0-main.py programming
- `2-recurse.py`: `recurse(subreddit, hot_list=None, after=None)` recursively
  returns a list of all hot article titles, or None if the subreddit is
  invalid.
- `3-count.py`: `count_words(subreddit, word_list)` recursively counts
  keywords in hot article titles and prints them sorted.
