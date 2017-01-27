import evaluate
import math

class Evaluate:
    def average(self, scores):
        return evaluate.average(scores)

    def variance(self, scores):
        return evaluate.variance(scores)
        

    def evaluateClass(self, avrg, std_dev):
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

    
if __name__ == "__main__":
    scores = [100, 90, 85, 88]
    avrg = evaluate.average(scores)
    var = evaluate.variance(scores)
    std_dev = round(math.sqrt(var), 1)
    print("average : ", avrg)
    print("variance : ", var)
    print("standard deviation : ", std_dev)
    
