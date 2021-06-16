import os
import eland as ed
import pandas as pd
from elasticsearch import Elasticsearch

df = pd.read_csv("fatal-police-shootings-data.csv")
ed.pandas_to_eland(df, es_index="wapo-police-shootings-data", if_es_exists="replace")
