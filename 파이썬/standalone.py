"""스텐드얼로운(standalone) 프로그램
지금까지는 파이썬의 대화식 인터페이스에서 코드를 작성하고 실행했다.
이번에 만들 파이썬 프로램은 <<< 가 존재하지 않는다.
실행하기위해서는 터미널 창에서 다음과 같이 입력하면 된다.
$ python standalon.py"""

print("this standalon program works!")

import sys
print('Program argument:', sys.argv)

"""모듈(module), Import문
파이썬에는 계층구조(Hierarchy)가 존재한다.
상향식구조로 
단어:데이터 타입(data type)
문장:선언문(statement)
단락:함수(function)
장:모듈(module)
"""

"""이번에는 import문을 사용하여 다른 모듈을 참조하는 방법을 배워볼 것이다.
import한 모듈은 해당 파일 내에 있는 코드와 변수를 사용할 수 있게 만들어 준다."""

#ex) wetherman.py와 report.py파일을 만들어준다.
