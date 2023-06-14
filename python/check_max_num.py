random_num = list(range(1, 50000, 38))
# print (random_num)
while (True):
    for (check_num) in (random_num):
        if (str(check_num)) > (str(random_num)):
            print (check_num)
        else:
            if (str(check_num)) == (str(random_num)):
             print (check_num)
             break

