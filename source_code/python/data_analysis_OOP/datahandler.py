from evaluate import *
import openpyxl

class DataHandler:
    #클래스 멤버 : 연산기 하나 
    evaluator = Evaluate()
    
     #class method : 전역함수처럼 쓸 수 있다              
    @classmethod
    def get_data_from_excel(cls, filename):
        dic = {}
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
        for a, b in ws['A1' : 'B10']:
            dic[a.value] = b.value
        return dic
    
    def __init__(self, filename, clsname):
        self.rawdata = DataHandler.get_data_from_excel(filename)
        self.clsname = clsname 
        #연산한 값을 저장해두는 저장소
        #필요할 때 연산하되
        #이미 연산된 값이면 연산 없이 저장된 값을 반환
        self.cache = {}
        
    def GetScores(self):
        if 'scores' not in self.cache:
            self.cache['scores'] = list(self.rawdata.values())
        
        return self.cache.get('scores')
      
    def GetAverage(self):
        if 'average' not in self.cache:
            self.cache['average'] = self.evaluator.average(self.GetScores())
        
        return self.cache.get('average')

    def GetVariance(self):
        if "variance" not in self.cache:
            vari = self.evaluator.variance(
                self.GetScores(), self.GetAverage())
            self.cache["variance"] = vari
  
        return self.cache.get("variance")

    def GetStandardDeviation(self):
        if "standard_deviation" not in self.cache:
            std_dev = self.evaluator.std_dev(
                self.GetVariance())
            self.cache["standard_deviation"] = std_dev

        return self.cache.get("standard_deviation")
    
    def WhoIsHighest(self):
        if "highest" not in self.cache:
            self.cache['highest'] = reduce(lambda a, b:
                              a if self.rawdata.get(a) > self.rawdata.get(b) else b,
                            self.rawdata.keys())
            
        return self.cache.get("highest")
    
    def GetHighestScore(self):
        return self.rawdata[self.WhoIsHighest()]
    
    def WhoIsLowest(self):
        if "lowest" not in self.cache:
            self.cache['lowest'] = reduce(lambda a, b:
                                a if self.rawdata.get(a) < self.rawdata.get(b) else b,
                                         self.rawdata.keys())
            
        return self.cache.get('lowest')
    
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
