# five-year-plan

five-year-plan is a small python application that can tweet made up five-year plans. It uses the indeed api, the markovify python package, and the tweepy python package. It takes job descriptions from indeed, uses them as the corpus forthe markov chain generator made by markovify. With a little but of massaging, it then tries to make sensible plans for your future.

## Setup Instructions

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

Also, I'd recommend creating a virtual environment for thisproject. It uses python 2.7, and then also needs to have all the packages in its `requirements.txt` installed in order to run. Happy future-ing!

## How to make it tweet as you

The function that does everything is *tweet_a_five_year_plan()*

It will tweet one!  Good luck. :)
