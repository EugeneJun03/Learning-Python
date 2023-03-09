"""파이썬은 배터리 포함(Batteries included)이라는 철학을 고수하여 유용한 작업을
처리하기위한 많은 표준 라이브러리(Standard library)가 있다.
이 파일에서는 제네릭(generic)를 사용할 수 있는 일부 모듈들을 살펴볼 것이다.
"""

"""1번 누락된 키 처리하기: setdefault(), defaultdict()
- 파이썬에서는 존재하지않는 키로 딕셔너리에 접근하려 하면 예외가 발생한다. 
기본값을 반환하는 get()함수를 활용하면 이예외를 피할 수 있다.
setdefault()함수는 get()함수와 같지만, 키가 누락된 경우 딕셔너리에 항목을 할당시킬 수 있다.
"""
#딕셔너리에 키가 없는 경우 새 값이 사용된다.
'''
>>> periodic_table = {'Hydrogen': 1, 'Helium': 2}
>>> print(periodic_table)
{'Hydrogen': 1, 'Helium': 2}
>>> carbon = periodic_table.setdefault('carbon', 12)
>>> carbon
12
>>> periodic_table
{'Hydrogen': 1, 'Helium': 2, 'carbon': 12}'''

# 존재하는 키에 다른 기본값을 할당하려 하면 키에 대한 원래 값이 반환되고 아무것도 바뀌지 않느다.
'''
>>> carbon = periodic_table.setdefault('carbon', 72)
>>> carbon
12
>>> periodic_table
{'Hydrogen': 1, 'Helium': 2, 'carbon': 12}'''

"""defultdict()함수는 딕셔너리를 생성할 때 모든 새 키에 대한 기본값을 먼저 지정한다.
이 함수의 인자는 함수이다."""

from collections import defaultdict
periodic_table = defaultdict(int)
#이제 모든 누락된 기본값은 0이댜.
periodic_table['Hydrogen'] = 1
'''
>>> periodic_table['Lead']
0
>>> periodic_table
defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})'''
#defaultdict()의 인자는 값을 누락된 키에 할당하여 반환하는 함수이다.
'ex)1'
from collections import defaultdict
def no_idea():
    return 'Huh?'
bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
'''
>>> bestiary['A']
'Abominable Snowman'
>>> bestiary['B']
'Basilisk'
>>> bestiary['C']
'Huh?'
'''
# int() = 0
# list() = []
# dict() = {}를 각각 반환한다. 만약 인자를 입력하지 않으면 None으로 설정된다.

'+ lamda를 사용해서 인자에 기본값을 설정할 수 있다.'
bestiary = defaultdict(lambda: 'Hola!')
'''
>>> bestiary = defaultdict(lambda: 'Hola!')
>>> bestiary['D']
'Hola!'
'''