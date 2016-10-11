"""
Takes in a phone number, and returns all the possible combinations of words
that could be made from the letters associated with the number on the keypad
"""
KEYPAD = {
            '1' : ['1'],
            '2' : ['A', 'B', 'C'],
            '3' : ['D', 'E', 'F'],
            '4' : ['G', 'H', 'I'],
            '5' : ['J', 'K', 'L'],
            '6' : ['M', 'N', 'O'],
            '7' : ['P', 'Q', 'R', 'S'],
            '8' : ['T', 'U', 'V'],
            '9' : ['W', 'X', 'Y', 'Z'],
            '0' : ['0']
        }

def phone_combinations(phonenumber):
    result = ['']
    for char in phonenumber:
        letters = KEYPAD[char]
        result = [prefix + letter for prefix in result for letter in letters]
    return result



print phone_combinations('723')