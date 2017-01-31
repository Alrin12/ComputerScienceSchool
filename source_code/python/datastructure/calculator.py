class Calculator:
    def __init__(self, exp):
        #만약 빈 공간이 있다면 없앤다
        self.orgExp = exp.replace(' ', '')

    
    
    def ConvertToPostfix(self):

        #연산자에 가중치를 부여한다
        # '('의 경우는 다른 연산자보다 우선 순위가 낮다
        def GetWeight(oprt):
            if oprt == '*' or oprt == '/':
                return 9
            elif oprt =='+' or oprt =='-':
                return 7
            elif oprt == '(':
                return 5
            else:
                return -1
        #후위표기법으로 만들어 담을 수식 리스트
        listExp=[]
        #연산자를 후위표기법에 맞춰서 이동시킬 스택 리스트
        listStack=[]

        for ch in self.orgExp:
            #만약 숫자(피연산자)라면 바로 수식 리스트에 담는다
            if ch.isdigit():
                listExp.append(ch)
                #연산자일 것 이므로 가중치에 따라 스택 리스트에 담는다
            else:
                #만약 '('이거나 스택 리스트가 비었다면 무조건 담는다
                if ch == '(' or not listStack:
                    listStack.append(ch)
                else:
                    #')'를 만나면 스택 리스트에서 '('를 만나기까지 모든 연산자를
                    # 수식 리스트에 담는다
                    if ch == ')':
                        while 1:
                            op = listStack.pop()
                            if op == '(':
                                break
                            else:
                                listExp.append(op)
                    else:
                        #가중치가 높다면 스택 리스트에 쌓인다
                        if GetWeight(ch) > GetWeight(listStack[-1]):
                            listStack.append(ch)
                        #만약 연산자의  가중치가 낮거나 같다면
                        #가중치가 더 낮은 연산자를 만날 때까지
                        #모두 수식 리스트에 담는다
                        #자신과 같은 가중치를 가진 연산자를 만나도 수식 리스트에 담는다!!!
                        elif GetWeight(ch) <= GetWeight(listStack[-1]):
                            #스택리스트가 비어있지 않아야 수식 리스트에 담을 수 있다!!
                            while listStack and GetWeight(ch) <=GetWeight(listStack[-1]):
                                op = listStack.pop()
                                listExp.append(op)
                            listStack.append(ch)
        #만약 연산자가 listStack에 남아있다면 모두 listExp에 담는다
        while listStack:
            op = listStack.pop()
            listExp.append(op)

        #후위표기법 수식으로 변환하여 멤버 변수로 만든다
        self.postfixExp = ''.join(listExp)
        return self.postfixExp

    def Calculate(self):
        def calcTwoOp(op1, op2, oprt):
            if oprt == '+':
                return op1 + op2
            elif oprt == '-':
                return op1 - op2
            elif oprt == '*':
                return op1 * op2
            elif oprt == '/':
                return op1//op2

        stackOperand=[]
        for ch in self.postfixExp:
            #숫자라면 피연산자 스택에 넣어둔다
            if ch.isdigit():
                stackOperand.append(int(ch))
            #연산자라면 피연산자 스택에서 두 숫자를 꺼내 연산 후 다시 스택에 insert
            else:
                #'-', '/'의 경우 순서가 중요하기 때문에 op1, op2의 순서가 중요함
                op2 = stackOperand.pop()
                op1 = stackOperand.pop()
                result = calcTwoOp(op1, op2, ch)
                stackOperand.append(result)

        #최종 연산 결과도 피연산자 스택에 들어있는 상태이므로 꺼내어 반환한다
        result = stackOperand.pop()
        return result

if __name__ == "__main__":
    a = input("수식을 입력하세요 : ")
    calc = Calculator(a)
    #빈공간을 잘 없애는지 테스트 코드
    print(calc.orgExp)
    #후위 표기법으로 잘 바꾸는지
    postExp = calc.ConvertToPostfix()
    print(postExp)
    #잘 계산하는지
    result = calc.Calculate()
    print("%s = %d" %(calc.orgExp, result))
    
    

