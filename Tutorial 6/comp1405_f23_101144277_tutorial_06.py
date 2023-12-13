#Tutorial 6 by Prayanshu Narayan S#101144277




def capitalVowelsIte(char_list: list) -> list:
    vowels = 'aeiou'
    for i in range(len(char_list)):
        if char_list[i].lower() in vowels:
            char_list[i] = char_list[i].upper()
    return char_list


def capitalVowelRec(char_list: list)-> list:
    vowels = 'aeiou'
    # Base case: if char_list is empty, return an empty list
    if not char_list:
        return []

    # Process the first character of the list
    first_char = char_list[0].upper() if char_list[0].lower() in vowels else char_list[0]

    # Recursive step: apply the function to the rest of the list and concatenate the first character
    return [first_char] + capitalVowelRec(char_list[1:])



    
    
def main():
    # Sample list of characters
    chars = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
    
    #a list called char alphabet with all the letters of the alphabet
    char_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                     'p','q','r','s','t','u','v','w','x','y','z']

    # Using the iterative function
    capitalized_chars_iterative = capitalVowelsIte(chars)
    print('Iterative:', capitalized_chars_iterative)

    # Using the recursive function
    capitalized_chars_recursive = capitali=capitalVowelRec(chars)
    print('Recursive:', capitalized_chars_recursive)

    #the iterative function for the alphabet
    capitalized_chars_iterative = capitalVowelsIte(char_alphabet)
    print('Alphabet test Iterative 2:', capitalized_chars_iterative)
    
    #the recursive function for the alphabet
    capitalized_chars_recursive = capitalVowelRec(char_alphabet)
    print('Alphabet test Recursive 2:', capitalized_chars_recursive)
    
main()