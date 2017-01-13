import pickle
import math

class Evaluate:
    def average(self, scores):
        sum = 0
        for score in scores:
            sum += score
        return sum/len(scores)

    def variance(self, scores, avrg):
        variance_sum = 0
        for score in scores:
            a = score - avrg
            variance_sum += (a**2)
        return variance_sum/len(scores)

    def evaluateClass(self, avrg, std_dev):
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

    

