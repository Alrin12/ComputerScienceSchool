
s1 = "abcde fghij abcde xyz"
#upper()
print(s1.upper())

#lower()
s2 = "Abcde Fghij"
print(s2.lower())

print("abc" in s1)


#capitalize()
s3 = "my name is neo"
print(s3.capitalize())

#title()
print(s3.title())


#split()
li1 = s1.split()
print(li1)

#find()
print(s1.find("abc", 5))
#없으면 -1 반환 
print(s1.find("i am"))

#rfind()
print(s1.rfind("abc"))

#startswith()
print(s1.startswith("abcde"))

#endswith()
print(s1.endswith("xyz"))

#count()
print(s1.count("abcde"))

#index()
print(s1.index('abc', 4))

#없으면 예외 발생
#print(s1.index("i am"))


#replace()
print(s1.replace("abcde", "......."))


