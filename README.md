# Content Aggregator
Little content aggregator using python.

# What the project does
This repo has to little projects, one is the scraper and the other one is the flask application to show the data to the web.
- The 'ca_scrapy':
  It uses Scrapy to pull data from two sources I choosed randomly (theverge and wired). The scraper pulls the most popular articles from the day and save the name and url to the mongo database by using pipelines.
- The 'ca_flask':
  It's the web application that fetch the information from the database and return the data to a jinja template to be shown in the browser.
  
# What I learned
I learn a lot from this little project, I learned how to scrape data, how to recognize the important tags out of html pages, and also how to use Scrapy at a basic level. 

I also learned a lot using flask, how to use Blueprints, a configuration using config.py, and how to work with Jinja templates.

# How to run this app
### Requirements
- Mongodb
- Python 3.5+
First you need to create a virtualenv with python and then install the requirements.txt in order to have all the packages needed.

In order to fetch the articles you need to run the script at 'ca_scrapy' called spiders_runner.py
``` python spiders_runner.py ```

Then you need to define your flask enviromental variables:
``` #Linux
    export FLASK_APP=ca_flask
    export FLASK_DEBUG=1
```
After that you can run the application with:
``` flask run ```
