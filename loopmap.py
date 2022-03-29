"""
    ** fuctions for looping based on number of counts
"""
import math


def loop_one(arr,new_arr):
    for el in range(len(arr)):
        new_arr.append(arr[el])
   

def loop_two(arr,new_arr):
    for el2 in range(len(arr[0])):
        new_arr.append([arr[0][el2],arr[1][el2]])
  
def loop_three(arr,new_arr):
    for el2 in range(len(arr[0])):
        new_arr.append([arr[0][el2],arr[1][el2],arr[2][el2]])

def loop_four(arr,new_arr):
    for el2 in range(len(arr[0])):
        new_arr.append([arr[0][el2],arr[1][el2],arr[2][el2],arr[3][el2]])

# helper function
def n_separator(num,sep):
    arr=[]
    separator = sep if sep != None else len(num)
    sep_length = len(num)/separator
    prev,next = 0,separator
    
    for el in range(math.ceil(sep_length)):
        arr.append(num[prev:next])
        prev+=separator
        next +=separator 
    return("-".join(arr))
