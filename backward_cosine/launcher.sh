#! /bin/bash

mkdir -p ../data/output/backward_cosine/
mkdir -p ../data/output/backward_cosine/files

python backward_cosine/step_02_clean_concatenated_patents.py
python backward_cosine/step_03_index_patents.py
python backward_cosine/step_04_cosine_similarity_five_years.py
python backward_cosine/step_05_join_cosine_similarity_files.py