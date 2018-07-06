#!/usr/bin/env python
# -*- coding=utf-8 -*-

import subprocess
import os
import time
import re
from threading import Timer



Run_In_Detail = False

def addTestCase(caseDir, case_list):
	os.chdir(caseDir)
	filelist = os.listdir('.')
	file_list = []
	for i in range(len(filelist)):
		num = re.findall(r'\d+',filelist[i])[0]
		file_list.append((filelist[i],int(num)))

	#sort according to the number in the Case name
	file_list = sorted(file_list, key=lambda x:x[1])
	filelist = [row[0] for row in file_list]

	for aFile in filelist:
		caseFile = open(aFile)
		try: # read all files into caseTxt
			testParam = ''
			testRes = ''
			testScore = '0'
			for line in caseFile.readlines():
				if line in ['\r\n', '\r', '\n']: #empty line
					continue
				elif line.find("#SCORE") != -1:
					testScore += line.replace('#SCORE:', '').strip('\n')
				elif line.find("#RES") != -1:
					testRes = line
				else:
					testParam = testParam + line
			testRes2=testRes.replace('#RES:', '').strip('\n')

			#case_list = [(case_name,input,output,score)]
			case_list.append((aFile,testParam,testRes2,int(testScore)))

		finally:
			caseFile.close()

def addExe(exeDir):

	return os.listdir(exeDir)


#feature: terminalt after timeout begin
def timer_expiry(proc,f):

	#print "timer expired"
	f.append('expiry')

	ppid = str(proc.pid)
	cmd = ['tskill',ppid]
	#Windows terminate a process using 'tskill', type 'tasklist' in cmd to see processes
	p = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

	err = p.communicate()[1]

	#print "DEBUG pid {} was killed".format(proc.pid)	

	if err == '':
		#print "%s was terminated."%(str(ppid))
		pass
	else:
		print "terminate process failed, err=",err

#feature: terminalt after timeout end



def callProc(cmd, inStr, outStr, trial_run = False):
	'''
	input: 
	cmd: trigger cmd
	inStr: input string
	outStr: Expected output string
	trial_run: to judge if print log

	'''
	global Run_In_Detail

	result = 1

	#print "debug cmd:",cmd
	p1 = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,\
	 stderr=subprocess.PIPE, shell=False)

	#feature: terminalt after timeout begin
	f = []
	my_timer = Timer(5,timer_expiry,[p1,f])
	try:
		my_timer.start()
		realOutStr, errStr = p1.communicate(input=inStr)
	except:
		print "Debug:catch except"
	finally:
		my_timer.cancel()	
	#feature: terminalt after timeout end

	#get rid of '\n\r' in windows
	realOutStr = realOutStr.strip(os.linesep)

	#Right answers prior to errors
	if cmp(outStr, realOutStr)!=0:
		'''
		if Run_In_Detail and not trial_run:
			print("\nYour output: {}".format(realOutStr))
			print("   Expected: {}".format(outStr))
		'''
		if outStr in realOutStr:
			return result,realOutStr,errStr
		else:
			result = 0
	else:
		return result,realOutStr,errStr

	if errStr != '':
		result = 0
		return result,realOutStr,errStr

	#timer expired accounted as TLE
	if len(f) == 1 and f[0] == 'expiry':
		result = 0
		errStr = "5s timer expired"

	return result,realOutStr,errStr


