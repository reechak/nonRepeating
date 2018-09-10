# nonRepeating
# Find Non repeating characters in a string
# Use Hashmap and Loop through each character. Add character as key and count of everytime the character appears as value .
def non_repeating(given_string):
    char_count = {}
    for c in given_string:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    for c in given_string:
        if char_count[c] == 1:
            return c
    return None
