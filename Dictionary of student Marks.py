dict1 = {"Raj": 90, "Prasad": 80, "Umakant": 84, "Akash": 79}

sname= input("Enter the student's name: ")

if sname in dict1:
    print(sname+"'s marks:" ,dict1[sname])
else:
    print("student not found.")