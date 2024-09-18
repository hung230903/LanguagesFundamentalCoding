age = input("Your age: ")
age = int(age)

is_con_nit = False #default #initialise the variable

if age < 10:
	is_con_nit = True

if is_con_nit :
	print("con nit")
elif age == 18:
	print("18 tuoi tre trau")
elif age < 18:
	print("Tre trau")
	if (age >=15 and age <= 17) or age == 20:
		print("Sieu tre trau")
else:
	print("nguoi lon")