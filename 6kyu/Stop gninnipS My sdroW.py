def spin_words(sentence):
    lsos = sentence.split(' ') # LiSt Of Sentence
    oli = [] # Output LIst
    if len(lsos) == 1:
        return ''.join(lsos)
    for i in range(len(lsos)):
        if len(lsos[i]) < 5:
            oli.append(lsos[i])
        else:
            revls = [] # REVersed LiSt
            for j in range(len(lsos[i])-1, -1, -1): # or use reversed()
                oli.append(lsos[i][j])
            oli.append('')
    return ''.join(oli)
pass
print(spin_words("Welcome to Las Pollos Hermanos"))