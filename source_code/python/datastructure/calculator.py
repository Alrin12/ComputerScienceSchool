#Calculator class

class Calculator:
    def __init__(self, exp):
        temp = list(exp)
        for t in temp:
            if t == ' ':
                temp.remove(' ')
        self.orgExp = ''.join(temp)

    def ConvertToPostfix(self):
        def GetWeight(a):
            if a == '*' or a == '/':
                return 9
            elif a == '+' or a == '-':
                return 7
            elif a =='(':
                return 5
            else:
                return -1
            
        listExp=[]
        listStack=[]
        orgList = list(self.orgExp)

        for ch in orgList:
            if ch.isdigit():
                listExp.append(ch)
            else:
                if ch == '(' or not listStack:
                    listStack.append(ch)
                else:
                    if ch == ")":
                        while 1:
                            op = listStack.pop()
                            if op == '(':
                                break
                            else:
                                listExp.append(op)
                    else:
                        if GetWeight(ch) > GetWeight(listStack[-1]):
                            listStack.append(ch)
                        elif GetWeight(ch) <=GetWeight(listStack[-1]):
                            while listStack and GetWeight(ch) <=GetWeight(listStack[-1]):
                                op = listStack.pop()
                                listExp.append(op)
                            listStack.append(ch)
        while listStack:
            op = listStack.pop()
            listExp.append(op)

        self.postfixExp = ''.join(listExp)
        return self.postfixExp
    
    def Calculate(self):
        def calcTwoOp(a, b, c):
            if c=='+':
                return a+b
            elif c=='-':
                return a-b
            elif c=='*':
                return a*b
            elif c=='/':
                return a//b

        listOperand=[]
        for ch in self.postfixExp:
            if ch.isdigit():
                listOperand.append(int(ch))
            else:
                b = listOperand.pop()
                a = listOperand.pop()
                result = calcTwoOp(a, b, ch)
                listOperand.append(result)
        result = listOperand.pop()
        return result




if __name__ == "__main__":
    a = input("수식을 입력하세요")
    calc = Calculator(a)
    b = calc.ConvertToPostfix()
    print("Postfix Expression : %s" % b)
    result = calc.Calculate()
    print("%s = %d" % (calc.orgExp, result))
            
