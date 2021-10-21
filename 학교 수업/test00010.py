# 알파벳을 정렬하라
# arr=['b','c','a','f','t','e']
# print(arr)
# # 정렬
# arr.sort()
# print(arr)
# print(arr[0]) #아스키 코드값이 제일 작은 알파벳을 출력
# print(len(arr)) #배열의 길이 출력


# 문제 : 아래 알파벳 중 가장 빨리 나오는 것과 마지막에 나오는 알파벡을 출력하시오.
# arr=['t','b','c','k','u','n']

# arr = ['t', 'b', 'c', 'k', 'u', 'n']
# arr.sort()
# # arr.sort(reverse=True) #거꾸로 출력
# print(arr[0],arr[len(arr)-1])
#n=len(arr)-1
#print(arr[0],arr[n])

#[문제]
# score=[55, 78, 99, 34, 87]
#1위 점수를 출력하시오

score=[55, 78, 99, 34, 87]
# score.sort()
# print(score[len(score)-1])
print(max(score))
print(min(score))