# Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). 
# Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, 
# he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, 
# check out how contractions are expected to be in the example below.

# Your task is to convert strings to how they would be written by Jaden Smith. 
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally 
# typed them.

def j_string(string):
    # list comp - loop thru split string, titlecase each word - join list of words to string - separate w space
    # return " ".join([word.capitalize() for word in string.split()])
    # return " ".join([word[0].upper()+word[1:] for word in string.split()])

    string_lst = string.split()
    for i in range(len(string_lst)):
        string_lst[i] = string_lst[i].capitalize()
    return " ".join(string_lst)

print(j_string("i have to go to the mall with my mum tomorrow! Aren't you excited?"))