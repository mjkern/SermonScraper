# Sermon Scraper
My Dad asked me to download a bunch of sermons for him for Christmas and I'm too lazy to click all the buttons myself ;)

# Prerequisites
- python 3.8 (if you don't already have it, may I recommend pyenv)
- [pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

# Usage

When first opening the project
```
pipenv shell
```

Then run the scraper
```
scrapy runspider McLeanPres.py -o outfile.csv
```

Cleanup (if you don't want the new results to append to the old)
```
rm outfile.csv
```

# Dev Tips
The [xpath helper](https://chrome.google.com/webstore/detail/xpath-helper/hgimnogjllphhhkhlmebbmlgjoejdpjl)
Chrome extension makes life much easier when developing web scrapers.