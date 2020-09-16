driving = input('請問你有沒開過車?')
if driving != '有' and driving !='沒有':
	print('只能輸入有/沒有')
	raise SystemExit

age = input('請問你幾歲?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜恭喜')
	else: # else age < 18:
		print('給我滾旁邊去')
elif driving == '沒有':
	if age >= 18: #if age >= '18':
		print('可以去開了阿小呆瓜')
	else: #if age < 18:
		print('知道未滿18開車就好')
else:
	print('只能輸入 有/沒有')