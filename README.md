# String and Number Conversion Challenge

## Your Task

You need to create a specific sentence using only the provided variables, type conversion, and string concatenation. You may not add any additional string or numeric literals.

### The Goal
Create a variable called `sentence` that contains exactly this text:
```
55 robots were built today
```

### Starting Variables
You have these variables to work with:
```python
num_str_1 = "42"      # A string containing a number
num_str_2 = "13"      # A string containing a number
num_str_3 = "7"       # A string containing a number (you might not need this!)
word_1 = "robots"     # A word
word_2 = "built"      # A word
word_3 = "today"      # A word
```

### Rules
1. You can convert strings to numbers using `int()`
2. You can convert numbers back to strings using `str()`
3. You can add strings together using `+`
4. You can add numbers together using `+`
5. You CANNOT type any numbers or words directly in your code
6. You CANNOT add any new string literals (even spaces!)
7. You must use the provided variables to create the sentence

### Steps to Success
1. Look at the target sentence and identify which numbers need to be added
2. Convert the right string numbers to integers
3. Add the numbers
4. Convert the sum back to a string
5. Figure out how to add spaces between words (hint: there might be spaces already in some variables!)
6. Combine everything in the right order

### Example (with different words)
If you had:
```python
num_1 = "5"
num_2 = "3"
word_1 = " cats"  # Notice the space!
```
And wanted to make "8 cats", you would do:
```python
result = str(int(num_1) + int(num_2)) + word_1
```

## Testing Your Solution
Your code will be tested to make sure:
1. You created a variable called `sentence`
2. Your sentence matches exactly: "55 robots were built today"
3. You didn't add any extra strings or numbers
4. You used the provided variables correctly

## Need Help?
- Check that your capitalization matches exactly
- Make sure you have spaces in the right places
- Remember that `int()` converts strings to numbers
- Remember that `str()` converts numbers back to strings
- Look carefully at the provided variables - some might have hidden spaces!

Good luck! 🚀
