# 產生隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random
start = input('請決定隨機數字開始值')
start = int(start)
end = input('請決定隨機數結束值')
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('請猜數字: ')  #input會把東西存成字串
	num = int(num)
	if num == r:
		print('你猜中了')
		print('這是你猜得第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜得第', count, '次')

