start_vaule = 50

with open(r"/workspaces/Advent_of_code/2025/Day_one_2025_files/Day_one_2025_input_file.txt", "r") as file:
    List_input_file = [str(line.strip()) for line in file]
    num_lines = len(List_input_file)
    print(List_input_file)
    print(num_lines)
List_input_file_change = List_input_file 
'''
while num_lines > 0 :
    List_input_file_change
'''

# only working for R
'''
if 0 <= next_rotation < 100 :
    Current_rotation + next rotation 

    if 0 <= current_rotation < 100 :    
        pass 
    elif current_rotation < 0 
        pass
    else :
        current_rotation = current_rotation - 100 


'''

import re

input = ["L68" ,"L30" ,"R48" ,"L5" ,"R60" ,"L55" ,"L1" ,"L99" ,"R14" ,"L82" ]
input_change = input 
while len(input_change) > 0 :  
  next_rotation = input.pop(0)
  print next_rotation
  current_rotation = re.split ("RL",next_rotation)
  print current_rotation
