def cumulative_sum(input_list):
    cum_sum = 0
    result = []
    for num in input_list:
        cum_sum += num
        result.append(cum_sum)
    return result

input_list = [1, 2, 3, 4, 5]
result = cumulative_sum(input_list)
print(result)
