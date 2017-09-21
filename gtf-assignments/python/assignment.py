# row 1 of our CSV file is room names prefaced by an empty space
office_names = ['', 'SCH 158', 'SCH 158A', 'SCH 158B', 'SCH 161', 'SCH 221', 'SCH 232']
# the rest of the rows give a name followed by preferences corresonding to the first row
initial_csv = {
	'Brock Baines', [,,2,3,1,,]
	'Elizabeth Balskus', [,,,,,,]
	'Larry Busk', [,,3,,1,,2]
	'Anna Cook', [,,2,1,3,,]
	'Lauren Eichler', [,,1,2,3,,]
	'Martina Ferrari', [,,,2,3,,1]
	'Devin Fitzpatrick', [,2,1,3,,,]
	'Cameron Gamble', [,,,,,,]
	'Billy Goehring', [,,,,,,]
	'Jon LaRochelle', [,3,1,,,,2]
	'Sarah McLay', [,,,2,1,,3]
	'Mary McLevey', [,,,,,,]
	'Jane Nam', [,3,1,,,2,]
	'Maggie Newton', [,3,1,2,,,]
	'Juan Ospina', [,,,,,,]
	'Claire Pickard', [,,3,,2,,1]
	'Eli Portella', [,,,,,,]
	'Oscar Ralda', [,,,,,,]
	'Kaja Rathe', [,,2,3,,,1]
	'Bonnie Sheehey', [,,3,2,1,,]
	'Paul Showler', [,,,3,2,,1]
	'Rebekah Sinclair', [,,1,2,3,,]
	'Harris Smith', [,3,1,2,,,]
	'Amie Zimmer', [,,2,1,3,,]
}

initial_csv = {
	'Brock Baines': ',,2,3,1,,',
	'Elizabeth Balskus': ',,,,,,',
	'Larry Busk': ',,3,,1,,2',
}

# turn defintion string (eg ,,231,,) into array
preference_list = {}
for key in initial_csv:
  preference_list[key] = initial_csv[key].split(',')
  
# match preferences to rooms
for key in preference_list:
  print(key)
  for i in range (0, len(office_names)):
    if preference_list[key][i] != '': # if preference exists
      print(preference_list[key][i])
      print(office_names[i])
