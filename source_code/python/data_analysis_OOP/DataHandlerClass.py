from EvaluateClass import *
import pickle

class DataHandler:
    #클래스 변수 : 클래스의 모든 인스턴스들이 공유하는 변수
    evaluator = Evaluate()

    #class method : 전역함수처럼 쓸 수 있다              
    @classmethod
    def GetRawdataInDic(cls, filename):
        items = []
        with open(filename, 'rb') as f:
            while 1:
                try: 
                    data = pickle.load(f)
                except EOFError:
                    break    
                items.append(data)
        
        rawdata={}
        for item in items:
            for i in item.items():
                rawdata.update({i[0] : i[1]})
        return rawdata


    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.GetRawdataInDic(filename)
        self.clsname = clsname
        
        self.cache = {} #이미 계산된 데이터를 저장할 저장공간
        
    def GetScores(self):
        if "scores" not in self.cache:
            scores = reduce(lambda r, e : r.append(e) or r, self.rawdata.values(), [])
            self.cache["scores"] = scores

        return self.cache.get("scores")

    def GetAverage(self):
        if "average" not in self.cache:
            avrg = round(self.evaluator.average(self.GetScores()), 1)
            self.cache["average"] = avrg

        return self.cache.get("average")

    def GetVariance(self):
        if "variance" not in self.cache:
            vari = round(self.evaluator.variance(self.GetScores(), self.GetAverage()), 1)
            self.cache["variance"] = vari
  
        return self.cache.get("variance")

    def GetStandardDeviation(self):
        if "standard_deviation" not in self.cache:
            std_dev = round(math.sqrt(self.GetVariance()), 1)
            self.cache["standard_deviation"] = std_dev

        return self.cache.get("standard_deviation")

    def GetScoreByName(self, name):
        return self.rawdata[name]
    
    def WhoIsHighest(self):
        if "highest" not in self.cache:
            high = reduce(lambda a, b: a if self.rawdata.get(a, 0) > self.rawdata.get(b)\
                             else b, self.rawdata.keys(), 'who')
            self.cache["highest"] = high
            
        return self.cache.get("highest")

    def GetHighestScore(self):
        return self.rawdata[self.WhoIsHighest()]
    
    def WhoIsLowest(self):
        if "lowest" not in self.cache:
            low = reduce(lambda a, b: a if self.rawdata.get(a, 101) < self.rawdata.get(b) \
                     else b, self.rawdata.keys(), 'who')
            self.cache["lowest"] = low
            
        return self.cache.get("lowest")

    def GetLowestScore(self):
        return self.rawdata[self.WhoIsLowest()]    

    def GetEvaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".\
              format(self.clsname, self.GetAverage(), self.GetVariance()\
                     , self.GetStandardDeviation()))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass()

    def evaluateClass(self):
        avrg = self.GetAverage()
        std_dev = self.GetStandardDeviation()
        
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")

            
