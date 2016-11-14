# five-year-plan

five-year-plan is a small python application that can tweet made up five-year plans.
It uses the [indeed](http://www.indeed.com/) api for job descriptions (with [requests](http://docs.python-requests.org/en/master/) for http requests and [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to parse both xml and html) that are then the corpus for [markovify](https://github.com/jsvine/markovify) to create short sentences.
The short sentences are seeded with words or phrases that could make a good plan for the future.
The [tweepy](https://github.com/tweepy/tweepy) package is then used to tweet the plans.

## Setup Instructions

This package uses [pyyaml](http://pyyaml.org/wiki/PyYAMLDocumentation) to read a yaml file with your indeed publisher id and your twitter credentials.
In order to use five-year-plan, you need to save a yaml file named `credentials.yml` in the same directory as the `robot.py` file.  This yaml file should look like this: (replace the replace-me bits with your credentials)

```
indeed:
  publisher_id: replace-me
twitter:
  consumer_key: replace-me
  consumer_secret: replace-me
  access_token: replace-me
  access_token_secret: replace-me
```

Also, I'd recommend creating a virtual environment for this project.
It uses python 2.7, and then also needs to have all the packages in its `requirements.txt` installed in order to run. Happy future-ing!

## How to make it tweet as you

The file `robot.py` is set up to be run as a python script.
When executed, it will carry out the function that tweets one plan.
If you want the bot to tweet five-year plans for you once a day at noon, you can set up a cron job with the following crontab in order to do so:

```
# m h  dom mon dow   command
0 12 * * * /path/to/virtualenv/bin/python /path/to/five-year-plan/robot.py
```
