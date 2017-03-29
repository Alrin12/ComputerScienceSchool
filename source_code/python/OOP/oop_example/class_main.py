from class_retailer import Retailer
from class_buyer import Buyer

p1 = Retailer("greg", 35, 10000, 100)
p2 = Buyer("taehwan", 21, 10000, 0)

print(p1)
print(p2)

#p1.transaction(p2, 3)
p2.transaction(p1, 3)

print(p1)
print(p2)
