#! /bin/bash

mkdir -p ../data/output/new_comb/

python new_comb/step_02_clean_concatenated_patents.py
python new_comb/step_03_index_patents.py
python new_comb/step_04_extract_baseline_vocabulary_of_comb.py
python new_comb/step_05_new_word_comb.py