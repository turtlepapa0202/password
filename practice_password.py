#密碼重試程式

#先在程式碼中，設定好密碼 password = 'a123456'
#讓使用者【最多輸入三次密碼】
#不對的話，就印出"密碼錯誤！ 還有__次機會"
#對的話，就印出"登入成功！"

a = 3
real_password = 'a123456'

while a >= 1:
	enter_password = input('請輸入密碼:　')
	if real_password == enter_password:
		print('登入成功')
		break
	else:
		a -= 1
		print('密碼錯誤！ 還有', a, '次機會')
if a == 0:
	print('88')