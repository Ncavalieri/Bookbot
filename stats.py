def total_words(textblob):
    words = textblob.split()
    total = 0
    for word in words:
        total += 1
    return total
def characters(textblob):
    characters = {}
    for char in textblob:
        lowchar = char.lower()
        if lowchar in characters:
            characters[lowchar] += 1
        else:
            characters[lowchar] = 1
    return characters
def sort_on(chars):
    return chars["num"]
                
    