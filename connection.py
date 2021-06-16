import os
from elasticsearch import Elasticsearch

client = Elasticsearch(
        cloud_id=os.environ.get("CLOUD_ID"),
        http_auth=(
            os.environ.get("ES_USERNAME", 'elastic'),
            os.environ.get("ES_PASSWORD"),
            ),
        )
