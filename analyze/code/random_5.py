# randomly genterate a list of 10 numbers between 1 and ueser input number

import random

# get user input
user_input = int(input("請輸入一個數字："))

# randomly genterate a list of 5 numbers between 1 and ueser input number
random_list = random.sample(range(1, user_input+1), 5)
# sort list from small to big
random_list.sort()
print(random_list)