def hello(param: str) -> str : 
    """Return params"""
    return param

def hello_user(param: str, user: str) -> str : 
    """Return params and user

    Parameter : 
    :param -- statement
    :user -- user name

    :Example : 
    >>> hello_user("Hello", "John")
        'Hello John'
    
    """
    return f"param : {param}, user: {user}"

"""
Docstrings are an essential part of writing clean, readable, and maintainable code. They provide a convenient way of associating documentation with Python modules, functions, classes, and methods. Here are some best practices for writing docstrings in Python: 
    1. Use Triple Quotes: Always use triple double quotes (\""") for docstrings, even if the string fits on one line. This makes it easy to expand the docstring later. 
    2. Describe the Purpose: Start with a short description of the function's purpose. This should be a concise summary of what the function does. 
    3. Include Parameters and Return Types: Clearly describe each parameter and the return type. Use the :param and :return directives to specify the types and descriptions. 4.
    4. Provide Examples: Include example usage of the function. This helps users understand how to use the function and what to expect as output. 
    5. Mention Exceptions: If the function raises any exceptions, mention them in the docstring using the :raises directive. 
    6. Follow PEP 257: Adhere to the conventions outlined in PEP 257, which provides guidelines for writing docstrings. 
    7. Be Consistent: Maintain a consistent style and format throughout your codebase. This makes it easier for others to read and understand your documentation. 
    8. Use Imperative Mood: Write the description in the imperative mood. For example, use "Return the sum of x and y" instead of "Returns the sum of x and y". 
    9. Keep It Simple: Avoid overly complex language and keep the docstring simple and to the point. 
    10. Update Regularly: Ensure that the docstrings are kept up-to-date with the code. If the function's behavior changes, update the docstring accordingly. 
    
    Example of a Well-Documented Function Here is an example of a well-documented function following the best practices:
"""

def add(x: int, y: int) -> int:
    """
    Add two numbers and return the result.

    :param x: The first number.
    :type x: int
    :param y: The second number.
    :type y: int
    :return: The sum of x and y.
    :rtype: int

    :example:
    >>> add(2, 3)
    5

    :raises TypeError: If x or y is not an integer.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers")
    return x + y
