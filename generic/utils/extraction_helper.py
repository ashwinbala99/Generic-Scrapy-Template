def get_consolidated_data(selector):
    title = selector.xpath('//div[contains(@class, "product_main")]/h1/text()').get()
    description = selector.xpath('//div[@id="content_inner"]/article/p/text()').get()

    stars = selector.css('div.product_main p.star-rating::attr(class)').get()
    stars = stars.split(' ')[-1]

    info_keys = selector.css('table.table-striped.table tr th::text').getall()
    info_values = selector.css('table.table-striped.table tr td::text').getall()

    return {
        "title": title,
        "description": description,
        "stars": stars,
        "more_info": {
            value[0]: value[1] for value in list(zip(info_keys, info_values))
        },
    }
