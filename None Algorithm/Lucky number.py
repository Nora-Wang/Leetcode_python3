def find_first_non_lucky_index(lucky_set, large_str):
    for i in range(len(large_str)):
        if int(large_str[i]) not in lucky_set:
            return i
    return -1

def create_res(large_str, change, index, max_lucky):
    res = []
    res.append(large_str[:index])
    res.append(change)
    for _ in range(index + 1, len(large_str)):
        res.append(str(max_lucky))

    return int(''.join(res))
    
def find_cloest_smaller_number(nums, target):
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid
    
    return nums[end] if nums[end] < target else nums[start]

def deal_with_lucky_number(large_str, index, min_lucky, sorted_luck_nums, max_lucky):
    # find first lucky number which is larger than min_lucky
    while index >= 0 and int(large_str[index]) == min_lucky:
        index -= 1
    
    if index >= 0:
        number = find_cloest_smaller_number(sorted_luck_nums, int(large_str[index]))
        return create_res(large_str, str(number), index, max_lucky)
    # if cannot find -> curt large is the smallest numer that lukcy_num could create (all are min_lucky)
    else:
        return -1

def lucky_number(large_int, lucky_nums):
    large_str = str(large_int)
    lucky_set = set(lucky_nums)
    sorted_luck_nums = sorted(lucky_nums)
    max_lucky = max(lucky_nums)
    min_lucky = min(lucky_nums)

    index = find_first_non_lucky_index(lucky_set, large_str)
    
    # all num in lucky_nums
    if index == -1:
        return deal_with_lucky_number(large_str, len(large_str) - 1, min_lucky, sorted_luck_nums, max_lucky)
        
    # exist non lucky number
    else:
        # could find smaller lucky number
        if int(large_str[index]) > min_lucky:
            number = find_cloest_smaller_number(sorted_luck_nums, int(large_str[index]))
            return create_res(large_str, str(number), index, max_lucky)
        else:
            return deal_with_lucky_number(large_str, index - 1, min_lucky, sorted_luck_nums, max_lucky)
            



print(lucky_number(444, [1,3]))
print(lucky_number(444, [1,3,8,9]))
print(lucky_number(377, [3,6,9]))
print(lucky_number(6603, [3,6,9]))
print(lucky_number(6303, [3,6,9]))

