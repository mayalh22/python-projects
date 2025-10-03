from itertools import product


digits = '012345'


combinations = product(digits, repeat=6)


for combo in combinations:
    print(''.join(combo))
    
def filter_numbers(numbers):
    # Function to check if a number satisfies the conditions
    def is_valid_number(num):
        # Convert the number to a string to get individual digits
        str_num = str(num)
        
        # Count occurrences of digits 0 through 5
        counts = [str_num.count(str(digit)) for digit in range(6)]

        # Check if each digit matches its corresponding count
        return all(int(str_num[i]) == counts[i] for i in range(6))

    # Filter the numbers using the is_valid_number function
    return [num for num in numbers if is_valid_number(num)]

# Example usage
numbers = [combo]
filtered_numbers = filter_numbers(numbers)
print(filtered_numbers)