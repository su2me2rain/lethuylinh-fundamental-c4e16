height = float(input('Enter your height in cm: '))/100
weight = float(input('Enter your weight in kg: '))
bmi = weight/(height*height)
if bmi < 16:
    print('You are severly underweighed.')
elif bmi < 18.5:
    print('You are underweighed.')
elif bmi < 25:
    print('You are normal.')
elif bmi < 30:
    print('You are overweighed.')
else:
    print('You are obese.')
