//Write a program that will ask the user to input a list of integer tuples. Ask for another integer value and assign it to K. Output the tuple that are visible by K

def get_integer_tuples():
    tuples = []
    while True:
        try:
            input_str = input("Enter a tuple of integers (comma-separated, or type 'done' to finish): ")
            if input_str.lower() == 'done':
                break
            tuple_values = tuple(map(int, input_str.split(',')))
            tuples.append(tuple_values)
        except ValueError:
            print("Invalid input. Please enter comma-separated integers.")

    return tuples

def filter_tuples_by_divisibility(tuples_list, k):
    divisible_tuples = [t for t in tuples_list if all(x % k == 0 for x in t)]
    return divisible_tuples

if __name__ == "__main__":
    print("Enter integer tuples separated by commas. Type 'done' to finish.")
    tuples_input = get_integer_tuples()

    k = int(input("Enter an integer value for K: "))

    divisible_tuples = filter_tuples_by_divisibility(tuples_input, k)

    if divisible_tuples:
        print(f"Tuples divisible by {k}:")
        for t in divisible_tuples:
            print(t)
    else:
        print(f"No tuples are divisible by {k}.")

