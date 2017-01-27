from DataHandlerClass import *

dh = DataHandler('class_A.bin', '2-3')

dh.GetEvaluation()

print(dh.WhoIsTheLowest())
print(dh.rawdata[dh.WhoIsTheLowest()])
print(dh.WhoIsTheHighest())
