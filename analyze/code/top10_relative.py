# draw four line form 4 set of data
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print(matplotlib.matplotlib_fname())

# set font
plt.rcParams['font.sans-serif'] = ['mingliu']
plt.rcParams['axes.unicode_minus'] = False

# set data
x = np.arange(1, 11)
y1 = [3788,3906,4012,4173,4703,4897,5099,6725,7838,8735]
y2 = [5701,5753,5995,6484,7225,7499,7745,7971,8877,11080]
y3 = [5608,6013,6120,6320,8689,9347,10145,10306,10720,11744]
y4 = [9183,9695,10158,10550,11072,11458,12202,15075,15737,21246]

# set total number
y1_total = 485394
y2_total = 589290
y3_total = 748791
y4_total = 734066

# devided by total number
y1 = [(i/y1_total)*100 for i in y1]
y2 = [(i/y2_total)*100 for i in y2]
y3 = [(i/y3_total)*100 for i in y3]
y4 = [(i/y4_total)*100 for i in y4]

# set label
plt.ylabel("佔全書比例（單位：％）")

# set title
plt.title("四大小說出現次數最多的十個字（佔全書比例）")

# set x axis invisible
plt.gca().get_xaxis().set_visible(False)
# set y axiz range
plt.ylim(0, 4)

# draw line
plt.plot(x, y1, marker='o', label='三國演義')
plt.plot(x, y2, marker='o', label='西遊記')
plt.plot(x, y3, marker='o', label='水滸傳')
plt.plot(x, y4, marker='o', label='紅樓夢')

# draw legend
plt.legend()

# save picture
plt.savefig("analyze/top10_relative.png")

# show picture
plt.show()
