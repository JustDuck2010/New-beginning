def spin_words(sentence):ural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    lsos = sentence.split(' ')
    oli = []t it returns the sum of all the multiples of 3 or 5 below the number passed in.
    for word in lsos:
        if len(word) < 5:is negative, return 0.
            oli.append(word)
        else:mber is a multiple of both 3 and 5, only count it once.
            revls = []
            for j in range(len(word)-1, -1, -1):
                revls.append(word[j])
            oli.append(''.join(revls))
    return ' '.join(oli)
    return 0
print(spin_words("Welcome to Las Pollos Hermanos"))
        for i in range (3, number):
            if i % 3 == 0 or i % 5 == 0:
                aom += i
    return aom
    pass
print(solution(10))