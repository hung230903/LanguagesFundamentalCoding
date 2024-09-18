
def ask_yes_no(prompt):
	while True:
		answer = input(prompt)
		if answer == "yes" or answer == "Yes":
			return True
		elif answer == "No" or answer == "no":
			return False
		else:
			continue
 
def print_height_info(is_male, height_feet):
	if is_male:
		if height_feet > 5.9:
			print("You are ", end = " ")
			for i in range (10):
				print("very", end = " ")
			print(" tall as a man")
		elif height_feet > 5.7:
			print("You are tall as a man")
		else:
			print("You are short as a man")
	else:
		if height_feet > 5.7: 	
			print("You are ", end = " ")
			i = 0
			while i < 10:
				print("very", end = " ")
				i += 1
			print(" tall as a girl")
		elif height_feet > 5.25:
			print("You are tall as a girl")
		else:
			print("You are short as a girl")
  

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet, 2)
	return feet

def calc_age(year_born):
	CURRENT_YEAR = 2023
	return CURRENT_YEAR - year_born

def ask_person_info():
	first_name = input("Your first name: ")
	last_name = input("Your last name: ")
	year_born = int(input("When you were born: "))
	height_meter = float(input("Your height in meter: "))
	is_male = ask_yes_no("Are you male(Yes/No): ")
	is_Vietnamese = ask_yes_no("Are you form Vietnam: ")
	return first_name, last_name, year_born, height_meter, is_male, is_Vietnamese


def print_person_info(first_name, last_name, age, height_feet, is_male, is_Vietnamese):
	CURRENT_YEAR = 2023
	print("--------------")
	print("Your name is: " + first_name + " " + last_name)
	print("You are {0} in {1}".format(age, CURRENT_YEAR) )
	print("You are " + str(height_feet) + " feet tall")
	print_height_info(is_male, height_feet)

	if is_Vietnamese:
		print("You are from Vietname")
	else:
		print("You are not form Vietnam ")



def main():
	first_name, last_name, year_born, height_meter, is_male, is_Vietnamese = ask_person_info()
	age = calc_age(year_born)
	height_feet = convert_meter_to_feet(height_meter)
	print_person_info(first_name, last_name, age, height_feet, is_male, is_Vietnamese)

main()