#! /bin/bash

python new_word/step_02_clean_concatenated_patents.py
python new_word/step_03_index_patents.py
python new_word/step_04_extract_baseline_vocabulary.py
python new_word/step_05_new_word.py