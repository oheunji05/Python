arr=[5,4,8,3] #list
arr.sort() # arr 리스트 내용 변경
print(arr)

arr=[5,4,3,8] #list
print(sorted(arr)) # arr 리스트 내용 변경 없음
print(arr)

arr=['김철수','박효신','BTS','이문세']
print(sorted(arr)) #오름차순
print(sorted(arr,reverse=True)) #내림차순

# 정렬을 위해 함수를 정렬 기준으로 사용해 보자 key
arr=['banana','apple','pineapple','peach','pear']
print(sorted(arr,key=len)) # key : 내가 원하는 조건을 적는 곳
print(*sorted(arr,key=len))
print(*sorted(arr,key=lambda x:x[2])) # peach pear banana pineapple apple

# 문제 아래와 같이 정렬되도록 하시오
# pear peach banana pineapple apple
print(*sorted(arr,key=lambda x:(x[2], len(x))))