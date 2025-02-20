# %%
import pandas as pd
import os
import os.path as osp
import re
import numpy as np
from pandas._libs.missing import NA
from tqdm.auto import tqdm

# %%
def read_patent(patent_path):
    with open(patent_path, "r") as patent_file:
        patent = patent_file.read().replace("\n", "").lower()
    return patent 

def split_patent(patent_path, id=1, fields=["claims", "title", "abstract", "filing_date", "priority_date", "docdb_family_id"]):
    patent = read_patent(patent_path)
    patent_name = osp.splitext(osp.basename(patent_path))[0]
    chunks = {"local_id":id, "global_id":patent_name}
    for part in fields:
        try:
            chunks[part] = re.search(f"(?<=<{part}>)(.*)(?=</{part}>)", patent).group(0)
        except:
            chunks[part] = np.nan
        
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
progressbar = tqdm(range(len(all_patents)))
all_parsed_patents = []
for idx, i in enumerate(all_patents):
    all_parsed_patents.append(split_patent(i, idx))
    progressbar.update(1)

# %%
future_claims_df = {
    "patent":[i["global_id"] for i in all_parsed_patents],
    "claim":[i["claims"] for i in all_parsed_patents],
    "docdb_family_id":[i["docdb_family_id"] for i in all_parsed_patents]
    }

future_local_global_id = {
    "local_id":[i["local_id"] for i in all_parsed_patents],
    "patent":[i["global_id"] for i in all_parsed_patents]
    }

future_title_abstract_df = dict()
for i in [i for i in fields if i != "claims"] + ["global_id"]:
    if i == "global_id":
        future_title_abstract_df["patent"] = [j[i] for j in all_parsed_patents]
        continue    
    future_title_abstract_df[i] = [j[i] for j in all_parsed_patents]    

# %%
pd.DataFrame(future_title_abstract_df).to_csv("../data/input/title_abstract.csv", sep="\t", index=False)
pd.DataFrame(future_claims_df).to_csv("../data/input/claims.csv", sep="\t", index=False)
pd.DataFrame(future_claims_df).to_csv("../data/input/patent_ids.csv", sep="\t", index=False)

# %%
