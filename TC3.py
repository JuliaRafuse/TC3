#Student Name: Julia   
#Program Title: Grade point calculator 
#Description: TC#3 

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    
    #Commands:
    print("Grade Point Calculator")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.")
    
    # Letter grade
    letter_grade = input("Please enter a letter grade: ").upper()
    # Modifier input
    modifier = input("Please enter a modifier (+, - or nothing): ")

    # Initialize numeric value
    numeric_value = 0.0

    # Letter grades
    if letter_grade == 'A':
        numeric_value = 4.0
    elif letter_grade == 'B':
        numeric_value = 3.0
    elif letter_grade == 'C':
        numeric_value = 2.0
    elif letter_grade == 'D':
        numeric_value = 1.0
    elif letter_grade == 'F':
        numeric_value = 0.0
    else:
        print("You entered an invalid letter grade.")
        print("The numeric value is: 0.0")
        return

    # Modifiers
    if modifier == "+" and letter_grade != 'A':  # A+ remains at 4.0
        numeric_value += 0.3
    elif modifier == "-":
        numeric_value -= 0.3
    elif modifier not in ["+", "-", ""]:
        print("You entered an invalid modifier.")
        return

    # make sure the value doesn't exceed 4.0
    if numeric_value > 4.0:
        numeric_value = 4.0

    # Print the numeric value
    print(f"The numeric value is: {numeric_value:.1f}")

if __name__ == "__main__":
    main()
