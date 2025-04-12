# Circle Calculator
# Circumference and Area

# Imports
import math

# Title
print('------------------------------------------------------------------------------')
print('Circle Calculator')
print('------------------------------------------------------------------------------')
print('What would you like to do?:')
print('------------------------------------------------------------------------------')
print('[1] Calculate the Circumference of a Circle')
print('[2] Calculate the Area of a Circle')
print('------------------------------------------------------------------------------')
print('')

# Choose What you would like to do
while True:
    Answer = input('Please choose 1 or 2: ')
    
    # Calculate the Circumference of a Circle
    if Answer == '1':

        Chosen_Calculation = 'Circumference'

        # Choosing Radius or Diameter
        print('')
        print('------------------------------------------------------------------------------')
        print('What are you calculating the Circumference of a Circle from?:')
        print('------------------------------------------------------------------------------')
        print('[1] Radius')
        print('[2] Diameter')
        print('------------------------------------------------------------------------------')
        print('')

        # Choose What you would like to do
        while True:
            method_choice = input('Please choose 1 or 2: ')
                
            # Using Radius
            if method_choice == '1':
                
                # Inputs
                print('')
                while True:
                    try:
                        Radius = float(input('What is your radius in cm?: '))
                        break
                    
                    # If they do not enter a valid number
                    except ValueError:
                        print('That is not a valid number!')

                # Calculation
                Circumference = 2 * math.pi * Radius
                Final_Answer = Circumference
                Is_Squared = ''

                break
            
            # Using Diameter
            elif method_choice == '2':
                
                # Inputs
                print('')
                while True:
                    try:
                        Diameter = float(input('What is your Diameter in cm?: '))
                        break
                    
                    # If they do not enter a valid number
                    except ValueError:
                        print('That is not a valid number!')

                # Calculations
                Converted_Diameter = Diameter / 2
                Circumference = 2 * math.pi * Converted_Diameter
                Final_Answer = Circumference
                Is_Squared = ''

                break
            
            # If 1 or 2 was not entered
            else:
                print('Please enter either 1 or 2.')

        break

    # Calculate the Area of a Circle
    elif Answer == '2':
        
        Chosen_Calculation = 'Area'

        # Choosing Radius or Diameter
        print('')
        print('------------------------------------------------------------------------------')
        print('What are you calculating the Area of a Circle from?:')
        print('------------------------------------------------------------------------------')
        print('[1] Radius')
        print('[2] Diameter')
        print('------------------------------------------------------------------------------')
        print('')

        # Choose What you would like to do
        while True:
            method_choice = input('Please choose 1 or 2: ')
                
            # Using Radius
            if method_choice == '1':
                
                # Inputs
                print('')
                while True:
                    try:
                        Radius = float(input('What is your radius in cm?: '))
                        break
                    
                    # If they do not enter a valid number
                    except ValueError:
                        print('That is not a valid number!')

                # Calculations
                Squared_Radius = Radius ** 2
                Area = math.pi * Squared_Radius
                Final_Answer = Area
                Is_Squared = '^2'

                break
            
            # Using Diameter
            elif method_choice == '2':
                
                # Inputs
                print('')
                while True:
                    try:
                        Diameter = float(input('What is your Diameter in cm?: '))
                        break
                    
                    # If they do not enter a valid number
                    except ValueError:
                        print('That is not a valid number!')

                # Calculations
                Converted_Diameter = Diameter / 2
                Squared_Converted_Diameter = Converted_Diameter ** 2
                Area = math.pi * Squared_Converted_Diameter
                Final_Answer = Area
                Is_Squared = '^2'

                break
            
            # If 1 or 2 was not entered
            else:
                print('Please enter either 1 or 2.')

        break

    # If 1 or 2 was not entered
    else:
        print('Please enter either 1 or 2.')

print('')
print('------------------------------------------------------------------------------')
print(f'You chose to Calculate the {Chosen_Calculation} of a circle.')
print(f'Your Answer is: {round(Final_Answer, 3)} cm{Is_Squared} rounded to 3 D.P.')
print('------------------------------------------------------------------------------')
print('')
input('Press the Enter Key to Exit...')