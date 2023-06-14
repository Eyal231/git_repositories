boom=list(range(101))
for seven in boom[:]:
      if '7' in str(seven):
        print((str(seven)).replace(str(seven), "boom"))
      else:
        print(seven)
