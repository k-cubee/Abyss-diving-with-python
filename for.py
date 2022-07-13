print("\033c")
rand = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in rand:
    sum = sum + i
print(sum)
# hi, this is a comment


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "K"
            else:
                translation = translation + "k"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter the word: ")))

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for j, supply in enumerate(supplies):
    print('Index {} in supplies is: {}'.format(str(j), supply))
