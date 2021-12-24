# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: 'Python 3.8.8 64-bit (''base'': conda)'
#     language: python
#     name: python3
# ---

# %%
import requests
import pandas as pd
import elsapy

from elsapy.elsclient import ElsClient
from elsapy.elsprofile import ElsAuthor, ElsAffil
from elsapy.elsdoc import FullDoc, AbsDoc
from elsapy.elssearch import ElsSearch
import json
import os
import os.path as osp
import sys

from tqdm.auto import tqdm

# %%
with open("config.json") as con_file:
    config = json.load(con_file)

## Initialize client
client = ElsClient(config["apikey"])
pubyear = sys.argv[1]

# %%
extended_query = [
    "fuzzy logic",
    "logic programming",
    "declarative programming",
    "expert system",
    "inference engine",
    "knowledge base",
    "machine learning",
    "feature selection",
    "adaboost",
    "rankboost",
    "stochastic gradient descent",
    "supervised learning",
    "semi-supervised learning",
    "cluster analysis",
    "anomaly detection",
    "topic modeling",
    "dimensionality reduction",
    "manifold learning",
    "unsupervised learning",
    "xgboost",
    "random forest",
    "support vector machine",
    "artificial neural network",
    "deep neural network",
    "deep learning",
    "convolutional network",
    "recurrent neural network",
    "gated recurrent unit",
    "long short term memory",
    "maximum a posteriori model",
    "latent variable model",
    "bayes network",
    "conditional random field",
    "hidden markov rule",
    "instance based learning",
    "k nearest neighbor",
    "latent dirichlet allocation",
]

extended_query = ['"' + i + '"' for i in extended_query]

joint_query = " OR ".join(extended_query)

joint_query = f"TITLE-ABS-KEY({joint_query}) AND PUBYEAR = {pubyear}"

# %%
doc_srch = ElsSearch(joint_query, "scopus")
doc_srch.execute(client, get_all=True)


# %%
def get_scp_id(entry):
    return int(entry["dc:identifier"].split(":")[1])


urls = [x["prism:url"] for x in doc_srch.results]
for doc in tqdm(urls):
    abs_doc = AbsDoc(doc)
    if abs_doc.read(client):
        abs_doc.write()
