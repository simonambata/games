# Python Compiler Online
# https://www.programiz.com/python-programming/online-compiler/

import random

index = 16 # number of total pokemon in your box storage
count = 2  # number of fainted pokemon in your party

selected_index = random.sample(range(1, index + 1), count)
print(selected_index)

# selected_index is the position of your pokemon in the storage box which you will withdraw

# note that there is also a mobile app that you can use similarly
