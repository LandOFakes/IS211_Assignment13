def fibonnaci(n):
  """
  Calculates the nth Fibonacci number recursively.

  Args:
    n: The position in the Fibonacci sequence (integer).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 0:
    print("Input should be a positive integer.")
    return None
  elif n == 1:
    return 0 # First Fibonacci number is 0
  elif n == 2:
    return 1 # Second Fibonacci number is 1
  else:
    # The nth Fibonacci number is the sum of the (n-1)th and (n-2)th [cite: 9]
    return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a, b):
  """
  Calculates the greatest common divisor (GCD) of two integers using Euclid's algorithm recursively. [cite: 12, 14]

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The greatest common divisor of a and b.
  """
  if b == 0:
    # Base case: if b is 0, the GCD is a [cite: 15]
    return a
  else:
    # Recursive step: gcd(a, b) = gcd(b, a % b) [cite: 13]
    return gcd(b, a % b)

def compareTo(s1, s2):
  """
  Compares two strings recursively. [cite: 16, 17]

  Args:
    s1: The first string.
    s2: The second string.

  Returns:
    - A negative number if s1 < s2
    - 0 if s1 == s2
    - A positive number if s1 > s2
  """
  # Base case: If both strings are empty, they are equal
  if not s1 and not s2:
    return 0
  # Base case: If one string is empty and the other is not
  if not s1:
    return -1 # s1 is shorter (less than s2)
  if not s2:
    return 1  # s1 is longer (greater than s2)

  # Compare the first characters
  if s1[0] < s2[0]:
    return -1
  elif s1[0] > s2[0]:
    return 1
  else:
    # If first characters are equal, compare the rest of the strings recursively
    return compareTo(s1[1:], s2[1:])

# Example Usage (optional - you can add this to test your functions)
if __name__ == "__main__":
  print("Fibonacci Sequence:")
  print(f"fibonnaci(10) = {fibonnaci(10)}") # Expected output: 34

  print("\nGreatest Common Divisor (GCD):")
  print(f"gcd(48, 18) = {gcd(48, 18)}") # Expected output: 6
  print(f"gcd(101, 103) = {gcd(101, 103)}") # Expected output: 1

  print("\nString Comparison:")
  print(f"compareTo('apple', 'banana') = {compareTo('apple', 'banana')}") # Expected output: negative number
  print(f"compareTo('cherry', 'cherry') = {compareTo('cherry', 'cherry')}") # Expected output: 0
  print(f"compareTo('date', 'apple') = {compareTo('date', 'apple')}")   # Expected output: positive number
  print(f"compareTo('apple', 'apples') = {compareTo('apple', 'apples')}") # Expected output: negative number
  print(f"compareTo('apples', 'apple') = {compareTo('apples', 'apple')}") # Expected output: positive number
