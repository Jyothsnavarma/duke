import sys

def take_numbers():
    numbers = []
    while True:
        try:
            num = int(input("Enter a number (0 to stop): "))
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return numbers

def take_words():
    words = []
    while True:
        word = input("Enter a word (END to stop): ")
        if word == "END":
            break
        if word.isalpha():
            words.append(word)
        else:
            print("Invalid input. Please enter a word (letters only).")
    return words

def main():
    numbers = take_numbers()
    words = take_words()

    # Sort numbers and words
    numbers.sort()
    words.sort()

    # Print numbers and words in ascending and descending order
    print("Numbers in ascending order:", numbers)
    print("Numbers in descending order:", numbers[::-1])
    print("Words in ascending order:", words)
    print("Words in descending order:", words[::-1])

if __name__ == "__main__":
    main()
