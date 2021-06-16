import eland as ed
import pandas as pd
from elasticsearch import Elasticsearch
from connection import client

def set_location(x):
    location = ",".join(x.values.astype(str))
    return location

df = pd.read_csv(
        "fatal-police-shootings-data.csv",
        parse_dates=True,
        )

def upload():
    ed.pandas_to_eland(
            df,
            es_client=client,
            es_dest_index="wapo-police-shootings-data",
            es_dropna=True,
            es_if_exists="replace",
            )
