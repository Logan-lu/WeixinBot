
import subprocess
import os
import codecs
import json
import re 

vedio_formats = ['mp4','avi','wmv','mov'] # 1
audio_formats = ['wav','flac','mp3','aiff'] # 2

def file_upload(voice):
	regex = r"(.+)\/(.+)"
	if re.search(regex, voice):
		match = re.search(regex, voice)
		file_dir = match.group(1) + '/'
		file_name_and_type = match.group(2).lower() 
	else: 
		raise fileNameError('fileNameError')
	regex = r"(.+)\.(.+)"
	if re.search(regex, file_name_and_type):
	    match = re.search(regex, file_name_and_type)
	    file_name = match.group(1)
	    file_type = match.group(2).lower()
	else: 
		raise fileNameError('fileNameError')
	file_pwd = file_dir + file_name_and_type
	transcripts_timed_pwd = file_dir + file_name + '.json'
	autosubing(file_pwd,transcripts_timed_pwd,file_type)
	json_data = open(transcripts_timed_pwd)
	transcripts_timed = json.load(json_data)
	transcripts_content = ''
	for i in transcripts_timed:
		transcripts_content = transcripts_content + ' ' + i['content']
	json_data.close()
	return transcripts_content

def autosubing(file_pwd,transcripts_timed_pwd,file_type):
	if file_format(file_type) == 1:	
		# command = "python autosub.py -F json -V %s" %(file_pwd)
		command = "python autosub.py %s -F json" %(file_pwd)
	else: 
		command = "python autosub.py %s -F json" %(file_pwd)
	subprocess.call(command, shell=True)	
	print "Autosubed"


# throw formatError
def file_format(file_type):
	if file_type in vedio_formats:
		return 1;
	elif file_type in audio_formats:
		return 2
	else: raise Exception('Format prohibited')

# dir1 = '/Users/n0where/GoogleDrive/WeixinBot/saved/voices/voice_2546547996039896197.mp3'
# dir2 = '/Users/n0where/Desktop/DFA_01.flac'
# dir3 = '/Users/n0where/GoogleDrive/ASQ/ASQ/transcripts/Chem101.mp4'
# dir4 = '/Users/n0where/GoogleDrive/WeixinBot/saved/voices/voice_1089270824656503909.mp3'
# dir5 = '/Users/n0where/GoogleDrive/WeixinBot/saved/voices/voice_8675834799709315495.mp3'
# print file_upload(dir5)
