#공책 정리
import random

arr=list() # arr를 리스트로 선언
# arr=[] # arr를 리스트로 선언
print(arr) #[]가 출력, 빈 리스트 의미

#로또 번호 생성기
for i in range(6): #6회 반복 range(0,6,1)
    arr.append(random.randint(1,46)) #1에서 46사이의 숫자 생성
    #append는 리스트에 차례대로 데이터 삽입

print(arr) #로또 리스트 출력

# arr에 있는 데이터 중 가장 큰 값을 출력하시오
print(max(arr))

arr.sort()
print(arr[-1])

#리스트에서 두번째 큰 값을 출력하시오
arr.sort(reverse=True) #내림차순
print(arr[1])

arr.sort() #오름차순
print(arr[-2])