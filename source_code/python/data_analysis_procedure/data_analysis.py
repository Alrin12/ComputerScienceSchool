import openpyxl
import math
from functools import reduce

def get_data_from_excel(filename):
    dic = {}
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    for a, b in ws['A1' : 'B10']:
        dic[a.value] = b.value
    return dic

def average(scores):
    return reduce(lambda a, b: a + b, scores)/len(scores)

def variance(scores, avrg):
    return round(reduce(
        lambda a, b: a + b,
        map(lambda s:(s-avrg)**2, scores))/len(scores), 1)

def std_dev(variance):
    return round(math.sqrt(variance), 1)

def evaluateClass(avrg, std_dev):
    if avrg <50 and std_dev >20:
        print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
    elif avrg > 50 and std_dev >20:
        print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
    elif avrg < 50 and std_dev <20:
        print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
    elif avrg > 50 and std_dev <20:
        print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

if __name__ == "__main__":
    raw_data = get_data_from_excel('class_1.xlsx')
    scores = list(raw_data.values())
    
    avrg = average(scores)
    variance = variance(scores, avrg)
    standard_deviation = std_dev(variance)

    print("A반의 평균은 {0}점이고 분산은 {1}이며, 따라서 표준편차는 {2}이다"\
          .format(avrg, variance, standard_deviation))
    evaluateClass(avrg, standard_deviation)

