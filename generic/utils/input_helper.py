def get_dummy_inputs():
    # Most likely the data will be obtained from some DB or redis queue
    return [
        {
            "id": "1",
            "name": "Book 1",
            "url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html",
        },
        {
            "id": "2",
            "name": "Book 2",
            "url": "https://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html",
        },
        {
            "id": "3",
            "name": "Book 3",
            "url": "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html",
        },
        {
            "id": "4",
            "name": "Book 4",
            "url": "https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html",
        },
        {
            "id": "5",
            "name": "Book 5",
            "url": "https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html",
        },
    ]
