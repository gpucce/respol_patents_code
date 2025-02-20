# -*- coding: utf-8 -*-
"""
Created on Mon Aug 3 14:15:00 2020

@authors: Juan Carlos Gomez
          Sam Arts
          Jianan Hou

@emails: jc.gomez@ugto.mx
         sam.arts@kuleuven.be
         jianan.hou@kuleuven.be

@description: Indexs the patent nrams in the file ngrams_[n].txt using the
vocabulary in ngrams_[n]_vocabulary.txt. This is done to speed up the
comparison process in the following steps. The outputs is ngrams_[n]_idx.txt,
that contains the index of each ngram as in the vocabulary. n is the size of
the ngrams (2 or 3)

This code is part of the article: "Natural Language Processing to Identify the
Creation and Impact of New Technologies in Patent Text: Code, Data, and New
Measures"

"""

data_dir = '../data/output/' # Processed data
# n-gram size (2 or 3)
n = 3
# Input files from new_ngram measure
voc_file = data_dir+'new_ngram/ngrams_'+str(n)+'_vocabulary.txt'
ngram_file = data_dir+'new_ngram/ngrams_'+str(n)+'.txt'
# Output file for new_ngram measure
idx_file = data_dir+'new_ngram/ngrams_'+str(n)+'_idx.txt'

print('Reading vocabulary...')
voc = {}
i = 0
with open(voc_file, 'r', encoding='utf-8') as voc_reader:
    for line in voc_reader:
        tokens = line.strip().split()
        ngram = ' '.join([token for token in tokens[:n]])
        # Each ngram in the vocabulary is indexed sequentially
        voc[ngram] = i
        i += 1
print('Vocabulary read!')

print('Indexing and saving patents...')
i = 0
with open(ngram_file, 'r', encoding='utf-8') as uni_reader,\
        open(idx_file, 'w', encoding='utf-8') as idx_writer:
    for line in uni_reader:
        tokens = line.strip().split(',')
        pno = tokens[0]
        tokens = tokens[1:]
        patent_indexed = ''
        if tokens[0] != '':
            # Index the ngrams
            tokens = [voc[token] for token in tokens]
            tokens.sort()
            patent_indexed = ' '.join([str(token) for token in tokens])
        idx_writer.write(pno+','+patent_indexed+'\n')
        i += 1
        if i % 100000 == 0:
            print('\t '+str(i)+' patents indexed')
print('Patents indexed and saved!')
