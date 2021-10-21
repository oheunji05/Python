# 두 수를 입력받아 덧셈을 출력하도록 하시오.
# [입력] 4 7
# [출력] 11

#n1,n2=map(int, input().split()) # 한 줄에 입력 받을 때   map(int, input().split()) 외우기
#print(n1+n2)



#두 숫자를 입력 받아 더 큰 숫자를 출력하는 프로그램을 만드시오
# [입력] 8 3
# [출력] 8

# n1,n2=map(int, input().split())
# if(n1>n2):
#     print(n1)
# else:
#     print(n2)


#제어문 : if문
# a=5
# if a>3:
#     print('3보다 큼')
# elif a>1: #else if
#     print('3보다 작고 1보다 큼')
# else :
#     print('1보다 작음')


#숫자 하나 입력 받아 70이상이면 '최우수'
# 그 외 50이상이면'우수'
# 그 외 20이상이면 '보통'
# 그 외는 '노력 필요'를 출력하는 프로그램을 만드시오.

a=int(input('숫자 하나를 입력하시오 : '))
if a>=70:
    print('최우수')
elif a>=50:
    print('우수')
elif a>=20:
    print('보통')
else:
    print('노력 필요')