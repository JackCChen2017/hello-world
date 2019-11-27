from random import choice


class Person:
    def __init__(self, name):
        self.greeting = 'hello {name}'
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    people = [
        Person('jane'),
        Person('jill'),
        Person('bob'),
        Person('banana')
    ]

    person = choice(people)
    print(person)


if __name__ == '__main__':
    main()
