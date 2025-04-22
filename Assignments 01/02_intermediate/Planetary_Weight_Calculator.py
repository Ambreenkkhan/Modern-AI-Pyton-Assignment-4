"""
Planetary Weight Calculator
This program asks the user for their weight on Earth and the name of a planet.
It calculates and displays the equivalent weight on the selected planet.

"""
# Gravity constants relative to Earth
GRAVITY_MULTIPLIERS = {
    "Mercury": 0.376,
    "Venus": 0.889,
    "Mars": 0.378,
    "Jupiter": 2.36,
    "Saturn": 1.081,
    "Uranus": 0.815,
    "Neptune": 1.14
}

def main():
    # Ask user for Earth weight
    try:
        earth_weight_input = input("Enter a weight on Earth: ")
        earth_weight = float(earth_weight_input)
    except ValueError:
        print("Invalid input! Please enter a numeric value for weight.")
        return

    # Ask user for a planet name
    planet_input = input("Enter a planet: ")

    # Capitalize first letter, lowercase the rest to match dictionary keys
    planet = planet_input.capitalize()

    # Check if planet exists in our dictionary
    if planet in GRAVITY_MULTIPLIERS:
        gravity = GRAVITY_MULTIPLIERS[planet]
        planetary_weight = earth_weight * gravity
        rounded_weight = round(planetary_weight, 2)
        print("The equivalent weight on " + planet + ": " + str(rounded_weight))
    else:
        print("Invalid planet name! Please enter one of these:")
        for key in GRAVITY_MULTIPLIERS:
            print("- " + key)

# Run the program
if __name__ == "__main__":
    main()
