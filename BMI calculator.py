def calculate_bmi(weight, height):
    """
    Calculate BMI based on weight (kg) and height (m).
    """
    return weight / (height ** 2)

def classify_bmi(bmi):
    """
    Classify BMI into categories (underweight, normal, overweight, obese).
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def get_positive_float(prompt):
    """
    Get a positive float from user input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Welcome to the BMI Calculator")

    # Input weight and height from the user
    weight = get_positive_float("Enter your weight in kilograms: ")
    height = get_positive_float("Enter your height in meters: ")

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Classify BMI
    category = classify_bmi(bmi)

    # Display the results
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
