def is_text_panlindromic():
    """ check to see if inputted text is a palindrome """
    text = input("Input some text: ") # ask for user input

    import re # needed to use the 're.sub(..)' function

    # build reverse_text:
    reverse_text = ""
    i = -1
    while i >= -len(text):
        # breakpoint() used to debug line by line only available in python 3.7+
        reverse_text = reverse_text + text[i]
        i -= 1
    
    # used 're.sub(..)' function to strip out punctuation and spaces
    reverse_text = re.sub(r'[^A-Za-z]', '', reverse_text)
    forward_text = re.sub(r'[^A-Za-z]', '', text)

    # test if reverse_text matches user-inputted text
    if reverse_text.lower() == forward_text.lower():
        return text + " is a palindrome"
    else:
        return text + " is not a palindrome"

print(is_text_panlindromic())

# Boom!
# palindrome.py: Determines if a text is palindromic
#   it_works_for_even_numbers:                       [PASS]
#   it_works_for_odd_numbers:                        [PASS]
#   it_works_for_simple_values:                      [PASS]
#   it_works_for_complete_sentences:                 [PASS]
#   it_works_for_complex_sentences:                  [PASS]
#   it_works_for_multiple_sentences:                 [PASS]
#   it_works_for_non_palindromes:                    [PASS]
# =========================================================
# Tests:    7 | Passed:   7 | Failed:   0