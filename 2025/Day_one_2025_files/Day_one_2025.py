start_vaule = 50

with open(r"/workspaces/Advent_of_code/2025/Day_one_2025_files/Day_one_2025_input_file.txt", "r") as file:
    List_input_file = [str(line.strip()) for line in file]
    num_lines = len(List_input_file)
 #   print(List_input_file)
  #  print(num_lines)
List_input_file_change = List_input_file 

input_test = ["L68" ,"L30" ,"R48" ,"L5" ,"R60" ,"L55" ,"L1" ,"L99" ,"R14" ,"L82" ]

List_input_file_change = input_test

List_input_file_change = []
List_input_file_change = input_test
num_lines_change = num_lines
current_value = start_vaule
while num_lines_change > 0 :
    Next_rotation = []
    Next_rotation = List_input_file_change.pop(0) # removes one item in the list at a time 
    num_lines_change = len(List_input_file_change)
    pos_neg = Next_rotation[0]
    if pos_neg == "R" :                           # removes the letter to leave the number 
        number_rotation = Next_rotation.lstrip("R")
        number_rotation = int(number_rotation)
        current_value = int(current_value)
        current_value = current_value + number_rotation
        if current_value > 99 :
            current_value = 100 - current_value
            print(current_value)
        else:
            print(current_value)

    else:
        number_rotation = Next_rotation.lstrip("L")
        number_rotation = int(number_rotation)
        current_value = int(current_value)
        current_value = current_value + number_rotation
        if current_value < 0 :
            current_value = current_value - 100 
            print(current_value)
        else:
            print(current_value)
'''
        number_rotation = Next_rotation.lstrip("L")
        print(int(number_rotation))
        int(number_rotation)
        start_vaule = number_rotation + start_vaule
        print (start_vaule)
        if start_vaule > 0 :
            start_vaule = 99 + start_vaule
        else:
            start_vaule = start_vaule
        print (start_vaule)
'''