# encoding: utf-8

def hello_world(message):
    """Speak a message.

    Speak a message to the world.

    # Argument
        message: `str`. The message you want to speak.

    # Return
        `None`.
    """
    pass


class Person(object):
    """This is a class of Person.

    # Arguments
        name: `str`. The name of the Person instance.
        age: `int`. Defaults to 18. The age of the Person instance.

    # Examples
        You could create a Person instance in this way:
        ```python
        batman = Person('Bruce Wayne')
        elder = Person('you-know-who', 99)
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
    from sophon.parsers import SophonParser
    parser = SophonParser()
    print parser.parse_from_class(Person)
    print parser.parse_from_function(Person.speak)
    print parser.parse_from_function(show_info)

