#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """A function that divides 2 lists by element

        Args
        my_list_1: first list
        my_list_2: second list
        list_length: size of returning list

        return: a new list derived from divided elements
    """
    div_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            div = 0
            print("wrong type")
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except IndexError:
            div = 0
            print("out of range")
        finally:
            div_list.append(div)
    return div_list
