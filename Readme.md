# Sermon Scraper
My Dad asked me to download a bunch of sermons for him for Christmas and I'm too lazy to click all the buttons myself ;)

# Prerequisites
- python 3.8 (if you don't already have it, may I recommend pyenv)
- [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

# Usage

## Before anything else
```
pipenv shell
```

## Run the scraper
Download all sermons and metadata
```
scrapy runspider McLeanPres.py -o output/outfile.csv
```

Cleanup if you don't want the results
```
rm -r output
```

## Run the organizer
After you have run the scraper, organize the data into an easy-to-use format
```
python Organizer.py
```

Cleanup if you don't want the results
```
rm -r McLean\ Pres\ Sermons/
```

# Dev Tips
The [xpath helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)
Chrome extension makes life much easier when developing web scrapers.