
# Imports
import getpass

# Body
def password_prompt():
	"""prompt the user to set-up a password"""
	# password = input("Please enter a password or finish to end: ")
	user_password = ''
	while user_password != 'finish':
		print("Please enter a password or finish to end. ")
		user_password = getpass.getpass()
		if user_password == 'finish':
			break
		elif  (' ' or '	' or '') in user_password:
			print('Space and tabs should not be used as password')
			continue
		else:
			total_length, total_lower, total_upper, total_digit, total_specialcharacter = password_check(user_password)
			pw_score = password_feedback(total_length, total_lower, total_upper, total_digit, total_specialcharacter)
			pw_strength(pw_score)
			iscommon, count = search_password(user_password)
			if iscommon: 
				print('The password is common.')
			print('Number of comparison: {}'.format(count))

def password_check(user_password):
	"""Check the component of user password : 
	1 upper, 1 lower, 1 digit, 1 non-letter non-digit, 6 characters"""

	password = str(user_password)
	total_length = len(password)
	total_lower = 0
	total_upper = 0
	total_digit = 0
	total_specialcharacter = 0

	# count the lowercase letters
	for character in password:
		if character.islower() == True:
			total_lower += 1
	# count the upper case letters
		elif character.isupper() == True:
			total_upper += 1
	# to check if there is only digits
		elif character.isdigit() == True:
			total_digit += 1	 
	# to check if there is any special charaters
		elif (33 <= ord(character) <= 47) or (58 <= ord(character) <= 64) or  (91 <= ord(character) <= 96) or ( 123 <= ord(character) <= 126):
			total_specialcharacter += 1
		
	return total_length, total_lower, total_upper, total_digit, total_specialcharacter

def password_feedback(total_length, total_lower, total_upper, total_digit, total_specialcharacter):
	"""Give feed back of the password and output which conditions are met and not met.	
	 """
	pw_score = 0
	# check the length of the password is at least 6
	if total_length < 6:
		print('You need at least 6 characters.')
	else:
		pw_score +=1 

	# feedback on the result of counting upper and lower cases
	if total_lower == 0:
		print('You need at least one lowercase letter.')
	if total_upper == 0:
		print('You need at least one uppercase letter.')
	if total_upper >= 1 and total_lower >= 1:
		pw_score += 1 

	# feedback on the result of counting digit
	if total_digit <= 0:
		print('You need at least 1 digit.')
	else:
		pw_score += 1

	# feedback on the result of counting special character
	if total_specialcharacter <= 0:
		print('You need a special character.')
	else:
		pw_score += 1
	return pw_score

def pw_strength(pw_score):
	"""# use the password score to identify the pw strength
	if pw_score : 0 : very weak, 1: weak , 2: medium strength, 
	                3 high medium strength, 4 strong"""
	if pw_score == 0:
		print('Password is very weak.')
	elif pw_score == 1:
		print('Password is weak.')
	elif pw_score == 2:
		print('Password is medium strength.')
	elif pw_score == 3:
		print('Password is high medium strength.')
	elif pw_score == 4:
		print('Passowrd is strong.')		


# Part (2)
def search_password(user_password):
	""" check whether the user's password 
	 is on the list of common passwords or not."""
	
	# getting all the passwords from the file
	lines = []
	count = 0 
	try:
		with open('common.txt', 'r') as fin:
			for line in fin:
				lines.append(line.strip())
	except:
		print('The common.txt is not present.')
	# change all capital letters in the users password to lower case letter
	check_pw = str(user_password)
	pw = check_pw.lower()

	# binary search algorithm in class  
	low = 0
	high = len(lines) - 1
	while low <= high:
		mid  = (low + high) // 2
		item = lines[mid]
		if pw == item:
			count += 1
			return True, count 

		elif pw < item:
			high = mid - 1
			count += 1
		else:
			low = mid + 1
			count += 1
	
	return False, count

################################################################################
def main():

	password_prompt()


if __name__ == '__main__':
	main()












































