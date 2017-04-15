from stack import Stack

class Calculator:
    def __init__(self, exp):
        self.org_exp = exp.replace(' ', '')
        self.postfix_exp = None

    def get_weight(self, oprt):
        if oprt == '*' or oprt == '/':
            return 9
        elif oprt == '+' or oprt == '-':
            return 7
        elif oprt == '(':
            return 5
        else:
            return -1
        
    def convert_to_postfix(self):
        exp_list = []
        oprt_stack = Stack()

        for ch in self.org_exp:
            #숫자 문자이면 수식 리스트에 담는다.
            if ch.isdigit():
                exp_list.append(ch)
            #연산자 문자 처리
            else:
                # '(' or 연산자 스택 비었을 때
                if ch == '(' or not oprt_stack:
                    oprt_stack.push(ch)
                # ')' or '+', '-', '*', '/'
                else:
                    # ')'
                    if ch == ')':
                        while True:
                            op = oprt_stack.pop()
                            if op == '(':
                                break
                            else:
                                exp_list.append(op)
                    # '+', '-', '*', '/'
                    else:
                        # 가중치가 높으면 연산자 스택에 쌓는다.
                        if self.get_weight(ch) > \
                           self.get_weight(oprt_stack.peek()):
                            oprt_stack.push(ch)
                        # 가중치가 낮거나 같으면
                        # 자신보다 더 낮은 연산자가 나올 때까지
                        # pop한 후
                        # 연산자 스택에 쌓는다
                        else:
                            while oprt_stack and \
                                  self.get_weight(ch) <=\
                                  self.get_weight(oprt_stack.peek()):
                                exp_list.append(oprt_stack.pop())
                            oprt_stack.push(ch)
        # 만약 연산자 스택에 연산자가 남아 있으면
        # 없을 때까지 pop 해서 수식 리스트에 추가
        while oprt_stack:
            exp_list.append(oprt_stack.pop())
        self.postfix_exp = ''.join(exp_list)

    def get_postfix_exp(self):
        if not self.postfix_exp:
            self.convert_to_postfix()
        return self.postfix_exp


    def calc_two_oprd(self, oprd1, oprd2, oprt):
        if oprt == '+':
            return oprd1 + oprd2
        elif oprt == '-':
            return oprd1 - oprd2
        elif oprt == '*':
            return oprd1 * oprd2
        elif oprt == '/':
            return oprd1 // oprd2

    def calculate(self):
        oprd_stack = Stack()
        for ch in self.postfix_exp:
            #숫자라면 피연산자 스택에 넣어둔다
            if ch.isdigit():
                oprd_stack.push(int(ch))
            #연산자라면 피연산자 스택에서 두 수를 꺼내 연산
            else:
                oprd2 = oprd_stack.pop()
                oprd1 = oprd_stack.pop()
                oprd_stack.push(
                    self.calc_two_oprd(oprd1, oprd2, ch))
        return oprd_stack.pop()

if __name__=="__main__":
    a = input("수식을 입력하세요 : ")
    calc = Calculator(a)
    print(calc.get_postfix_exp())
    print("{exp} = {result}".format(
        exp = calc.org_exp, result = calc.calculate()))    
