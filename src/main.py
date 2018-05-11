# -*- coding: utf-8 -*-

import os
import logging

logging.basicConfig(filename='../data/logs/logs.log', filemode='w', level=logging.INFO)

directory_input = '../data/input/'
directory_output = '../data/output/'
prefix = 'Billboard_authors_'
suffix = '.txt'
split_criteria = '|'
subfile_limit = 50

for file in os.listdir(directory_input):
    filename = os.fsdecode(file)
    if filename.startswith(prefix) or filename.endswith(suffix):
        clean_filename = filename.replace(suffix, '')

        file = open(directory_input + filename, 'r', encoding='utf-8')
        content = file.readline()
        file.close()
        content_list = content.split(split_criteria)
        content = None
        subfiles_counter = 0
        elements_list = ''

        logging.info('{} starts'.format(clean_filename))
        for i in range(len(content_list)):
            element = content_list[i]
            elements_list += element + split_criteria
            if i % subfile_limit == 0 and i > 0:
                subfile_opened = open(directory_output + clean_filename + '_{}.txt'.format(subfiles_counter), "wb")
                subfile_opened.write(elements_list.rstrip('\n').encode())
                subfile_opened.close()
                elements_list = ''
                subfiles_counter += 1
                logging.info('- Subfile number {} created with {} elements'.format(subfiles_counter, subfile_limit))

        subfile_opened = open(clean_filename + '_{}.txt'.format(subfiles_counter), "wb")
        subfile_opened.write(elements_list.rstrip('\n').encode())
        logging.info('- Subfile number {} created. {} ends'.format(subfiles_counter, clean_filename))
    else:
        continue