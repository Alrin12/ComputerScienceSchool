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
$ pip install virtualenv
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
$ source virenv/bin/activate
```

---
## virtualenv

```python
$ pip freeze --local > requirements.txt
```

---
## virtualenv

```python
$ cat requirements.txt
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
## virtualenv

```python
$ virtualenv -p usr/bin python2.7 py27_env
```

---
## virtualenv

```python
$ pip install -r requirements.txt
```

---
## virtual environment in visual studio code

```python

```










