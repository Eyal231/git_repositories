def get_max_num(list_numbers):
    max_num = list_numbers[0]
    sec_max_num = list_numbers[-1]
    for some_num in list_numbers:
        if some_num > max_num:
            sec_max_num = max_num
            max_num = some_num
    return(sec_max_num)

l1 = [4, 8, 5, 6, 15, 258, 5878]

secend = get_max_num(l1)
print(secend)
