import pymsgbox
h = open('password.txt', 'r')
content = h.readlines()
key = ''.join(str(e) for e in content)

chance_current = 4
while chance_current <= 4:
	response = pymsgbox.password("You have only 4 chances to enter key password \n Enter the current password \t{}".format(chance_current))
	chance_changed = 3
	if response == key :

			while chance_changed <= 3:
				changed_password = pymsgbox.password("Enter the new password")
				retype_password  = pymsgbox.password("Re-enter the password")
				if changed_password == retype_password :
					password = str(changed_password)
					#write password in the file
					w = open('password.txt','w')
					w.write(password)
					w.close()
					break
				else :
					pymsgbox.alert("Your password is incorrect{}".format(chance_changed),timeout= 2000)
					if chance_changed == 0 :
						break
					else :
						chance_changed -= 1


			break
	else:
		pymsgbox.alert("You typed wrong password ",timeout=2000)
		if chance_current == 0 :
			break
		else:
			chance_current -= 1
