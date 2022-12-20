# Scrapy settings for generic project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'generic'

SPIDER_MODULES = ['generic.spiders']
NEWSPIDER_MODULE = 'generic.spiders'

ROBOTSTXT_OBEY = False
LOG_ENABLED = True
LOG_FILE = "logfile.log"
LOG_LEVEL = 'INFO'

# Increase number of threads
REACTOR_THREADPOOL_MAXSIZE = 100

# Autothrottle settings
DOWNLOAD_DELAY = 0.5
CONCURRENT_REQUESTS = 32

# You can create and use your own middlewares and add them to the below list
DOWNLOADER_MIDDLEWARES = {
    'generic.middlewares.SetCommonHeadersMiddleware': 543,
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# Proxy handling using scrapy-rotating-proxies
ROTATING_PROXY_LIST = [
    # Add your proxies to this list
]
ROTATING_PROXY_PAGE_RETRY_TIMES = 2

# You can create and use your own pipelines and add them to the below list
ITEM_PIPELINES = {
    'generic.pipelines.GenericPipeline': 300,
}

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
