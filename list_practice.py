def count_positives_sum_negatives(arr):
    """
    Counts number of positive integers and sum of negative integers
    :param arr: list of integers
    :return: list of two integers (positive int count, sum of negative integers, respectively)
    """
    list_info = []
    positive_num_count = 0
    negative_num_sum = 0
    for num in arr:
        if num >= 0:
            positive_num_count += 1
        else:
            negative_num_sum += num
    list_info.append(positive_num_count)
    list_info.append(negative_num_sum)
    return list_info


num_list = []
user_numbers = input("Give me random numbers, positive and negative: ")
split_list = user_numbers.split(sep=", ")
print(split_list)

for num in split_list:
    num_list.append(int(num))
result = count_positives_sum_negatives(num_list)
print(result)