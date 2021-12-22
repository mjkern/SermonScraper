from scrapy.spiders import Spider
from scrapy import Request

class McLeanPres(Spider):
    """
    Scrapes sermons from McLean Presbyterian Church, according to sermon series
    """

    # basic settings
    name = "McLeanPresSermonSpider"
    allowed_domains = ["mcleanpres.org"]
    start_urls = ["https://mcleanpres.org/sermons/series/all"]

    # don't abuse the website
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter'
    }

    def parse(self, response):
        # parse each series from the page
        all_series = response.xpath("//div[@class='cell']/h4/a")
        all_series = all_series[0:2] # limit rows when testing
        results = []
        for series in all_series:
            # get the data on this page
            series_data = {}
            series_data['series_title'] = series.xpath("./text()").extract()[0]
            series_data['series_link'] = series.xpath("./@href").extract()[0]

            # and from the page for this series (including subsequent pages)
            request = Request(series_data['series_link'], callback=self.parseSeries)
            request.meta['series_data'] = series_data # put this into the request so it is accessible later

            # save all the things we got from the next pages
            print(request)
            print(request.meta)
            results.append(request)

        # we did it :)
        return results
    
    def parseSeries(self, response):
        # grab the result info from the first request so we can keep using it
        series_data = response.meta['series_data']

        # parse each sermon from the page
        all_sermons = response.xpath("//div[@class='sermon-list-content']")
        results = []
        for sermon in all_sermons:
            # add the series info
            sermon_data = {}
            sermon_data['series_title'] = series_data['series_title']
            sermon_data['series_link'] = series_data['series_link']

            # get the data on this page
            sermon_data['title'] = sermon.xpath("./h3[@class='title']/a/text()").extract()[0]
            sermon_data['sermon_link'] = sermon.xpath("./h3[@class='title']/a/@href").extract()[0]
            sermon_data['date'] = sermon.xpath("./div[@class='sermon-list-date']/text()").extract()[0].strip()
            sermon_data['speaker'] = sermon.xpath("./a[@class='more']/text()").extract()[0].strip()
            results.append(sermon_data)
        
        # we did it :)
        return results
        



