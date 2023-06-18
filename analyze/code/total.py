import csv
# open .csv file
file_name = "analyze\三國演義_clean4_word.csv"
with open(file_name, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    # turn csv file into a list
    list = []
    for i in reader:
        list.append(i)
    # count the lengthe of the list
    length = len(list)
    # count the sum of second coulumn
    sum = 0

    for i in list:
        if (i[1] != ''):
            sum += int(i[1])

    # return sum and length
    print(f"字數 = {sum}")
    print(f"字種類數 = {length}")
    print(f"多樣性 = {(length/sum)*1000}")

