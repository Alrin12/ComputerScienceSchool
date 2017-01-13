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
$ tar xvzf [파일명.tgz]

$ tar xvf [파일명.tar.xz]

만약 tar.xz
$ xz -d [파일명.tar.xz]
$ tar xvf [파일명.tar]
```

---
## python 설치 

```python 
$ sudo apt-get install build-essential checkinstall
```

---
## python 설치 

```python 
$ sudo apt-get install libreadline-gplv2-dev 
libncursesw5-dev libssl-dev libsqlite3-dev tk-dev 
libgdbm-dev libc6-dev libbz2-dev
```
---
## python 설치 (command only)

```python 
$ cd /usr/src
```

---
## python 설치 (command only)

```python 
$ wget https://www.python.org/ftp/
    python/3.6.0/Python-3.6.0b3.tgz
```

---
## python 설치 (command only)

```python 
$ sudo tar xzf Python-3.6.0b3.tgz
```

---
## python 설치 (command only)

```python 
$ cd
```

---
## python 설치 (command only)

```python 
$ sudo ./configure
```
---
## python 설치 (command only)

```python 
$ cd Python-3.6.0/
```
---
## python 설치 : makefile 파일 생성

```python 
$ ./configure
```

---
## python 설치 : 컴파일

```python 
$ sudo make
```

---
## python 설치 : 루트 권한으로 설치

```python 
$ sudo make install
```

---
## python 설치 : pip 설치

```python 
pip : 파이썬 관련 패키지 설치시 사용
$ sudo apt-get install python-pip
```

---
## python 설치 : pip 설치

```python 
pip : upgrade
$ pip install --upgrade pip
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
이런 방법도 있지만 우리는 하지 않도록 하죠!

$ sudo nano ~/.bash_aliases


(in the file)
alias python=python3
ctrl + x
y
enter
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

-->.vscode --> settings.json
```


---
## text editor : visual studio code

```pyth
파이썬 개발환경 세팅
setting.json

"python.linting.pylintEnabled" : false
```


