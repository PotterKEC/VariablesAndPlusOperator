import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def test_create_sentence():
    # Import and get the sentence from student's code
    from assignment import num_str_1, num_str_2, num_str_3, word_1, word_2, word_3
    
    # The student needs to create this exact sentence: "55 robots were built today"
    # They must convert num_str_1 and num_str_2 to integers, add them, 
    # convert back to string, and combine with the other variables
    
    # Test each component separately
    try:
        num_sum = int(num_str_1) + int(num_str_2)  # Should be 55
        assert num_sum == 55, "The sum of num_str_1 and num_str_2 should be 55"
    except ValueError:
        assert False, "Make sure you're converting strings to numbers correctly"
    
    # Test that they've created a variable called 'sentence' with the correct value
    try:
        from assignment import sentence
        assert isinstance(sentence, str), "The sentence variable should be a string"
        expected = "55 robots were built today"
        assert sentence == expected, f"Expected '{expected}', but got '{sentence}'"
    except ImportError:
        assert False, "Make sure you create a variable called 'sentence'"
