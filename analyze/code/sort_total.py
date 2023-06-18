import csv
import matplotlib.pyplot as plt
import numpy as np

# open file form the folder
file_input = ['analyze/csv/三國演義_cut_total.csv',
              'analyze/csv/西遊記_cut_total.csv',
              'analyze/csv/水滸傳_cut_total.csv',
              'analyze/csv/紅樓夢_cut_total.csv']
remove_text = ['三國演義_', '西遊記_', '水滸傳_', '紅樓夢_']
y = [[] for _ in range(4)]

for i in range (4):
    temp_list = []
    # open file
    with open(file_input[i], 'r', encoding='utf-8') as f:
        # read file
        reader = csv.reader(f)
        
        # turn csv file into a list
        x = 0
        for row in reader:
            if x==0:
                x+=1
                continue
            temp_list.append(row)

        # sort list base on file_name's number
        temp_list.sort(key=lambda x: int(x[0].strip(remove_text[i]).strip('.txt.csv')))

        for row in temp_list:
            y[i].append(round(float(row[3]),2))

# set x
x0 = np.arange(1, len(y[0])+1)
x1 = np.arange(1, len(y[1])+1)
x2 = np.arange(1, len(y[2])+1)
x3 = np.arange(1, len(y[3])+1)

# set font
plt.rcParams['font.sans-serif'] = ['mingliu']
plt.rcParams['axes.unicode_minus'] = False

# Initialise the subplot function using number of rows and columns
figure, axis = plt.subplots(2, 2)
  
# For 三國演義_多樣性變化
axis[0, 0].plot(x0, y[0])
axis[0, 0].set_title("三國演義_多樣性變化")
axis[0, 0].get_xaxis().set_visible(False)
axis[0, 0].set_ylim(90, 180)
  
# For 西遊記_多樣性變化
axis[0, 1].plot(x1, y[1])
axis[0, 1].set_title("西遊記_多樣性變化")
axis[0, 1].get_xaxis().set_visible(False)
axis[0, 1].set_ylim(90, 180)

# For 水滸傳_多樣性變化
axis[1, 0].plot(x2, y[2])
axis[1, 0].set_title("水滸傳_多樣性變化")
axis[1, 0].get_xaxis().set_visible(False) 
axis[1, 0].set_ylim(90, 180)

# For 紅樓夢_多樣性變化
axis[1, 1].plot(x3, y[3])
axis[1, 1].set_title("紅樓夢_多樣性變化")
axis[1, 1].get_xaxis().set_visible(False)
axis[1, 1].set_ylim(90, 180)

# Combine all the operations and display
plt.show()

# save picture
plt.savefig("analyze/total_diversity.png")


