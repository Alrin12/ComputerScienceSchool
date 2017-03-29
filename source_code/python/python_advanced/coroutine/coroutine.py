
def echo():
    s = "coroutine started"
    try:
        while True:
            msg = (yield s)
            s = "message of \"{}\" received".format(msg)
            print(msg, "in coroutine")
    except GeneratorExit:
        print("coroutine closed")
    except RuntimeError:
        print("RuntimeError occurred!")
    except BaseException as e:
        print(e)
    finally:
        print("good bye")
    
#coroutine object 생성
e_obj = echo()
print(e_obj)

#코루틴 실행
received_s = next(e_obj)
print(received_s)
print()

#send message

for i in range(3):
    input_s = input("message : ")
    received_s = e_obj.send(input_s)
    print(received_s)
    print()

'''
try:
    e_obj.throw(BaseException("BaseException has been thrown"))
except StopIteration:
    pass
'''

#coroutine close
#close() does nothing if the generator already exited due to an exception or normal exit
e_obj.close()
