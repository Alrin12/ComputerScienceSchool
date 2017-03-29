#fibonacci series
'''
def fibo(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

        
n = 10
f = fibo(n)
print(f)

for i in range(n):
    print(next(f), end = '  ')
'''

#returning a generator instead of iterator
'''
class Square:
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        for i in range(1, self.n+1):
            print("calculated....")
            yield i * i

n = 5
s = iter(Square(n))

sum = 0

result = next(s)
print(result)
sum +=result

result = next(s)
print(result)
sum +=result

result = next(s)
print(result)
sum +=result

result = next(s)
print(result)
sum +=result

result = next(s)
print(result)
sum +=result


print("the result of sum : {}".format(sum))
'''

cnt = 0
#중첩 리스트를 단일 리스트로
def traverse(li):
    global cnt
    cnt+=1
    print("traverse called {}".format(cnt))
    for ele in li:
        if isinstance(ele, list):
            for e in traverse(ele):
                print(e, " on recursive for loop")
                yield e
        else:
            print(ele)
            yield ele

li = [1, 2, [3, 4, 5], [6, [7, [8], 9], 10], 11, 12]
result = list(traverse(li))
print(result)
