class GenericPipeline:
    """
    Useful Links:-

    A. Pipeline:
        1. https://docs.scrapy.org/en/latest/topics/item-pipeline.html

    B. Saving Data to DB:
        1. JSON - https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-a-json-lines-file
        2. MongoDB - https://docs.scrapy.org/en/latest/topics/item-pipeline.html#write-items-to-mongodb
        3. Postgres - https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-postgres
    """

    def process_item(self, item, spider):
        # Write the code to save the returned item to some db
        # START

        # END

        return item
