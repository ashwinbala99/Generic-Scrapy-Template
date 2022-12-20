from scrapy import Request, Spider
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import (DNSLookupError, TCPTimedOutError,
                                    TimeoutError)

from ..items import GenericItem
from ..utils.extraction_helper import get_consolidated_data
from ..utils.header_helper import get_headers
from ..utils.info_helper import get_info_dict
from ..utils.input_helper import get_dummy_inputs


class SampleScrapySpider(Spider):
    name = 'book_spider'

    def start_requests(self):
        """
        Useful Links:-

        A. Python Best Practices:

            1. https://www.datacamp.com/blog/python-best-practices-for-better-code
            2. https://realpython.com/tutorials/best-practices/

        B. Scrapy Request Subclasses:

            1. https://docs.scrapy.org/en/latest/topics/request-response.html#request-objects
            2. https://docs.scrapy.org/en/latest/topics/request-response.html#formrequest-objects
            3. https://docs.scrapy.org/en/latest/topics/request-response.html#jsonrequest
        """

        items = get_dummy_inputs()
        print(f"Loaded {len(items)} inputs from DB")

        for item in items:
            current_url = item["url"]
            yield Request(
                url=current_url,
                method="GET",
                meta={
                    "id": item["id"],
                    "name": item["name"]
                },
                callback=self.parse,
                errback=self.error_handler,
                dont_filter=True,
                headers=get_headers(current_url),
            )

    def parse(self, response):
        """
        Useful Links:-

        A. Selectors:

            1. https://docs.scrapy.org/en/latest/topics/selectors.html
            2. https://docs.scrapy.org/en/latest/topics/items.html

        B. 
        """
        meta = response.request.meta
        print(f"Processing item {meta['id']}")

        data = get_consolidated_data(response)

        yield GenericItem(
            name=meta["name"],
            data=data,
            info=get_info_dict("success", meta),
        )

    def error_handler(self, failure):
        meta = failure.request.meta

        error, error_code = "Proxy Error", "No Proxies Available"

        if failure.check(HttpError):
            error, error_code = "HTTP Error", failure.value.response.status
        elif failure.check(DNSLookupError):
            error, error_code = "DNS Error", "DNSLookupError"
        elif failure.check(TimeoutError, TCPTimedOutError):
            error, error_code = "Timeout Error", "TimeoutError/TCPTimedOutError"
        else:
            error, error_code = "Proxy Error", "Proxy Timeout"

        print(f"Error: {error} occurred at {meta['id']}")

        yield GenericItem(
            name=error,
            data=None,
            info=get_info_dict(error_code, meta),
        )
