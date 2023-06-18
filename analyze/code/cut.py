# read a text file line by line
# when word count is more than 10000, cut it and save it to a new file

import os
import re
import sys

# read a text file line by line
file_input = 'analyze/text/西遊記_clean.txt'
file_output_folder = 'analyze/text/西遊記_cut'

temp = ''
word_count = 0
part_num = 1

with open(file_input, 'r', encoding='utf-8') as f:
    while True:
        lines = f.readline()
        # if line is empty, break
        if not lines:
            break
        
        lines = lines.strip()
        # if after strip, line is empty, continue
        if not lines:
            continue

        # if line is not empty, add it to temp    
        temp += lines
        word_count += len(lines)

        # if word count is more than 10000, cut it and save it to a new file
        if word_count > 10000:
            # save it to a new file
            output_file = os.path.join(file_output_folder, '西遊記_' + str(part_num) + '.txt')
            with open(output_file, 'w', encoding='utf-8') as f2:
                f2.write(temp)
            # reset temp and word_count
            temp = ''
            word_count = 0
            print('part ' + str(part_num) + ' done')
            part_num += 1
            # continue to read the rest of the file
            continue
