# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 10:30:42 2024

@author: Dharun Venkat
"""

import random

# I think the only way of doing this is by swapping the list elements; there's no way of doing it by checking
# whether the number is less than all the other numbers then adding it to the list
# maybe if it's bigger you slap it on at the back?



list_length = int(input('How long do you want the list to be? '))
the_list = []
the_list2 = []


for i in range(0, list_length):
    
    r = random.randint(0, 100)
    
    the_list.append(r)
    

print(f'The unsorted list of numbers is {the_list}')
                   

for j in range (0, len(the_list)):
    
    x = min(the_list)
    
    the_list2.append(x)
    
    the_list.remove(x)

        
print(f'The sorted list of numbers the is {the_list2}')
                
    
    


    
    

