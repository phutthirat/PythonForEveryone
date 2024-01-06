Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = ming
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name = ming
NameError: name 'ming' is not defined. Did you mean: 'min'?
name = 'ming'
lastname = 'chimthai'
fullname = name + ' ' + lastname
print(fullname)
ming chimthai
>>> fullname = name + lastname
>>> print(fullname)
mingchimthai
>>> type(name)
<class 'str'>
>>> age = 10
>>> type(age)
<class 'int'>
>>> name = 'Ming'
>>> name.upper()
'MING'
>>> name.lower()
'ming'
>>> print(name)
Ming
>>> name = name.upper()
>>> print(name)
MING
>>> number = '1'
>>> number.zfill(5)
'00001'
>>> number = '15'
>>> number.zfill(5)
'00015'
>>> print('ลุงครับผมชื่อ{} นามสกุล{} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อMING นามสกุลchimthai อายุ 10 ขวบ
>>> print(f'ลุงครับผมชื่อ{name} นามสกุล{lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อMING นามสกุลchimthai อายุ 10 ขวบ
