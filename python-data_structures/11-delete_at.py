#!/usr/bin/python3
def delete_at(my_list=[], idx=0):

    if idx < 0 or idx >= len(my_list):
        return my_list
    
    temp_list = []

    for num in my_list:
        if num != idx:
            temp_list.append(num)
    return temp_list
