def make_hangul_unicode(cho, jung, jong):
    unicode = 0xAC00 + ((cho * 21) + jung) * 28 + jong
    return chr(unicode)

#양
#ㅇ : 11 (초성), ㅑ : 2 (중성), ㅇ : 21(종성)
print(make_hangul_unicode(11, 2, 21))
    
