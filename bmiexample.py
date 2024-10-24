# create a program to calculate your BMI

def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    # Input weight and height
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Determine the BMI category
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        # Display the result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Please enter valid numbers for weight and height.")


# Run the program
if __name__ == "__main__":
    calculate_bmi()
