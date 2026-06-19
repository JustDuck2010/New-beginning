def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    sewivo = ''
    for i in sentence:
        if i.lower() not in vowels:
            sewivo += i
    return sewivo
    pass

print(get_count('abimba'))