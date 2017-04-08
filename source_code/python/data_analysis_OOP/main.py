from DataHandlerClass import *

dh = DataHandler('class_A.bin', '2-3')

dh.GetEvaluation()

print("the lowest score : ({} = {})".format(dh.WhoIsLowest(),\
                                            dh.GetLowestScore()))

print("the highest score : ({} = {})".format(dh.WhoIsHighest(),\
                                             dh.GetHighestScore()))
