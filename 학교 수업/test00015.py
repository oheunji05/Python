#팩토리얼 구현

num=int(input('자연수 입력 : '))
fac=1 #초기값 설정

for i in range(1,num+1,1): #for i in range(1,num+1):
    fac=fac*i

#for(i=1;i<num+1;i++){
#    fac=fac*i
#}

print(f'{num} 팩토리얼은 {fac}입니다')