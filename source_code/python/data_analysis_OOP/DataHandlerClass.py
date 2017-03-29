from EvaluateClass import *
import pickle

class DataHandler:
    #클래스 변수 : 클래스의 모든 인스턴스들이 공유하는 변수
    evaluator = Evaluate()
    
    #static method : 전역함수처럼 쓸 수 있다
    @staticmethod
    def GetItemsFromFile(filename):
        items = []
        with open(filename, 'rb') as f:
            while 1:
                try: 
                    data = pickle.load(f)
                except EOFError:
                    break    
                items.append(data)
        return items
        
    @staticmethod
    def GetRawdataInDic(items):
        rawdata={}
        for item in items:
            for i in item.items():
                rawdata.update({i[0] : i[1]})
        return rawdata

    @staticmethod
    def GetScores(rawdata):   
        return reduce(lambda r, e : r.append(e) or r, rawdata.values(), [])
    
    @staticmethod
    def GetTheHighest(rawdata):
        return reduce(lambda a, b: a if rawdata.get(a, 0) > rawdata.get(b) else b\
                      , rawdata.keys(), 'who')

    @staticmethod
    def GetTheLowest(rawdata):
        return reduce(lambda a, b: a if rawdata.get(a, 101) < rawdata.get(b) else b\
                      , rawdata.keys(), 'who')

    #생성자 : 객체 변수 모두 초기화
    def __init__(self, filename, clsname):        
        #객체 변수
        self.items = DataHandler.GetItemsFromFile(filename)
        self.rawdata = DataHandler.GetRawdataInDic(self.items)

        self.scores = DataHandler.GetScores(self.rawdata)
        
        self.average = round(DataHandler.evaluator.average(self.scores), 1)
        self.variance = round(DataHandler.evaluator.variance(self.scores, self.average), 1)
        self.std_dev = round(math.sqrt(self.variance), 1)

        self.clsname = clsname
        
        self.highest = DataHandler.GetTheHighest(self.rawdata)
        self.lowest = DataHandler.GetTheLowest(self.rawdata)
        
    def GetAverage(self):
        return self.average

    def GetVariance(self):
        return self.average

    def GetStandardDeviation(self):
        return self.std_dev

    def GetEvaluation(self):
        print('*' * 50)
        print("%s 반 성적 분석 결과" % self.clsname)
        print("{0}반의 평균은 {1}점이고 분산은 {2}이며,따라서 표준편차는{3}이다".format(self.clsname, self.average, self.variance, self.std_dev))
        print('*' * 50)
        print("%s 반 종합 평가" % self.clsname)
        print('*' * 50)
        self.evaluateClass(self.average, self.std_dev)
        
    def WhoIsTheHighest(self):
        return self.highest

    def WhoIsTheLowest(self):
        return self.lowest

    def GetScoreByName(self, name):
        return self.rawdata[name]

    def evaluateClass(self, avrg, std_dev):
        if avrg <50 and std_dev >20:
            print("성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.")
        elif avrg > 50 and std_dev >20:
            print("성적은 평균이상이지만 학생들 실력 차이가 크다. 주의 요망!")
        elif avrg < 50 and std_dev <20:
            print("학생들간 실력차는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
        elif avrg > 50 and std_dev <20:
            print("성적도 평균 이상이고 학생들의 실력차도 크지 않다.")





    
    
    
