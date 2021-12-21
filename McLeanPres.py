from scrapy.spiders import Spider

class McLeanPres(Spider):
    """
    Scrapes sermons from McLean Presbyterian Church, according to sermon series
    """

    # basic settings
    name = "s0" # name of the spider
    allowed_domains = ["mcleanpres.org"]
    start_urls = ["https://mcleanpres.org/sermons/series/all"]

    # don't abuse the website
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter'
    }

    def parse(self, response):
        all_series = response.xpath("//div[@class='cell']/h4/a")
        results = []
        print(len(all_series))
        for series in all_series:
            result = {}
            result['series_title'] = series.xpath("./text()").extract()
            result['series_link'] = series.xpath("./@href").extract()
            results.append(result)
        return result