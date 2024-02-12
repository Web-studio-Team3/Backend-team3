items_mapping = {
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "text", "analyzer": "autocomplete" },
        "description": {"type": "text"},
        "condition": {"type": "text"},
        "address": {"type": "text"},
        "cost": {"type": "text"},
        "status": {"type": "text"},
    }
}

items_settings = {
    "analysis": {
        # "filter": {
        #     "autocomplete_filter": {
        #         "type": "ngram",
        #         "min_gram": 1,
        #         "max_gram": 3
        #     }
        # },
        "analyzer": {
            "autocomplete": { 
                "type": "custom",
                "tokenizer": "autocomplete_tokenizer",
                "filter": [
                    "lowercase",
                    # "autocomplete_filter"
                ]
            }
        },
        "tokenizer": {
            "autocomplete_tokenizer": {
                "type": "ngram",
                "min_gram": 1,
                "max_gram": 3
            }
        }
    },
    "index.max_ngram_diff": "3"
}
