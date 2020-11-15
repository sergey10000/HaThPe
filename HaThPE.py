import time
banner = '''
 ______________
}   HACKING    {
}     THE      {
}  PENTAGON... {
}______________{
Телеграм-канал: @termuxsoid
Введите "start" для взлома Пентагона
'''

def minecraft():
	i = 112724
	while i <= 282734:
		print(str(i) + "   " +str(i) + "   " +str(i) + "   " +str(i))
		if i == 228228:
			print("228 228 - хах")
			time.sleep(5)
		if i == 222222:
			time.sleep(1)
		i = i + 1
	print("Pentagon hacked")

def lol():
	x = input()
	if x == "start":
		minecraft()
	else:
		print("Вы сделали что-то не так введите \"start\" для взлома Пентагона (без ковычек)")
		lol()

print(banner)
lol()





