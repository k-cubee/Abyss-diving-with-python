from random import randint

print("\033c")


class human:
    def __init__(self, name, age, height, gender):
        self.name = name
        self.age = age
        self.height = height
        self.gender = gender


kCube = human("Kcube", 15, "165 cm", "male")
print(kCube.name)
randNumGenerator = randint(0, 11)
print(randNumGenerator)


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


qPrompts = ["a", "b", "c"]

questions = [
    Question(qPrompts[0], 1),
    Question(qPrompts[1], "p"),
    Question(qPrompts[2], 3)
]


def test(questions):
    score = 0
    for question in questions:  # question has is basically the position of the array
        answer = input(question.prompt + ": ")
        if answer == str(question.answer):
            score += 1
    print(str(score))


test(questions)
