def longest_word(text):
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text=text.replace('\t',' ')
    text=text.replace('\n',' ')
    text =''.join(filter(str.isprintable, text))
    if len(text.replace(' ', '')) == 0:
      maxword, minword = None, None 
    else:
      maxword =max(text.split(), key=len)
      minword =min(text.split(), key=len)
    return print((minword,maxword))

