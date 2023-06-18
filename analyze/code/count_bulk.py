from count import count_word
import os

# open file form the folder
file_input_folder = 'analyze/text/三國演義_cut'
file_output_folder = 'analyze/csv/三國演義'

# get all the file name in the folder
file_list = os.listdir(file_input_folder)

# for each file in the folder 
for file_name in file_list:
    # open file and count it
    with open(os.path.join(file_input_folder, file_name), 'r', encoding='utf-8') as f:
        string = f.read()
        count_word_result = count_word(string)
        # save the result into test.csv
        with open(os.path.join(file_output_folder, file_name + '.csv'), 'w', encoding='utf-8') as f:
            for i in count_word_result:
                f.write(i + ',' + str(count_word_result[i]) + '\n')
    print(file_name + ' done')
