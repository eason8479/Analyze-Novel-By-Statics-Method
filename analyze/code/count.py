# turn string of word with no space into a list of word
def word_to_list(string):
    # remove \n
    string = string.replace('\n', '')
    # add space into a string of word with no space
    new_string = ''
    for i in string:
        new_string += i + ' '

    # turn string of word with space into a list of word
    list = []
    for i in string:
        if i != (' ' or ''):
            list.append(i)
    return list

# count the frequecy of each element in a list
def count_list(list):
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

# combine function word_to_list and count_list
def count_word(string):
    return count_list(word_to_list(string))



