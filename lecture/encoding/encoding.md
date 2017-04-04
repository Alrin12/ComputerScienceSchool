# Computer Science School
## encoding

---

#  character encoding
## from characters to code
 - from 'a' to 97(ASCII)
---

# character encoding
## encoding model
 - ASCII : 7 bit (2의 7승 : 128 가지 문자)
   - 로마자 및 특수 기호(한글 포함 안됨)
 - unicode
   - 2 byte (2의 16승 : 65,536가지 문자)
   - 한글 및 많은 언어 포함
   - 모든 인코딩 방법을 대체하려고 함

---

# character encoding
## unicode exam
 - 'A' - U+0041 (ASCII 호환)
 - '가' - U+AC00
---

# character encoding
## unicode exam
```python
>>> '\u0041'
'A'
>>> '\uAC00'
'가'
```
---
# character encoding
## 한글의 범위
  - U+AC00 ~ U+D7AF
```python
>>> '\uAC00'
'가'
>>> '\uB098'
'나'
>>> '\uB2E4'
'다'
```

---
# character encoding
## 공식에 의해 한글 유니코드 계산하기
  - 0xAC00 + (초성순서 * 21) + 중성순서) *28 + 종성순서
```python
def make_hangul_unicode(cho, jung, jong):
	unicode = 0xAC00 + ((cho * 21) + jung) * 28 + jong
    	return chr(unicode)
        
# 양
# ㅇ : 11 (초성), ㅑ : 2 (중성), ㅇ : 21(종성)
print(make_hangul_unicode(11, 2, 21))
```

---
# character encoding
## UTF-8 이란?
 - 유니코드의 부호화 방식
   - UTF-8 
     - 8bit 기반
     - 가변 길이 유니코드 인코딩 시스템 
   - UTF-16
   - UTF-32

---
# character encoding
## UTF-8 이란?
 - 1 byte ~ 4 byte 
 - U+0000 ~ U+007F(ASCII)
   - 1 byte로 나타낸다
 - 


---
# character encoding
## in python
 - 부호화 방식이 UTF-8
```python
>>> coded = "abcde".encode()
>>> coded
b'abcde'
```
---
# character encoding
## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "abcde".encode()
>>> for ch in coded_string:
		print(ch)
97
98
99
100
101
```
---

# character encoding
## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "파이썬".encode()
>>> coded_string
b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac' # 한 글자당 3byte
```
---
# character encoding
## '가'의 encoding 과정
 - UTF-8 구조 
   - 0800 - FFFF 
     ==> 1110XXXX 10XXXXXX 10XXXXXX
   - '가'의 유니코드 
     ==> U+AC00
     ==> 1010 1100 0000 0000
     ==> 1010 110000 000000
   - 11101010 10110000 10000000
   - 0xEAB080
   - 즉, 3 바이트로 인코딩
---

---
# character encoding
## '가'의 encoding 과정
  - 0xEAB080
 ```python
 >>> '가'.encode('UTF-8')
 b'\xea\xb0\x80'
 # EA B0 80
 ```
---

# character encoding
## in python
 - 부호화 방식이 UTF-8
```python
>>> string = coded_string.decode()
>>> string
"파이썬"
```
---

# character encoding
## in python
 - 부호화 방식이 UTF-8
```python
>>> string = coded_string.decode()
>>> string
"파이썬"
```