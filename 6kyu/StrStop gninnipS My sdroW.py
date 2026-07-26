def spin_words(sentence):
    print(sentence)
    words = sentence.split(' ')
    str = ''
    for i in range (len(words)):
        if len(words[i]) >= 5:
            str += words[i][::-1]
        else:
            str += words[i]
        if i != len(words) - 1:
            str += ' '
    return str
print(spin_words("Welcome to Las Pollos Hermanos"))