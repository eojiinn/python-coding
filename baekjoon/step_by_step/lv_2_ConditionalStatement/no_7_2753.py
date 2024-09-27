# 윤년

year = int(input())
# 4 배수 % not 100 배수
# 400 배수
if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)