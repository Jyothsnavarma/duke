def identify_pattern(sequence):
    elements = sequence.split(',')

    if all(elem.isnumeric() for elem in elements):
        difference = int(elements[1]) - int(elements[0])
        return lambda x: int(elements[-1]) + difference * x
    elif all(elem.isalpha() for elem in elements):
        return lambda x: chr(ord(elements[-1]) + x)
    elif elements[:-1].isalpha() and elements[-1].isnumeric():
        prefix = ''.join(elements[:-1])
        return lambda x: f"{prefix}{int(elements[-1]) + x}"


def main():
    user_input = input("Enter a sequential pattern: ").strip()

    next_number = identify_pattern(user_input)

    if next_number:
        count = int(input("Enter the count of numbers to emit: "))
        result = [next_number(i) for i in range(1, count + 1)]
        print("Next numbers in the sequence:", result)
    else:
        print("Invalid input. Please enter a valid sequential pattern.")


if __name__ == "__main__":
    main()
