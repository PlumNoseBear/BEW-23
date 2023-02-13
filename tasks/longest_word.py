import re
def find_shortest_longest_word(text):

    text = text.strip()

    if not text:
        return None, None
    text=re.sub(r'\s+', ' ', text)
    words = re.split(r'\s+?', text)
    words.sort(key=lambda w:len(w))
    return words[0], words[1]
print(find_shortest_longest_word(''))
print(find_shortest_longest_word('        '))
print(find_shortest_longest_word('\n\n\t'))
print(find_shortest_longest_word('hello\n\n\tsir'))
print(find_shortest_longest_word('hello there, general kenobi'))
print(find_shortest_longest_word('привет всем'))
print(find_shortest_longest_word('привет       всем'))
