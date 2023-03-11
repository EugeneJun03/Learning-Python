# 주석표현은 #으로 표시한다.

# 자료형(DataType) : 프로그래밍을 할 때 쓰이는 숫자, 문자열 등등의 것들을 뜻한다.

# 자료형의 종류: 숫자형, 문자열, 리스트, 튜플, 딕셔너리, 집합, 불린(boolean)


#  1) 숫자형(크게 두가지로 분류한다면 : 정수형(integer), 부동소수점:실수(float))
#   정수 : 12432
#   실수 : 123.45
#   복소수 : 1+10i
#   8진수 : 0o25
#   16진수 : 0x2F

aa = 124 #정수형은 파이썬에서 long형이 따로 없이 모든 정수는 int형으로 담을 수 있다.
aa = -154
aa = 0

print(aa)

bb = 23.22 # 부동소수점
bb = 32.4E-3 #E표기법 : E뒤의 값이 10지수임을 표현 --> 32.4*10^-3을 의미

cc = 0o166 #8진수 표기법

dd = 0xabc #16진수 표기법

''' 
  숫자 연산 : 사칙연산(+, - , *, /)을 계산기와 마찬가지로 사용한다.
  
  ** : 승 값을 나타내는 연산자
  % : 나머지값을 반환하는 연산자
  // : 소수점자리를 버리는 연산자(즉, 몫이다.)
'''

a = 10
b = 10
c = 100

