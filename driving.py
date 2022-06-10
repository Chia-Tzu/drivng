country = input('請輸入你的國家: ')
age = input('請輸入你的年齡: ')
age = int(age)

if country == '臺灣':
	if age >= 18 :
		print('你可以考駕照')
	else:
		 print('你還不可以考駕照')
elif country == '英國':
	if age >= 16 :
		print ('你可以考駕照')
	else:
		print('你還不可以考駕照')
elif country == '紐西蘭':
	if age >= 15:
		print ('你可以考駕照')
	else:
		print('你還不可以考駕照')
elif country == '法國':
	if age >= 14 :
		print ('你可以考駕照')
	else:
		print('你還不可以考駕照')
else:
	print('只能輸入臺灣/英國/紐西蘭/法國')