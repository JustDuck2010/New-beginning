def get_count(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    q = 0
    for i in sentence:
        if i.lower() in vowels:
            q += 1
    return q
    pass
print(get_count('abimba'))