# 1. Create a script named datatypes_demo.py.

def main():
    # 2. Declare variables of different types: int, float, string, boolean.
    my_int = 25
    my_float = 4.5
    my_string = "Python"
    my_bool = True

    # 3. Print the type of each variable using type().
    # We use .__name__ to show a clean type name instead of <class 'type'>
    print("--- Variable Types ---")
    print(f"Value: {my_int}, Type Name: {type(my_int).__name__}")
    print(f"Value: {my_float}, Type Name: {type(my_float).__name__}")
    print(f"Value: {my_string}, Type Name: {type(my_string).__name__}")
    print(f"Value: {my_bool}, Type Name: {type(my_bool).__name__}")
    print("-" * 20)

    # 4. Perform arithmetic operations using numeric variables.
    sum_result = my_int + my_float
    print(f"Arithmetic: {my_int} + {my_float} = {sum_result}")

    # 5. Convert string input to integer and float using type casting.
    # 6. Handle invalid input using basic error handling.
    print("\n--- Input & Type Casting ---")
    user_input = input("Enter a numeric value: ")

    try:
        # 9. Add clear comments explaining each conversion.
        # Explicitly creating an integer object from string data
        val_int = int(user_input) 
        # Explicitly creating a float object from string data
        val_float = float(user_input)

        # 7. Concatenate strings and numbers properly.
        # Option A: Manual casting to string
        print("Concatenation: The number is " + str(val_int))
        # Option B: F-string (Internally handles the string conversion)
        print(f"F-String display: {val_float}")

    except ValueError:
        print("Error: Invalid input! Input must be numeric.")

    # 8. Demonstrate dynamic typing by reassigning variable values.
    # This proves the variable name is just a pointer to an object.
    dynamic_var = 100
    print(f"\nDynamic Typing: Pointer initially points to: {type(dynamic_var).__name__}")
    dynamic_var = "Now I am a string"
    print(f"Dynamic Typing: Pointer now points to: {type(dynamic_var).__name__}")

if __name__ == "__main__":
    main()