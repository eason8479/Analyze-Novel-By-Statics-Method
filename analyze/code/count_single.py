from count import count_word

file_in = "analyze\\text\\三國演義_clean4.txt"
file_out = "analyze\\csv\\三國演義_clean4_word.csv"


# open file and count it
with open(file_in, 'r', encoding='utf-8') as f:
    string = f.read()
    count_word_result = count_word(string)
    # save the result into test.csv
    with open(file_out, 'w', encoding='utf-8') as f:
        for i in count_word_result:
            f.write(i + ',' + str(count_word_result[i]) + '\n')