print (a+b)
'20'
print (a**b)
'10000000000'
print(5%2)
'1'
print(2%5)
'2'
print(3/2)
'1.5'
print(3//2)
'1'

'------------------------------------------------------------------------------'

#2) 문자열(string) : 문자의 나열을 의미한다.(문자들의 집합) 
# 작은 따옴표를 이용해서 문자열을 지정할 수 있다. 예> '헬로우 파이썬!!' 
# 공백과 띄어쓰기 탭등이 그대로 유지된다.

# 큰따옴표 : 작은 따옴표로 둘러싸인 문자열과 완전히 동일하게 취급된다.
# 예> "Hello Python!!" 
# 큰 따옴표안에 작은 따옴표를 포함할 수 있다.
# 예> "I'm OK!!"
print ("I'm OK!!")

# 세개의 따옴표 표현하는 경우 -(""" 또는 ''')
# 세개의 따옴표를 사용하는 경우는 여러 라인에 걸친 문자열을 표현할 때 사용한다.

''' 안녕하세요!!!
반갑습니다....
'''

print (''' 안녕하세요 
반가워요
또 만납시다!!! ''')

""" 반갑습니다...
만나뵈서 ...즐거웠습니다...!!!
"""

''' 파이썬에서는 문자형(char형)이 따로 없다.  파이썬에서는 필요가 없다 '''

''' [ 이스케이프 코드 ]

   \n : 개행(줄바꿈)
   \r : 캐리지 리턴
   \" : 큰따옴표 출력 (")
   \' : 작은따옴표 출력(')
   \000 : 널문자
   \t : 수평탭
   \\ : '\' 문자 표현('\')

-- 문자열 연산 : 파이썬에서는 문자열을 더하고 곱할 수 있다.

[ 문자열 더하기(concatenation) ]
   --> 문자열 + 문자열

[ 문자열 곱하기 ]
문자열 *숫자 는 문자열을 숫자 만큼 반복을 의미한다. 
'''
a = "You've got"
b = " a friend"

print(a+b) #문자열 더하기

c = "hello"
print(c * 3)
'hellohellohello'

print("+" * 30)
print("Hello Python")
print("+"*30)

'''
-- 인덱싱과 슬라이싱

str = "You've got a friend"

'''
str = "You've got a friend"
print(str[4])

print(str[3])
print(str[6])
print(str[7])

print(str[13])

print(str[-1])

str1 = str[-6] + str[-5]+str[-4]+str[-3]+str[-2]+str[-1]

print(str1)

print(str[-1:-6]+"print(str[-1:-6]) 해당식은 잘못된 식으로 결과값이 출력이 되지 않습니다.") #  인덱스 -1에서 -6까지 슬라이스 하겠다.

print(str[-6:]) # 인덱스 -6에서부터 끝까지 슬라이스 한다.

print(str[0:3])
print(str[:3])

print(str[:]) #str문자열 처음 부터 끝까지 슬라이스 한다.

str = "20150613121320"
date = str[:8]
time = str[8:]

year = date[:4]

month =date[4:6]
day = date[6:8]
print (date)
print (time)
print (year+"년"+month+"월"+day+"일")

""" + 'How to reverse a string'
1) stringname[stringlength::-1]
2) stringname[::-1]
3) use while or for structure
"""

#문자열의 교체방법
aa = "ABCD"
print(aa[1] )

#문자열, 튜플 자료형은 그 요소 값을 변경할 수 없다!
'''
aa[1] = 'F' 
print(aa[1])
'''
aa[:1]
print(aa[:1])
aa[2:]
print(aa[2:])

aa = aa[:1]+'F'+aa[2:]

print(aa)

'------------------------------------------------------------------------------'

''' [ 문자열 포맷(Format) ]
   : 문자열 내에 어떤 특정 값을 변화시키는 방법

 예> 현재 날짜는 6월 20일 입니다.
	 ....
	 ....
       현재 날짜는 6월 21일 입니다.

'''
#숫자 대입
print( "제 나이는  %d 살 입니다." %20)

print( "제 나이는  %d 살 입니다." %21)

#문자열 대입

print("저의 이름은 %s 입니다" %"홍길동")
print("저의 이름은 %s 입니다" %"고길동")

# 숫자형 변수로 대입
age = 22
print("제 나이는 %d 살입니다." %age)

# 여러 개의 값을 대입하기
age = 22
name = "김말똥"
print("저의 이름은 %s 입니다. 나이는 %d 입니다." %(name, age))

# 또 다른 포맷 방식

a = "안녕 내 이름은 {} 이야!".foramta("의진")
print(a)

b = "넌 이름이 {} 이구나".format("진하")
print(b)

c = "나는 {name}이고 {sport}를 좋아해".format(name="의진", sport="농구")
print(c)

# 또는 숫자 배열로도 표현할 수 있다.
name="의진"
sport="농구"
c = "나는 {0}이고 {1}를 좋아해".format(name, sport)
print(c)
# f문자열 포메팅 방법
name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
# f문자열 방식은 다른 모든 포메팅에 사용할 수 있습니다.


''' 포맷 코드
%s : 문자열(String)
%d : 정수(Integer)
%f :실수형(float)
%c : 문자(character)
%o : 8진수
%x : 16진수
%% : 리터럴 %

'''

# print("완치될 확률은 %d% 입니다" %70) 는 오류 발생
# not enough arguments for format string
print("완치될 확률은 %d%% 입니다" %70)

''' [포맷코드의 활용예]

  소숫점 표현하기 '''

print("%0.5f" %2.454545) #소숫점 5자리까지 표현하기

#정렬과 공백처리
# %10s 는 전체 길이가 10개인 문자열 공간에서 대입되는 
# 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 
# 남겨 두라는 의미이다.

print("%10s" %"hello")
print("%-10s" %"hello")

print("%-6sPython!!" %'Hello') 

# 또 다른 정렬 방법
"{0:<10}".format("hi") #죄측 정렬
"{0:>10}".format("hi") #우측 정렬
"{0:^10}".format("hi") #가운데 정렬
"{0:=^10}".format("hi") # =으로 공백 체우기

'------------------------------------------------------------------------------'

# [문자열에서의 함수들]
'''1)문자 개수 세기(count)
>>> a = "hobby"
>>> a.count('b')
2
'''
'''2)위치 알려주기(find, index)
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
>>> a = "Life is too short"

>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
ValueError: substring not found-1'''

'''3) 문자열 삽입(join)
>>> ",".join('abcd')
'a,b,c,d'
'''

'''4) 소문자와 대문자 바꾸기(upper, lower)
>>> a = "hi"
>>> a.upper()
'HI'
>>> a = "HI"
>>> a.lower()
'hi'
'''

'''5)오른쪽, 왼쪽 공백지우기(rstrip, lstrip)
>>> a= " hi "
>>> a.rstrip()
' hi'
>>> a = " hi "
>>> a.lstrip()
'hi '
'''

'''6) 문자열 바꾸기(replace)
>>> a = "Life is too short"
>>> a.replace("Life", "Your leg")
'Your leg is too short'
'''

'''7) 문자열 나누기(split)
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
>>> b = "a:b:c:d"
>>> b.split(':')
['a', 'b', 'c', 'd']'''
''' 

'------------------------------------------------------------------------------'

3) 리스트(list)
: 다른 언어의 배열과 같은 형을 의미한다.

 리스트의 예> aa = [10, 20 , 30]
         movies = ["트랜스포머", "국제시장", "명량"]
				  bb = [10, 20, "명량", "국제시장"] 
				  cc =[10, 20,["명량", "국제시장"]]
				  dd =[] 빈리스트
     ** 리스트 내에는 어떠한 자료형도 포함시킬 수 있다.

[리스트의 인덱싱과 슬라이싱]	 
'''
aa= [10, 20, 30]

print(aa[0])

print(aa)

print(aa[1]+aa[2])

print(aa[-1]) #인덱스 값이 -인경우에는 뒤에서 부터 요소를 가리킨다.

bb = [10,20,30,["ab", "cd", "ef"]] # 이중 리스트구조

print(bb[0])
print(bb[-1])
print(bb[3])


print(bb[-1][1])

cc=[10,20,['aa', 'bb', 'cc',["국제시장", "명량"]]]  # 삼중 리스트구조

print(cc[2][3][0]) # 삼중리스트구조에서 인덱싱 하기

# [리스트의 슬라이싱]

ab = [1,10, 100, 1000, 10000]

print(ab[:3])

ab = "110100100010000"
print(ab[:3])

bc = [1,10,100,['aa','bb','cc'],1000, 10000]
print(bc[2:5])

print(bc[3][1:])

#리스트 연산 (+, *:반복)
aa = [10, 20, 30]

bb = [100,200,300]

print (aa+bb)


print(aa*2)

#리스트의 값을 변경하기

print(aa[1])

aa[1]=100 # 문자열, 튜플의 형의 요소값은 변경할 수 없지만, 리스트의 요소값은 변경할 수 있다.
print(aa)

print(aa[2:])
aa[2:] = ["국제시장", "명량"]
print(aa)

print(aa[1:3])

aa[1:3] = ["백", "천", "만"]

print(aa)

aa[4] = ["십만", "백만", "천만"]

print(aa)

aa[1:4] = [] # 요소 삭제 : 인덱스1에서 4까지 삭제

print(aa)

del aa[0] # del함수를 이용한 삭제 방법 del(파이썬 내장함수) del 객체(모든 자료형)
 
print (aa)

'------------------------------------------------------------------------------'

''' 4) 튜플(tuple) : 리스트와 비슷한 자료형이다.
  - 리스트와 튜플의 차이점
    . 리스트는 [ ], 튜플은 ( ) 를 사용한다.
	. 리스트는 요소의 변경(수정, 삭제, 생성)이 가능하지만, 튜플은 요소의 값을 변경할 수 없다.

  사용예>
  tu = () --> 빈값이 들어 있는 형태
  tu2 = (1,)
  tu3 =(10, 20, 30, 40)
  tu4 = 10,20,30
  tu5 = ("국제시장", "명량",("ab", "cd"))

.튜플의 인덱싱, 슬라이싱, 연산
'''

tu = ('a','b','c', 10, 1000)

print(tu[0])

print(tu[2:])

tu2 = ('d', 'e', 'f')
print(tu+tu2)

print(tu*3)


del tu2[2] #튜플은 문자열처럼 요소를 변경하는 것을 허용하지 않는다.

'------------------------------------------------------------------------------'

''' 5) 불린형(참과 거짓) "bool"

		문자열 : "aaa" ---> 참(true), ""(false)
		리스트 : [1,22,33] 참, [](거짓)
		튜플 : ('a','b')참, ()거짓
		딕셔너리 : {}(거짓)
		숫자 : 1(참), 0(거짓)
		None (거짓)
'''

if []:
	print("참")
else:
	print("거짓")

if [1,2]:
	print("true")
else:
	print("false")

'''>>> bool('python')
True
>>> bool('')
False
'''

'------------------------------------------------------------------------------'

# 딕셔너리 a ={Key:"Value"} 즉, Key값을 통해 Value를 알아내는것이다.
'''
>>> a = {1:"Hello!!"}
>>> a
{1: 'Hello!!'}
>>> a = {'first':['a','b','c']}
>>> a
{'first': ['a', 'b', 'c']}
>>> 
>>> sports = {"축구":"박지성", "야구":"강정호", "체조":"손연제"}
>>> 
>>> 
>>> sports["축구"]
'박지성'
>>> sports["야구"]
'강정호'
>>> 
>>> 
>>> aa = {1:"안녕"}
>>> aa[2] = "하이"
>>> aa
{1: '안녕', 2: '하이'}
>>> 
>>> aa[3] = "방가"
>>> aa
{1: '안녕', 2: '하이', 3: '방가'}
>>> aa["인사"] = "굿모닝"
>>> aa
{1: '안녕', 2: '하이', 3: '방가', '인사': '굿모닝'}
>>> aa[3] = [1,2,3]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝'}
>>> aa[age] = 34
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    aa[age] = 34
NameError: name 'age' is not defined
>>> aa["age"] = 34
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], '인사': '굿모닝', 'age': 34}
>>> aa[0] = "adf"
>>> aa
{0: 'adf', 1: '안녕', 2: '하이', 3: [1, 2, 3], 'age': 34, '인사': '굿모닝'}
>>> 
>>> 
>>> 
>>> del aa[0]
>>> aa
{1: '안녕', 2: '하이', 3: [1, 2, 3], 'age': 34, '인사': '굿모닝'}

딕셔너리 주의사항
-- key값(지수)은 고유한 값이므로 중복되는 값을 설정해 놓으면 안된다.
만약 중복이 된다면 하나만 적용되고 나머지는 제외된다.

키값으로 리스트는 쓸 수 없다. 튜플은 키 값으로 사용 가능하다.
키값은 값이 변할 수 없다는 전제하에 타입을 설정하면된다.

dict() 함수

'''

aa = dict() #항목(key:value)이 없는 딕셔너리를 만든다.
print(aa)

aa['one'] = "첫번째"
print (aa)


#keyList 만드는 함수(keys())
bb = {"name":"홍길동", "hp":"010-1234-1234", "age":24}
keyList = bb.keys() #리턴객체는 dict_keys
print(keyList)


for key in bb.keys(): #dict_keys 객체의 각 요소값을 출력
    print(key)

keyList1 = list(bb.keys())#dict_keys 객체를 리스트로 변환
print (keyList1)

#valueList 를 만드는 함수 (values())
valueList = bb.values()#리턴값은 dict_values객체이다.
print (valueList)

#key와 value 한쌍(항목)을 얻기(items())

item = bb.items()#리턴값은 dict_items객체이다. 이객체의 요소는 튜플로 구성된다.
                 #dict_items객체 : [('name', '홍길동'), ('hp', '010-1234-1234'), ('age', 24)] 
print(item)

#key:value 쌍을 모두 삭제하기(clear())
#bb.clear()
#print(bb)

#key값을 이용하여 value를 얻어오기(get)
age = bb.get('age')
print(age)

age = bb['age']#get함수를 이용하지 않고 사용하는 방법
print(age)

'''
gender = bb['gender'] 이때 키값이 존재하지 않으면 에러가 난다.
print(gender) '''

#get()함수는 키값이 존재하지 않을 경우에는 None값을 리턴한다.
gender = bb.get('gender')
print(gender)
print("=======get함수 실행후 bb 딕셔너리 ======")
print(bb)

#딕셔너리내에 키값이 없을 경우 디폴트값을 주는 방법
gender = bb.get('gender', '디폴트값')
print(gender)

#딕셔너리내에 해당 키가 존재하는지 알아보기
confirm_bb = 'gender' in bb
print(confirm_bb)

confirm_bb = 'name' in bb
print(confirm_bb)

#pop()함수를 이용해서 value값을 가져오기: 딕셔너리에 항목을 제거한다.
m = bb.pop('name')
print(m)
print("=========pop함수 실행후 bb 딕셔너리 ========")
print(bb)

bb["name"] = "홍길동"
print(bb)

m = bb.pop('gender','없음') #키가 없는 경우에는 디폴트값으로 대체 :pop(키 [,디폴트값])
print(m)

length = len(bb) #딕셔너리의 항목 갯수를 구함
print(length)

bb.clear() # 딕셔너리의 값을 지운다.

# 딕셔너리의 key가 존재하는 지 확인하는 불문 구조
'''>>> a = {'name':'pey', 'phone':'010-9999-1234', 'birth': '1118'}
>>> 'name' in a
True
>>> 'email' in a
False
'''

'------------------------------------------------------------------------------'

'''6) 집합 자료형
  집합에 관련된 것들을 쉽게 다룰 수 있도록 하기워해 만든 자료형
    특징:
    1.중복을 허용하지 않는다.(그러므로 자료형의 중복을 없에기 위한 필터로 종종 활용된다.)
    2.순서가 없다.(즉, 인덱싱으로 값을 얻을 수 없다.)
    그러므로 인덱싱을 위해서는 리스트나 튜플로 변환하여 사용해야 한다.(딕셔너리도 인덱싱 안됨)
    '''
# 교집합, 차집합, 합집합 구하기
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합
''' 
>>> s1 & s2 
>>> s1.intersection(s2)
{4, 5, 6}
'''

# 차집합
''' 
>>> s1 - s2
>>> s1.difference(s2)
{1, 2, 3}
>>> s2 - s1
>>> s2.difference(s1)
{8, 9, 7}'''

# 합집합
''' 
>>> s1 | s2
>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
'''

s1.add(4) # 4를 s1집합에 추가하기
s1.update([5, 6, 7]) #여러개의 값 추가하기
s1.remove(4) # 특정값 제거하기

