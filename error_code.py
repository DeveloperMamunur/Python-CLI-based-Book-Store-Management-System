import re

class ErrorCode:
    def error_str(self, item):
        # Validates if the input is a valid string containing only letters and spaces.
        # Raises an error if numbers or special characters are found.

        item = item.strip()
        
        if not item:
            raise Exception("Input cannot be empty. It should be a valid string.")
        
        pattern = r'^[A-Za-z\s]+$'  # Only letters and spaces allowed
        if not re.match(pattern, item):
            raise Exception("Invalid input: Only letters and spaces are allowed.")
        
        return item
    
    def error_negative(self, item):
        #Ensures that the given number is positive (greater than zero).
        #Raises an error if it is negative or zero.
        if not isinstance(item, (int, float)):
            raise Exception("Invalid input: Value should be a number.")
        
        if item <= 0:
            raise Exception(f"Invalid input: {item} is not allowed. It should be a positive number.")
        
        return item