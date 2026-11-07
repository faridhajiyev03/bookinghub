procedure_start = int(input('Enter procedure start time: '))

procedure_lasting = int(input('Enter procedure last time: '))

total = procedure_start + procedure_lasting

if procedure_start < 9:
    print("Too early")
elif total > 18:
    print("Too late")
else:
    print("Accepted")