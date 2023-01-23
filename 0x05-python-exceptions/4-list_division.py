#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for idx in range(list_length):
        div = 0
        try:
            div = my_list_1[idx] / my_list_2[idx]
            new_list[idx] = div
        except IndexError:
            print("Out of Range")
        except TypeError:
            print("Wrong Type")
        except ZeroDivisionError:
            print("Dvision by 0")
        new_list[idx] = div
        
