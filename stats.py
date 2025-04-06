def get_num_words(text):
    """
    Returns the number of words in the given text.
    """
    return len(text.split())

def count_characters(text):
    """
    Returns the number of characters in the given text.
    """
    text_dict = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in text_dict:
                text_dict[char] += 1
            else:
                text_dict[char] = 1
    
    entries = [{"letter": k, "count": v} for k, v in text_dict.items()]
    
    return entries