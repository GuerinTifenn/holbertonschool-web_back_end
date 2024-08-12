# Python - Variable Annotations

## Introduction

This project focuses on the use of type annotations in Python. Type annotations help specify function signatures and variable types, improving code readability and robustness. You will learn how to use type annotations for functions and variables, and how to validate your code using `mypy`.

## Learning Objectives

By the end of this project, you should be able to:
- Understand type annotations in Python 3.
- Use type annotations to specify function signatures and variable types.
- Apply Duck typing.
- Validate your code using `mypy`.

## Requirements

- Python 3.9
- `mypy` for type validation

## Project Structure

Each task is associated with a specific Python file, as listed below. The files are created following the requirements provided in the project instructions.

### Tasks

#### 0. Basic annotations - add

Write a type-annotated function `add` that takes two arguments of type `float` and returns their sum as a `float`.

File: [`0-add.py`](./0-add.py)

#### 1. Basic annotations - concat

Write a type-annotated function `concat` that takes two string arguments `str1` and `str2` and returns a concatenated string.

File: [`1-concat.py`](./1-concat.py)

#### 2. Basic annotations - floor

Write a type-annotated function `floor` which takes a `float` `n` as an argument and returns the floor of the float as an `int`.

File: [`2-floor.py`](./2-floor.py)

#### 3. Basic annotations - to string

Write a type-annotated function `to_str` that takes a `float` `n` as an argument and returns the string representation of the float.

File: [`3-to_str.py`](./3-to_str.py)

#### 4. Define variables

Define and annotate the following variables with the specified values:
- `a`: an integer with a value of `1`
- `pi`: a float with a value of `3.14`
- `i_understand_annotations`: a boolean with a value of `True`
- `school`: a string with a value of `"Holberton"`

File: [`4-define_variables.py`](./4-define_variables.py)

#### 5. Complex types - list of floats

Write a type-annotated function `sum_list` which takes a list of floats as an argument and returns their sum as a `float`.

File: [`5-sum_list.py`](./5-sum_list.py)

#### 6. Complex types - mixed list

Write a type-annotated function `sum_mixed_list` which takes a list of integers and floats and returns their sum as a `float`.

File: [`6-sum_mixed_list.py`](./6-sum_mixed_list.py)

#### 7. Complex types - string and int/float to tuple

Write a type-annotated function `to_kv` that takes a string `k` and an int or float `v` as arguments and returns a tuple. The first element of the tuple is the string `k`, and the second element is the square of the int/float `v` as a `float`.

File: [`7-to_kv.py`](./7-to_kv.py)

#### 8. Complex types - functions

Write a type-annotated function `make_multiplier` that takes a float `multiplier` as an argument and returns a function that multiplies a float by `multiplier`.

File: [`8-make_multiplier.py`](./8-make_multiplier.py)

#### 9. Let's duck type an iterable object

Annotate the below function’s parameters and return values with the appropriate types:
```python
def element_length(lst):
    return [(i, len(i)) for i in lst]
```

File: [`9-element_length.py`](./9-element_length.py)
