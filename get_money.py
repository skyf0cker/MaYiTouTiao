#coding=utf-8
import os
import time


i = 0
time_start = time.time()
print("正在拼命挣钱...\n")
while True:
	i += 1
	a = os.system("adb shell input roll 0 10")
	b = os.system("adb shell input roll 0 -10")
	time_end = time.time()
	if time_end - time_start >= 200:#861 1187
		print("时间间隔为："+str(time_end - time_start))
		print("马上进入下一篇文章...")
		# c = os.system("adb shell input tap 861 1187")
		c = os.system("adb shell input tap 54 143") #返回列表
		time.sleep(2)
		d = os.system("adb shell input swipe 200 400 200 900")  #刷新
		time.sleep(2)
		e = os.system("adb shell input tap 554 422") #点击第一个
		time_start = time_end+4


			#adb shell input tap 54 143
			#adb shell input swipe 200 400 200 900
			#adb shell input tap 554 422
	if a == 1 or b == 1:
		break