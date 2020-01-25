# scraper.py

## Description

Generates (slowly) a complete offline version of the [Mozilla MDN Documentation](https://developer.mozilla.org/en-US/), removing all examples.
The generated documentation is designed for use in an exam environment where internet access is restricted yet access to the documentation is permitted.

## Usage

```
./scraper.py
```
All downloaded files are located in a directory called `output`.

## Improvements

* Currently the scraper works synchronously and processes a single link at a time. It would be highly beneficial to scrape multiple links at a time (perhaps with an argument to specify how many)
* There is currently no way of specifying a download directory (it is downloaded into a directory called `output`). This would be a useful feature
* A flag for deciding whether or not to remove examples would probably be useful in the case where someone wants to generate the documentation but retain the examples.