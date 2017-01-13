from DataHandlerClass import *

dh = DataHandler('class_A.bin', '2-3')

#ex2
highest= dh.WhoIsTheHighest()
print(highest, "got the score of", dh.GetScoreByName(highest))


'''
#ex2
lowest = dh.WhoIsTheLowest()
print(lowest, "got the score of", dh.GetScoreByName(lowest))
'''

'''
#ex2
print(dh.rawdata)
'''

std_dev = dh.GetStandardDeviation()
print(std_dev)

avrg = dh.GetAverage()
print(avrg)


dh.GetEvaluation()