def execTest():
	timeMsLimit = 1500	# 1000ms = 1S
	#These dir can be used only after the system environment configured.
	#Check out the readme to see how to set system environment variables.
	python2Dir = 'python2'
	python3Dir = 'python3'
	javaDir = 'java'
	javacDir = 'javac'
	gccDir = 'gcc'
	gppDir = 'g++'	
	#Felix change the path begin	
	exeDir      = os.path.join(os.getcwd(),'exe')
	testCaseDir = os.path.join(os.getcwd(),'case')
	#Felix change the path end

	exe_file_list = addExe(exeDir)

	case_list = []
	#case_list = [(case_name,input,output,score)]
	addTestCase(testCaseDir, case_list)
	case_total = len(case_list)	
	file_total = len(exe_file_list)
	score_total = sum([item[-1] for item in case_list])

	#case_result_list =[(code_name,language,score,run_time,state)]
	case_result_list = []
	submit_total = 0

	print "%d tests in 'case'"%(case_total),
	print "%d files in 'exe'"%(len(exe_file_list))
 	os.chdir(exeDir)
	# beging to loop everyone's code submission
	for exe_file in exe_file_list:

		file_exe = exe_file
		case_result = []
		score = 0
		time_used = []
		case_passed = 0
		case_error = 0
		case_tle = 0
		case_wrong = 0
		language =  'N/A'
		compile_success = True
		state = ''

		cmd = []

		if '.exe' in exe_file and ((exe_file[:-4] + '.cpp') in exe_file_list or \
				(exe_file[:-4] + '.c' in exe_file_list)):
				#exclude .exe file that was built previously
				continue

		elif '.class' in exe_file and ((exe_file[:-6] + '.java') in exe_file_list):
				#exclude .class file that was built previously
				continue

		submit_total += 1
		print "---"*20
		print "{}.'{}'".format(submit_total,exe_file)

		if '.py' in exe_file:
			#pythnon2,3 auto running: py -2 xxxpy2.py or py -3 xxxpy3.py
			if 'py3' in exe_file or '3.' in exe_file \
			or '3' in exe_file.replace('32','').replace('q3','').replace('Q3','').replace('.3',''):
				cmd = [python3Dir,exe_file]
				language = "Python3"
			else:
				cmd = [python2Dir,exe_file]
				language = "Python2"

		elif '.class' in exe_file: # java: java -cp . xxx(.class)
			cmd = [javaDir,'-cp','.',exe_file.strip('.class')]
			language = "Java"

		elif '.exe' in exe_file:
			cmd = [exe_file]
			language = "C/C++"

		#feature auto-compile C/C++/Java begin
		elif '.c' == exe_file[-2:]:
 			language = "C"
			#'gcc -o xxx_c xxx.c' to build out a xxx_c.exe
			compile_cmd = [gccDir,'-std=c11','-o',exe_file.replace('.c',''),exe_file]
			p_compile = subprocess.Popen(compile_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,\
	 		stderr=subprocess.PIPE, shell=False)	

	 		p_compile.wait()
	 		err = p_compile.stderr.read()
	 		if 'error' not in err:
	 			err = ''

	 		if err == '':
	 			file_exe = exe_file.replace('.c','.exe')
	 			print "Successfully Compiled:'gcc -std=c11 -o {} {}'".format(file_exe.replace('.exe',''),exe_file)
	 			cmd = [file_exe]
	 		else:
	 			print "Compiled failed, error:"
	 			print err
	 			compile_success = False
	 			state = "Compile_Error"

		elif '.cpp' == exe_file[-4:]:
			language = "C++"
			#feature compile C/C++/Java begin
			#gcc -o xxx_c xxx.c to build out a xxx_c.exe
			compile_cmd = [gppDir,'-std=c++11','-o',exe_file.replace('.cpp',''),exe_file]
			p_compile = subprocess.Popen(compile_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,\
	 		stderr=subprocess.PIPE, shell=False)	
	 		p_compile.wait()

	 		err = p_compile.stderr.read()
	 		if 'error' not in err:
	 			err = ''
	 		if err == '':
	 			file_exe = exe_file.replace('.cpp','.exe')
	 			print "Successfully Compiled:'g++ -std=c++11 -o {} {}'".format(file_exe.replace('.exe',''),exe_file)
	 			cmd = [file_exe]
	 		else:
	 			print "Compiled failed, error:"
	 			print err
	 			compile_success = False

		elif '.java' in exe_file:
			language = "Java"
			#javac xxx.java build out a xxx.class
			compile_cmd = [javacDir,exe_file]
			p_compile = subprocess.Popen(compile_cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,\
	 		stderr=subprocess.PIPE, shell=True)	
	 		p_compile.wait()

	 		err = p_compile.stderr.read()
	 		if 'error' not in err:
	 			err = ''
	 		if err == '':
	 			file_exe = exe_file.replace('.java','.class')
	 			print "Successfully compiled '{}' to '{}'".format(exe_file, file_exe)
				#cmd = 'java' + ' -cp . ' + file_exe.strip('.class')
				cmd = ['java','-cp','.',file_exe.strip('.class')]
	 		else:
	 			print "Compiled failed, error:"
	 			print err
	 			compile_success = False
	 	#feature compile C/C++/Java end

		elif '.sh' in exe_file:
			#need to vi and :set fileformat=unix or else there is /r error
			cmd = ['bash',exe_file]
			language = "bash"


		else:
			print "error, {0} is not supported to run.".format(exe_file)
			language = exe_file.split('.')[1]
			case_result.append("'{}'".format(exe_file))
			case_result.append(language)
			case_result.append('0')
			case_result.append('N/A')
			case_result.append('Unsupport Error')
			case_result_list.append(case_result)

			continue

		case_result.append("{}".format(exe_file))
		case_result.append(language)

		if not compile_success:
			print ""
			case_result.append(str(score))
			case_result.append('N/A')
			case_result.append('Compile_Error')
			case_result_list.append(case_result)
			print ""
			continue

		#Just run case1 to load code into memory	
		for case in case_list:
			s_input = case[1]
			s_output = case[2]
			callProc(cmd, s_input, s_output, trial_run=True)
			break

		#felix beging to loop to check every cases in case_list
		for case in case_list:
			case_name = case[0]
			s_input = case[1]
			s_output = case[2]
			case_score = case[3]

			s = "'{0}'({1} points): ".format(case_name, case_score)
			print "%-30s"%s,
			start_time = time.clock()

			re,real_output,err = callProc(cmd, s_input, s_output)

			cost_time = int((time.clock() - start_time)*1000)

			#re != 1, the right result is prior to errors
			if err != '' and re != 1:
				print "Run Error:",
				print err
				case_error += 1

			elif cost_time > timeMsLimit and re == 1:
				print "Time limit Exceeded: %dms"%(cost_time)
				time_used.append(cost_time)
				case_tle += 1

			elif re == 0 and err == '':
				print "Wrong anwser. {}ms".format(cost_time)
				time_used.append(cost_time)
				case_wrong += 1
				if Run_In_Detail:
					print("Your output:\n{}".format(real_output))
					print("Expected:\n{}".format(s_output))

			elif re == 1 and cost_time < timeMsLimit:
				case_passed += 1
				score += case_score
				print "Passed! {0}ms".format(cost_time)
				time_used.append(cost_time)
			else:
				print "'DEBUG:It could not happen'"

		if len(time_used) == 0:
			run_time = 'N/A'
		else:
			run_time = sum(time_used)/len(time_used)

		print "'{}' Result: {}/{} passed, {}/{} points, average {}ms"\
		.format(exe_file,case_passed,case_total,score,score_total,run_time)

		case_result.append(str(score))
		case_result.append(str(run_time))
		if case_passed > 0 and case_passed < case_total:
			state += 'Passed:{}'.format(case_passed)
		if case_tle > 0:
			state += 'TLE:{}'.format(case_tle)
		if case_wrong > 0:
			state += 'Wrong:{}'.format(case_wrong)
		if case_error > 0:
			state += 'Error:{}'.format(case_error)
		if case_passed == case_total:
			state = "All {} cases passed!".format(case_total)
		case_result.append(state)
		case_result_list.append(case_result)
		print ""
	#end for for exe_file in exe_file_list:

	print "Summary"
	print "-"*90
	print "%-5s"%("Index"),
	print "%-35s"%("File_Name"),
	print "%-10s"%("Language"),
	print "%-10s"%("Score"),
	print "%-10s"%("Run_Time"),
	print "%-10s"%("State")

	pass_num = 0
	index = 0
	for item in case_result_list:
		if 'All' in item[4]:
			pass_num += 1
		index += 1
		print "%-5s"%(str(index)),
		#print "{}.".format(j),
		for i in range(len(item)):
			if i == 0:
				print "%-35s"%(item[i]),
			else:
				print "%-10s"%(item[i]),
		print
	print "-"*90

	print "{} submissions checked, {} passed.".format(submit_total,pass_num)

if __name__ == '__main__':

	n = raw_input("Run in detail? (y/n): ")
	if n == 'y' or n == 'Y':
		Run_In_Detail = True
	else:
		Run_In_Detail = False

	execTest()

