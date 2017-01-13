# Fastcampus 
## Python install


---
## python 설치

```python
python.org 방문 후 python 3.6 다운로드
```

---
## python 설치

```python
$ tar xvzf Python-3.6.0.tgz
```

---
## python 설치 : makefile 파일 생성

```python 
$ ./configure
```

---
## python 설치 : 컴파일

```python 
$ make
```

---
## python 설치 : 루트 권한으로 설치

```python 
$ sudo su
$ make install
```

---
## python 설치 : pip 설치

```python 
pip : 파이썬 관련 패키지 설치시 사용
$ sudo apt-get install python-pip
```

---
## python 설치 : pip 사용하기

```python 
$ pip install numpy
$ pip uninstall numpy
$ pip install numpy --upgrade
$ pip search numpy
```


---
## python 설치 3.6을 default로

```python 
$ sudo nano ~/.bash_aliases
(in the file)

alias python=python3
(save this and quit)
```

---
## text editor : visual studio code

```python 
ctrl + p -> ext install python
```

---
## text editor : visual studio code

```python 
show all command
ctrl + shift + p
```

---
## text editor : visual studio code

```python
사용할 인터프리터 설정
python:Select Workspace Interpreter
```

---
## text editor : visual studio code

```python 
깔았던 package을 지울 때
$sudo apt-get remove --auto-remove <패키지이름>
```

---
## text editor : visual studio code

```pyth
파이썬 개발환경 세팅
setting.json

"python.linting.pylintEnabled" : false
```


