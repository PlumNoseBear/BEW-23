def find_shortest_longest_word(text):

    text = text.replace('\t',' ')
    text = text.replace('\n',' ')
    text = ''.join(filter(str.isprintable, text))

    words = text.split()
    if len(words) == 0:
        return (None, None)
    min_len = len(words[0])
    max_len = len(words[0])
    min_word = words[0]
    max_word = words[0]

    for word in words:
        if len(word) < min_len:
            min_len = len(word)
            min_word = word

        if len(word) > max_len:
            max_len = len(word) 
            max_word = word

    return (min_word, max_word)

print(find_shortest_longest_word(''))
print(find_shortest_longest_word('        '))
print(find_shortest_longest_word('\n\n\t'))
print(find_shortest_longest_word('hello\n\n\tsir'))
print(find_shortest_longest_word('hello there, general kenobi'))
print(find_shortest_longest_word('привет всем'))
print(find_shortest_longest_word('привет       всем'))