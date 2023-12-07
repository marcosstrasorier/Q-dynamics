"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""

def to_camel_case(text):
    text = text.replace("-", " ").replace("_", " ")
    text = text.split(" ")
    for i in range(len(text)):
        if i == 0:
            if text[i] == text[i].lower():
                text[i] = text[i]
            else:
                text[i] = text[i].capitalize()
        else:
            text[i] = text[i].capitalize()
    return "".join(text)

print(to_camel_case("the-stealth-warrior"))
print(to_camel_case("The_Stealth_Warrior"))
print(to_camel_case("The_Stealth-Warrior"))