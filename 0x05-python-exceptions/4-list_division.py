#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divide element by element in two lists.

    Args
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    result = 0

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            print("result: {}".format(result))
        except TypeError:
            print("wrong type")
            result = 0

        except ZeroDivisionError:
            print("division by 0")
            result = 0

        except IndexError:
            print("out of range")
            result = 0

        finally:
            new_list.append(result)

    return new_list
