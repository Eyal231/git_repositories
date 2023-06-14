num_list = list(range(10, 15 , 1)) 
for x in num_list:
        if (x%17) == 0:
         print( x )
         break
else:
   print("no num dividable by 17")
