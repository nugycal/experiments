# Reddit Experiments

## Scraper

**scraper** is a tool written to scrape submissions from a specified subreddit. It utilises [PRAW (the Python Reddit API Wrapper)](https://praw.readthedocs.io/en/latest/) to get this information. This data is then parsed into a desired format and is stored into a csv table using the python module [pandas](https://pypi.org/project/pandas/).

### Usage

```
./scraper <subreddit> <user>
./scraper unixporn nugycal
```

## import_csv

This is a tool written to use the generated data from **scraper** to inject data into the COMP2041 project [seddit](https://cgi.cse.unsw.edu.au/~cs2041/19T2/assignments/ass2/index.html).

It extracts any images/links to images from a post, downloads the image and then base64 encodes the images. It then handles the user authorisation required to post the images - it will attempt to login to a user account with the author of the reddit post's name using the password "password". If this is unsuccessful, it will create a new account for this user with the password "password". It will then submit the post into the correct corresponding 'subseddit', and move on to the next entry in the table.

### Usage
```
./import_csv <csv file> <api endpoint>
```

#### Notice: Issues have been known to arise from attempting to use this with an endpoint which is not local