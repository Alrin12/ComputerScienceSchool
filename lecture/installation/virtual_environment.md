# Fastcampus 
## virtual environment

---
## virtual environment

```python
virtual environment
 : keep dependencies separate
   (프로젝트 의존성을 분리해줍니다)
   
  ex) 예로 어떤 프로젝트는 scrapy ver1을
      다른 프로젝트는 scrapy ver2를 사용할 경우 
      global package conflict (충돌)이 일어날 수 있습니다!
```

---
## virtualenv

```python
$ sudo pip install virtualenv
```

---
## virtualenv

```python
$ pip list
```

---
## virtualenv

```python
$ mkdir project
```

---
## virtualenv

```python
$ cd project
$ virtualenv virenv

$ virtualenv -p /usr/local/bin/python3.6 virenv2
```

---
## virtualenv

```python
$ source virenv/bin/activate
```

---
## virtualenv

```python
$ deactivate
```

---
## virtualenv

```python
$ rm -rf virenv
```

---
## virtual environment in visual studio code

```python
(in settings.json)

{
    "python.pythonPath" : 
    "[virtual environ folder]/bin/python3.6",
    "python.autoComplete.extraPaths" : [
    "[virtual environ folder]/lib/python3.6",
    "[virtual environ folder]/lib/python3.6/site-packages"
    ]

```











