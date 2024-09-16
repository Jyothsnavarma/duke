import unittest
from calculation import calculate


def read_test_cases():
    test_cases = []
    with open("unittest.txt", "r") as file:
        for line in file:
            parts = line.strip().split(", ")
            operation = parts[0]
            x = float(parts[1])
            y = float(parts[2])
            expected_result = parts[3]
            test_cases.append((operation, x, y, expected_result))
    return test_cases


class TestCalculatorFunctions(unittest.TestCase):

    def run_test_case(self, operation, x, y, expected_result):
        global result
        if operation == "addition":
            result = x+y

        elif operation == "subtraction":
            result = x-y

        elif operation == "multiplication":
            result = x*y

        elif operation == "division":
            if y == 0:
                result = "cannot divided by zero"

            else:
                result = x / y
                self.assertEqual(result, float(expected_result))

    def test_operations_from_file(self):
        test_cases = read_test_cases()
        for operation, x, y, expected_result in test_cases:
            with self.subTest(operation=operation, x=x, y=y):
                self.run_test_case(operation, x, y, expected_result)


if __name__ == '__main__':
    unittest.main()
