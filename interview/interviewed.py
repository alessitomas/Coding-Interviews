from collections import defaultdict

def is_permutation_of_palindrome( string : str):
    string_new_lst = []
    
    for c in string:
        if c.isalpha():
            string_new_lst.append(c.lower())
   
    string_new = "".join(string_new_lst)


    char_freq = defaultdict(int)

    for c in string_new:
        char_freq[c] =  char_freq[c] + 1
    
    count_char_with_odd_freq = 0
    
    for _, v in char_freq.items():
            if v % 2 == 1:
                count_char_with_odd_freq += 1
        
    odd_length = len(string_new) % 2  == 1

    if count_char_with_odd_freq == 0:
        if odd_length:
                return False
        else:
            return True
    elif count_char_with_odd_freq == 1 and odd_length:
        return True
    # more than 1 char with odd freq, count_char_with_odd_freq == 1 and even_length
    else:
        return False