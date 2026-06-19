def to_camel_case(text):
    newtext = ''
    if len(text) == 0:
        return "An empty string was provided but not returned"
    artext = list(text)
    aretx = []
    i = 0
    while i < len(artext):
        if artext[i] != "_" and artext[i] != "-":
            aretx.append(artext[i])
        elif i < len(artext) - 1:
            aretx.append(artext[i+1].upper())
            i += 1
        i += 1
    return(''.join(aretx))
print(to_camel_case("the_stealth_warrior"))

'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior" '''