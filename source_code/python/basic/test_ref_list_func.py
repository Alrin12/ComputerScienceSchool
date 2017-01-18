def func(a):
   print("a : " + str(id(a)) + " before trying change in func")
   a[1] = 7
   print("a : " + str(id(a)) + " after trying change in func")
   a = [11, 12 ,13]
   print("a : " + str(id(a)) + " after allocating in func")

li = [1, 2, 3]
print("li : " + str(id(li)) + " before functiuon")
func(li)
print("li : " + str(id(li)) + " after function")
