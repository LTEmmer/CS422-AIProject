# test_numpy_hello

    Purpose

    This function takes a list of numbers and returns a list of the same numbers multiplied by 2.
    
    @param num_list a list of numbers
    @return a list of the same numbers multiplied by 2
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    def double_numbers(num_list):
        """
        Doubles the values in the list num_list
        
        Args:
        num_list: a list of numbers
        
        Returns:
        a list of the same numbers multiplied by 2
        """
        result = []
        for num in num_list:
            result.append(num * 2)
        return result
    
    @param result a list of the same numbers multiplied by 2
    @example: [2, 4, 6] -> [2, 4, 6]
    @example: [2, 4, 6, 8, 10, 12, 14, 16, 18] -> [2, 4, 6, 8, 10, 12, 14, 16, 18]
    """
    def test_numpy_hello(self):
        """
        Tests the numpy_greetings.numpy_hello module
        """
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')
    
    @param s a string containing the message to be returned
    @example: 'Hello [[0]\n [1]]!' -> 'Hello [[0]\n [1]]!'
    @example: 'Hello [[2]\n [3]\n [4]\n [5]]!' -> 'Hello [[2]\n [3]\n [4]\n [5]]!'
    """
    def say(self):
        """
        Prints a greeting message
        
        Returns:
        a string containing the message to be returned
        """
        names = numpy.arange(self.n)
        s = "Hello " + names + "!"
        s = s.reshape(self.n, 1)
        return s
    
    @param n the number of names to be greeted
    @example: 1 -> 'Hello [[0]]!'
    @example: 3 -> 'Hello [[0]\n [1]\n [2]]!'
    """
    def __init__(self, n):
        """
        Initializes the numpy_greetings object
        
        Args:
        n: the number of names to be greeted
        """
        self.n = n
    
    @param n the number of names to be greeted
    @example: 1 -> 'Hello [[0]]!'
    @example: 3 -> 'Hello [[0]\n [1]\n [2]]!'
    """
    def say(self, n):
        """
        Prints a greeting message
        
        Args:
        n: the number of names to be greeted
        
        Returns:
        a string containing the message to be returned
        """
        if n == 0:
            return None
        names = numpy.arange(n)
        s = "Hello " + names + "!"
        s = s.reshape(n, 1)
        return s
    
    @param result a list of the sum of the numbers in num_list
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
    """
    def test_numpy_hello(self):
        """
        Tests the numpy_greetings.numpy_hello module
        """
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')
    
    @param num_list a list of numbers
    @return a list of the sum of the numbers in num_list
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
    """
    def sum_list(num_list):
        """
        Sums the values in the list num_list
        
        Args:
        num_list: a list of numbers
        
        Returns:
        a list of the sum of the numbers in num_list
        """
        result = []
        for num in num_list:
            result.append(num + 2)
        return result
    
    @param num_list a list of numbers
    @return a list of the sum of the numbers in num_list
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
    """
    def sum_list(num_list):
        """
        Sums the values in the list num_list
        
        Args:
        num_list: a list of numbers
        
        Returns:
        a list of the sum of the numbers in num_list
        """
        result = []
        for num in num_list:
            result.append(num + 2)
        return result
    
    @param num_list a list of numbers
    @return a list of the sum of the numbers in num_list
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
    """
    def sum_list(num_list):
        """
        Sums the values in the list num_list
        
        Args:
        num_list: a list of numbers
        
        Returns:
        a list of the sum of the numbers in num_list
        """
        result = []
        for num in num_list:
            result.append(num + 2)
        return result
    
    @param result a list of the sum of the numbers in num_list
    @example: [1, 2, 3] -> [2, 4, 6]
    @example: [1, 2, 3, 4, 5, 6, 7, 8, 9] -> [3, 6, 9, 12, 15, 18, 21, 24, 27]
    """
    def sum_list(num_list):
        """
        Sums the values in the list num_list
        
        Args:
        num_list: a list of numbers
        
        Returns:
        a list of the sum of the numbers in num_list
        """
        result = []
        for num in num_list:
            result.append(num +
    Parameters

    ""
    Returns

    
    Examples

    Always explain what the code does, and why it's needed.

    ## Basic usage

    ### Explanation
    ```python
    import numpy as np

    ### Code
    ```

    ### Example
    ```python
    # Explanation
    ### Code
    ```

    ## Edge case

    ### Explanation
    ```python
    ### Code
    ```

    ### Example
    ```python
    ### Explanation
    ### Code
    ```

    ## Advanced scenario (if applicable)

    ### Explanation
    ```python
    ### Code
    ```

    ### Example
    ```python
    ### Explanation
    ### Code
    ```


## Code Examples


### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Explanation
### Code

### Example
```python
# Explanation
### Code
```

### Basic usage

import numpy as np

### Exp
    Docstring

    """```
```
```python
    def test_numpy_hello(self):
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
```
```python
def test_numpy_hello(self):
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
    def test_numpy_hello(self):
        s = numpy_greetings.numpy_hello.say()
        self.assertEqual(s, 'Hello [[0]\n [1]]!')

    Include:

    A one-line description

    Args section with parameter details

    Returns section with return value details

    Examples section showing usage

    Do not offer suggestions, refactorings, or code improvements.
    Only describe the purp"""
    ```