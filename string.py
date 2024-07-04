hello_world = "mommy said 'hello world'"
print(hello_world)


# 문자열은 문자열끼리 계산 가능(+) / 다른 둘이 합칠라면(,)
name = "박민상"
money = 1000
print("안녕하세요."+ name + "님, 반갑습니다." )
print("입력하신 금액은", money, "원 입니다. 축하드립니다."  )

#  데이터 출력 시 % 기호 사용하는 방법
print("안녕하세요. 저의 이름은 %s입니다."%"박민상")
name = "박민상"
print("안녕하세요. 저의 이름은 %s입니다."%name)

cash = 10000
print("입력하신 금액은 %d 원 입니다."%cash)

a = 7
b = 3
result = (a + b)
print(result)

# 문자열 길이 구하기
hello_world = "mommy said 'hello world'"
print(len(hello_world))

# 문자열 슬라이싱
자유로운_문자열 = "파이썬 정말 재밌다..!"
print(len(자유로운_문자열))
print(자유로운_문자열[0:3])

# 문자열 치환(Replace)
date = "2024.07.04"
print("바꾸기 전의 데이터 :", date)
date = date.replace(".", "-")
print("바꾼 후의 데이터 : ", date)

나 = "박민상/27"
print("바꾸기 전", 나)
나 = 나.replace("/", ":")
print("바꾼 후", 나)

#  문자열 여러 줄 출력하기
자유로운_문자열 = "파이썬 정말 재밌다..! 근데 저는 파이썬 하고 싶지 않아요. \n게임이나 하고 싶습니다."
print(자유로운_문자열)
