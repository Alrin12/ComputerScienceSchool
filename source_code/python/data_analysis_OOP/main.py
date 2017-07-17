from datahandler import *

dh = DataHandler('class_1.xlsx', '2-3')

dh.GetEvaluation()

print("the lowest score : ({} = {})".format(dh.WhoIsLowest(),\
                                            dh.GetLowestScore()))

print("the highest score : ({} = {})".format(dh.WhoIsHighest(),\
                                             dh.GetHighestScore()))
