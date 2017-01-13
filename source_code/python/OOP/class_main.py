from class_person import Person
from class_retailer import Retailer
from class_buyer import Buyer

p1 = Retailer("greg", 35, 10000, 100)
p2 = Buyer("taehwan", 21, 10000, 0)

p1.showMyInfo()
print('\n')
p2.showMyInfo()

#p1.Sell(p2, 3)
p2.Buy(p1, 3)
print('\n')

p1.showMyInfo()
print('\n')
p2.showMyInfo()
