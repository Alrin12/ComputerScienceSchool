s = '''
for i in range(11):
    result += i

print(result)
'''

code = compile(s, '<string>', 'exec')

result = 0
exec(code)


code_2 = compile('a+10', '<string>', "eval")

a = 11
a = eval(code_2)
print(a)

