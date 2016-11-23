# encoding: utf-8


class Person(object):
    """This is a class of Person.

    # Arguments
        name: `str`. The name of the Person instance.
        age: `int`. Defaults to 18. The age of the Person instance.

    # Attributes
        name: `str`. The name of the Person instance.
        age: `int`. Defaults to 18. The age of the Person instance.
        sex: `str`. Defaults to 'male'. The sex of the Person instance.

    # Note
        This is Note.

    # Examples
        You could create a Person instance in this way:
        ```python
        batman = Person('Bruce Wayne')
        elder = Person('you-know-who`, 99)
        ```
    """

    def __init__(self, name, age=18):
        self.name = name
        self.age = age
        self.sex = 'male'

    def speak(self, message):
        """Speak something.

        # Argument:
            message: `str`. Something to speak.

        # Return:
            `None`.
        """
        print('[{}]: {}'.format(self.name, message))


def show_info(person):
    """Show the personal information of the given person.

    # Argument
        person: `Person`. The person.
    """
    print('name:{}, age:{}'.format(person.name, person.age))


if __name__ == '__main__':
    p = Person('monitor1379')
    p.speak('Are you OK?')
    show_info(p)
