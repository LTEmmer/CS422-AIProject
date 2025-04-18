# test_numpy_hello

    Purpose

    As I said above, refactor the above code to use the 'do' method in the 'say' class below.
    ```python
    class say:
        def say(self, numpy_string):
            self.string = numpy_string
            do("[[[0]\n [1]]]!")
            return "[[[[0]\n [1]]]!]!"
```
            You don't need to do anything else in this script. Just run it to see how well it works.
            ```python
            import unittest

            class numpy_greetings:
                from say import say

                def numpy_hello():
                    numpy_greetings.say("Hello World!")

                def test_numpy_hello(self):
                    self.assertEqual(numpy_greetings.say("Hello World!"), "[[[0]\n [1]]]!")
            ```
            ## Do not change any of the code above. The code below is what I wanted to test.
            ```python
            class say:
                def say(self, numpy_string):
                    self.string = numpy_string
                    do("[[[0]\n [1]]]!")
                    return "[[[[0]\n [1]]]!]!"
            ```
            ## I created this test class for you to use. Do not change any of the code below.
            ```python
            import unittest

            class numpy_greetings:
                from say import say

                def numpy_hello():
                    numpy_greetings.say("Hello World!")

                def test_numpy_hello(self):
                    self.assertEqual(numpy_greetings.say("Hello World!"), "[[[0]\n [1]]]!")
            ```
            I wanted to test your code above to see if it did what you wanted it to do. However, my test below did not pass.
            ```python
            unittest.main()
            ```
            I ran my test below to see if I was right.
            ```python
            class say:
                def say(self, numpy_string):
                    self.string = numpy_string
                    do("[[[0]\n [1]]]!")
                    return "[[[[0]\n [1]]]!]!"

            class test_numpy_greetings:
                def test_say(self):
                    self.assertEqual(numpy_greetings.say("Hello World!")
    Parameters

    ### Example
    Returns

    ```
    ---
    ##
    Examples

    """
    Explanation
    ```python
    code
    ```

    Code snippet
    ```python
    code
    ```

    Examples:
    ```python
    code
    ```

    Edge Case:
    ```python
    code
    ```

    Advanced Example:
    ```python
    code
    ```
    Docstring

    """```
    ```python
    def test_numpy_hello(self):
        """
        >>> test_numpy_hello()
        """
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```
    ```python
    def test_numpy_hello(self):
        """
        >>> test_numpy_hello()
        """
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purpose of the code *as written*.
    ```
    ```python
    def test_numpy_hello(self):
        """
        >>> test_numpy_hello()
        """
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')

    Include:

    A one-line description

    Args section with p"""
    ```