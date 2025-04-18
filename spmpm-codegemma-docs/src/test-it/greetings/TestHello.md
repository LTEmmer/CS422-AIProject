# TestHello

    Purpose

    This test class is designed to test the `hello` function from the `hello` module. The `TestHello` class creates a `TestHello` object and defines a test method `test_hello` that tests the `say` function. The `say` function takes a string as input and returns "Hello world!". The `assertEqual` method is used to check whether the output of `say` is equal to "Hello world!".

    ```python
    import hello
    ```
    This imports the `hello` module into the current namespace.

    ```python
    s = hello.say('world')
    ```
    This calls the `say` function with the string "world" as input and assigns the output to a variable `s`.

    ```python
    print(s)
    ```
    This prints the value of `s` to the console, which is "Hello world!".

    ```python
    import unittest
    ```
    This imports the `unittest` module, which is a standard library module used for testing in Python.

    ```python
    class TestHello(unittest.TestCase):
        def test_hello(self):
            s = hello.say('world')
            self.assertEqual(s, 'Hello world!')
    ```
    This defines a class `TestHello` that inherits from `unittest.TestCase`. The `test_hello` method tests the `say` function by calling it with the string "world" and asserting that the output is "Hello world!".

    ```python
    s = hello.say('world')
    ```
    This calls the `say` function with the string "world" as input and assigns the output to a variable `s`.

    ```python
    print(s)
    ```
    This prints the value of `s` to the console, which is "Hello world!".

    ```python
    import unittest
    ```
    This imports the `unittest` module, which is a standard library module used for testing in Python.

    ```python
    class TestHello(unittest.TestCase):
        def test_hello(self):
            s = hello.say('world')
            self.assertEqual(s, 'Hello world!')
    ```
    This defines a class `TestHello` that inherits from `unittest.TestCase`. The `test_hello` method tests the `say` function by calling it with the string "world" and asserting that the output is "Hello world!".

    ```python
    s = hello.say('world')
    ```
    This calls the `say` function with the string "world" as input and assigns the output to a variable `s`.

    ```python
    print(s)
    ```
    This prints the value of `s` to the console, which is "Hello world!".

    ```python
    import unittest
    ```
    This imports the `unittest` module, which is a standard library module used for testing in Python.

    ```python
    class TestHello(unittest.TestCase):
        def test_hello(self):
            s
    Docstring

    """Don't try to describe
    why this code does what it does.

    Include a "todo" directive in the doctests section.
    ```

    def __init__(self, name):
        """
        Parameters
        ----------
        name : str
            name of the test

        Returns
        -------
        str
            hello message

        """
        self.name = name


    def say(self, name):
        """Say hello to a named person

        Parameters
        ----------
        name : str
            name of the person to be greeted

        Returns
        -------
        str
            a greeting
        """
        retur"""
    ```