def my_split(inputsentence, sep):
    # Initialize an empty list to store the result
    result = []
    # Initialize an empty string to accumulate characters between separators
    word = ''
    # Iterate through each character in the input sentence
    for char in inputsentence:
        # If the character is not the separator, add it to the current word
        if char != sep:
            word += char
        # If the character is the separator, add the current word to the result list
        # and reset the word to an empty string
        else:
            result.append(word)
            word = ''
    # After the loop, add the last word to the result list (if any)
    if word:
        result.append(word)
    
    return result

def my_join(list, sep):
    newlist = ''
    for i in range(len(list)):
        newlist += list[i]

        if i < len(list) - 1:
            newlist += sep
    
    return newlist

sentence = input('Please enter a sentence: ')
print(my_join(my_split(sentence, ' '),','))
print(my_join(my_split(sentence, ' '),'\n'))


