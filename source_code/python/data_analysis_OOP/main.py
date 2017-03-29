from DataHandlerClass import *

dh = DataHandler('class_A.bin', '2-3')

dh.GetEvaluation()

print("the lowest score : ({} = {})".format(dh.WhoIsTheLowest(),\
                                            dh.rawdata[dh.WhoIsTheLowest()]))

print("the highest score : ({} = {})".format(dh.WhoIsTheHighest(),\
                                             dh.rawdata[dh.WhoIsTheHighest()]))
