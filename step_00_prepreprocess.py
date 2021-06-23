# %%
import pandas as pd
import os
import re
from tqdm import tqdm

# %%
def read_patent(patent_path):
    with open(patent_path, "r") as patent_file:
        patent = patent_file.read().replace("\n", "").lower()
    return patent 

def split_patent(patent_path, fields=["claims", "title", "abstract", "filing_date", "priority_date", "docdb_family_id"]):
    patent = read_patent(patent_path)
    chunks = {}
    for part in fields:
        try:
            chunks[part] = re.search(f"(?<=<{part}>)(.*)(?=</{part}>)", patent).group(0)
        except:
            continue
        
    return chunks


# %%
patents_folders = [
    "../data/input/txt1", 
    "../data/input/txt2", 
    "../data/input/txt3"
    ]

fields = ["claims", "title", "abstract", "filing_date", "priority_date", "docdb_family_id"]

# %%
all_patents = []
for dir in patents_folders:
    all_patents += [dir + "/" + i for i in os.listdir(dir)]


# %%
split_patent(all_patents[0]).keys()

# %%
all_parsed_patents = list(filter(lambda x: len(x) == 6, [split_patent(i) for i in tqdm(all_patents)]))

# %%
future_claims_df = {"patent":[i["docdb_family_id"] for i in all_parsed_patents],"claim":[i["claims"] for i in all_parsed_patents]}
future_title_abstract_df = dict()
for i in [i for i in fields if i != "claims"]:
    future_title_abstract_df[i] = [j[i] for j in all_parsed_patents]

# %%
pd.DataFrame(future_title_abstract_df).to_csv("../data/input/title_abstract.csv")
pd.DataFrame(future_claims_df).to_csv("../data/input/claims.csv")

# %%
