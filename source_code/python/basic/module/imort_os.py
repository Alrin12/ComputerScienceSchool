import os
#from datetime import datetime

# 모든 attributes and methods
#print(dir(os))

#1. get current working directory
#print(os.getcwd())

#2. change directory
#os.chdir('C:\\Users\\user\\')
#print(os.getcwd())

#3. list directory
#print(os.listdir())

#4. make directory
#os.mkdir('testfolder')

#5. remove drectory
#os.rmdir('testfolder')

#with open("test.txt", "w") as f:
#    pass

#6. rename a file or a directory
#os.rename('test.txt', 'pypy.txt')
#os.rename('testfolder', 'pypyfolder')

#7. statistics for a file or a directory
#print(os.stat('pypy.txt'))
#print(os.stat('pypyfolder'))
#파일크기를 바이트로
#print(os.stat('pypy.txt.').st_size)      

#최종 수정 시간
'''
mod_time = os.stat('pypy.txt').st_mtime
print(datetime.fromtimestamp(mod_time))
'''

#8. walk all of directory trees
'''
for dirpath, dirnames, fnames in os.walk('C:\\Users\\user\\Desktop\\'):
    print("Current Path : ", dirpath)
    print('Directories : ', dirnames)
    print('Files : ', fnames)
'''

 #9. 환경변수 접근
#print(os.environ)
#print(os.environ.get('HOME'))

fpath = os.path.join(os.environ.get('HOME'), 'desktop/text.txt')
print(fpath)


with open(fpath, 'w') as f:
    f.write("python is good. We can do everything!")

    
