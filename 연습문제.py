# 연습문제 5
# 1. 주어진 변수 및 데이터를 할당
old = 'Python'
print(len(old))
# 슬라이싱 해보기
print(old[5])
new = old[5] + old[4] + old[3] + old[2] + old[1] + old[0]
print(new)


# 연습문제 6
var = 'abcd'
var = var.replace("a", "A")
print(var)

# 연습문제 7 리스트의 평균 구하기
# nums = [1, 2, 3, 4, 5]
nums = list(range(1, 6))
# print(nums)
sum_nums = nums[0] + nums[1] + nums[2] + nums[3] + nums[4]
average = sum_nums / (len(nums))
print(average)

# 연습문제 8
var = {'aplle': 3, 'banana': 5, 'cherry': 2}
print(var['banana'])

# 한국, 미국, 중국의 위도, 경도 데이터 (dictionary)
nat = {'KOR' : {"위도": 37, "경도" : 127}, 'USA': {"위도": 48, "경도" : 122}, 'CHN' : {"위도": 20, "경도" : 75}}
print(nat['KOR'])
