import evaluate

scores = [10, 15, 12, 13, 12]
avrg = evaluate.average(scores)
var = evaluate.variance(scores)

print(avrg, var)
