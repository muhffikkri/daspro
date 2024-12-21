# Dasar Pemrograman Exercises

This repository contains function for the subject "Dasar Pemrograman". This repository is intended for educational purposes and to help students understand the basic concepts of programming.

## Overview

This README will cover the following topics:

- Basic Expressions (function evaluation, named expression, etc.)
- Conditional Expressions
- Built-in Data Types
- Object Collections
- Recursive Expressions
- Lists
- Trees
- Lambda Functions

## Topic Summaries

### Basic Expressions (function evaluation, named expression, etc.)

Fundamental programming constructs such as evaluating functions and using named expressions (variables).

### Conditional Expressions

Expressions that evaluate to different values based on certain conditions, typically using `if`, `else`, and `elif` statements.

### Built-in Data Types

Standard data types provided by the programming language, such as integers, floats, strings, and booleans.

#### Example:

```python
data_types = ["int", "float", "str", "bool"]
print(data_types)  # Output: ['int', 'float', 'str', 'bool']
```

### Object Collections

Data structures that can hold multiple objects, such as arrays, lists, sets, and dictionaries.

### Recursive Expressions

Expressions where a function calls itself in order to solve a problem, often used in algorithms that break down problems into smaller, more manageable sub-problems.

#### Example:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### Lists

Ordered collections of items, which can be of any data type. Lists are a common data structure used to store sequences of elements.

#### Example:

```python
def sum_list(lst):
    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4]))  # Output: 10
```

### Trees

Hierarchical data structure where each element (node) has a value and references to other nodes (children). Trees are used in various algorithms and applications, such as representing hierarchical relationships.

#### Example:

```python
def sum_tree(tree):
    if tree == []:
        return 0
    else:
        return tree[0] + sum_tree(tree[1]) + sum_tree(tree[2])

tree = [1, [2, [], []], [3, [4, [], []], []]]
print(sum_tree(tree))  # Output: 10
```

### Lambda Functions

Small, anonymous functions defined using the `lambda` keyword. They are often used for short, throwaway functions that are not reused elsewhere in the code.

#### Example :

```python
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5
```
