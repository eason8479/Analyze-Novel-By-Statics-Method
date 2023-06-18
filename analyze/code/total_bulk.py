import os
import csv

# open file form the folder
file_input_folder = 'analyze/csv/西遊記'
file_output = 'analyze/csv/西遊記_cut_total.csv'

# get all the file name in the folder
file_list = os.listdir(file_input_folder)

total = {}

# for each file in the folder 
for file_name in file_list:
    # open file and count it
    with open(os.path.join(file_input_folder, file_name), 'r', encoding='utf-8') as f:
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

        # save the result into total
        total[file_name] = [sum, length, (length/sum)*1000]
        
        
# save total into csv file
with open(file_output, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['file_name', 'sum', 'length', 'diversity'])
    for i in total:
        writer.writerow([i, total[i][0], total[i][1], total[i][2]])

print('done')
