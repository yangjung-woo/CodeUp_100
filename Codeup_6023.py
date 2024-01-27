# 6023 : [기초-입출력] 시분초 입력받아 분만 출력하기(py)
import re

s = input()
c = ':'
# 특정 문제에 대해 Python의 re 모듈 내에서 finditer() 함수를 사용할 수 있습니다
# finditer() 함수는 패턴과 문자열을 입력 매개변수로 사용합니다. 문자열을 왼쪽에서 오른쪽으로 읽고 패턴이 발생한 모든 인덱스를 반환합니다. 
# 목록 이해와 함께 이 함수를 사용하여 Python의 목록 내부에 결과를 저장할 수 있습니다.
# 다음 코드 스니펫은 정규 표현식을 사용하여 문자열 내에서 문자의 모든 인덱스를 찾는 방법을 보여줍니다.

index_list = [i.start() for i in re.finditer(c, s)]


# print(index_list)   [2 , 5] 

print(s[index_list[0]+1:index_list[1]])