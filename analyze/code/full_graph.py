import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import csv

print(matplotlib.matplotlib_fname())

# set font
plt.rcParams['font.sans-serif'] = ['mingliu']
plt.rcParams['axes.unicode_minus'] = False


# set y
y = [[] for _ in range(4)]


file = ['analyze\\csv\\三國演義_clean4_word.csv',
        'analyze\\csv\\西遊記_clean_word.csv',
        'analyze\\csv\\水滸傳_clean_word.csv',
        'analyze\\csv\\紅樓夢_clean_word.csv']

# read in data
for i in range(4):
    with open(file[i], 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if (row[0] == ''):
                continue
            y[i].append(float(row[1]))




# sort y form low to high
y[0].sort()
y[1].sort()
y[2].sort()
y[3].sort()


# set x    
x1 = np.arange(1, len(y[0])+1)
x2 = np.arange(1, len(y[1])+1)
x3 = np.arange(1, len(y[2])+1)
x4 = np.arange(1, len(y[3])+1)

# set label
plt.ylabel("出現次數")

# set title
plt.title("全文詞頻分析")

# set x axis invisible
plt.gca().get_xaxis().set_visible(False)

# draw line
plt.plot(x1, y[0], label='三國演義')
plt.plot(x2, y[1], label='西遊記')
plt.plot(x3, y[2], label='水滸傳')
plt.plot(x4, y[3], label='紅樓夢')

# draw legend
plt.legend()

# save picture
plt.savefig("analyze//全文詞頻分析.png")

# show picture
plt.show()
