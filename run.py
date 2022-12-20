from scrapy.cmdline import execute

if __name__ == "__main__":
    spider_name = 'book_spider'
    outfile_name = 'sample.json'

    if outfile_name is None:
        execute(f'scrapy crawl {spider_name}')
    else:
        execute(f'scrapy crawl {spider_name} -O {outfile_name}'.split())
