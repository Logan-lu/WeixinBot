 #coding=utf-8 
import simsimi
import language_codes
import response_codes
import re
from simsimi import SimSimiException

keys = ['20666778-3204-480a-b98b-0d705ad7c170','45c0139e-7a59-4c06-9a83-7a9e4c8f6470','59a9d8b2-e4d0-495a-8a9f-1168cbb1193f']
keys_sum = 0
simSimis = []

for i in range(len(keys)):
	simSimis.append(simsimi.SimSimi(
        conversation_language=language_codes.LC_CHINESE_SIMPLIFIED,
        conversation_key=keys[i] ))
simSimi = simSimis[0]

def foo():
	global simSimi
	global keys_sum
	try:
		response = simSimi.getConversation(u'。。'.encode('utf-8'))
	except Exception, e:
		print e
		if str(e).find("Not found") != -1:
			response = {'response': "傻逼"}
		elif str(e).find("Limit Exceeded") != -1:
			response = {'response': "到达每日上限了，正在自动更换api_key，使用第%d个api_key"%((keys_sum+1) % len(keys)+1)}
			keys_sum = keys_sum + 1
			simSimi = simSimis[keys_sum % len(keys)]
		else: 
			response = {'response': "代码出现了未知的问题"}

	print response['response']

for i in range(3):
	foo()