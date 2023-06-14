boom = list(range(101))
newlist = []

for x in boom:
  if "7" in str(x):
    newlist.append("boom")
  else:
    if x in boom:
     newlist.append(x)
    # print(newlist)


print(newlist)