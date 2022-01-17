#! /bin/bash

mkdir -p ../data/output/new_ngram/

python new_ngram/step_02_clean_concatenated_patents_extract_n_gram.py
python new_ngram/step_03_index_patents.py
python new_ngram/step_04_extract_baseline_vocabulary.py
python new_ngram/step_05_new_ngram.py