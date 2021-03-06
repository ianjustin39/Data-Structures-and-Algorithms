def binary_search_recursive(array, target):
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    mid_index = (start_index + end_index) // 2  # integer division in Python 3

    mid_element = array[mid_index]

    if target == mid_element:  # we have found the element
        return mid_index

    elif target < mid_element:  # the target is less than mid element
        end_index = mid_index - 1  # we will only search in the left half
        binary_search_recursive_soln(array[:mid_index], target, start_index, end_index)
    else:  # the target is greater than mid element
        start_index = mid_element + 1  # we will search only in the right half
        binary_search_recursive_soln(array[mid_index:], target, start_index, end_index)
    return -1


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
