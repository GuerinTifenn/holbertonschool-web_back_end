# Python - Async Comprehension

This project focuses on asynchronous programming in Python, particularly on async comprehensions and async generators. The goal is to help you understand and implement asynchronous operations effectively using Python 3.7.

## Concepts

Before starting, it's essential to have a good understanding of the following concepts:
- Python - Asynchronous execution
- Python - Asynchronous Programming

## Resources

To complete this project, you should read or watch the following resources:
- [PEP 530 – Asynchronous Comprehensions](https://www.python.org/dev/peps/pep-0530/)
- [What’s New in Python: Asynchronous Comprehensions / Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep530)
- [Type-hints for generators](https://docs.python.org/3/library/typing.html#typing.Generator)

## Learning Objectives

By the end of this project, you should be able to:
- Write an asynchronous generator.
- Use async comprehensions.
- Type-annotate generators in Python.

## Requirements

### General
- Your code should be written in Python 3.7.
- All files should end with a new line.
- The first line of all your files should be `#!/usr/bin/env python3`.
- Your code should follow the `pycodestyle` (version 2.5.x) style guide.
- File lengths will be tested using `wc`.
- All modules should have documentation, including docstrings for functions and coroutines.
- All functions and coroutines must be type-annotated.

## Tasks

### Task 0: Async Generator

**File:** [`0-async_generator.py`](./0-async_generator.py)

Write a coroutine called `async_generator` that takes no arguments. This coroutine should:
- Loop 10 times.
- Asynchronously wait for 1 second in each iteration.
- Yield a random number between 0 and 10 using the `random` module.

```python
#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Task 1: Async Comprehensions

**File:** [`1-async_comprehension.py`](./1-async_comprehension.py)

Write a coroutine called `async_comprehension` that takes no arguments. This coroutine should:
- Collect 10 random numbers using an async comprehension over `async_generator`.
- Return the list of 10 random numbers.

```python
#!/usr/bin/env python3

from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
```

### Task 2: Run Time for Four Parallel Comprehensions

**File:** [`2-measure_runtime.py`](./2-measure_runtime.py)

Write a coroutine called `measure_runtime` that will execute `async_comprehension` four times in parallel using `asyncio.gather`. This coroutine should:
- Measure the total runtime of these parallel executions.
- Return the total runtime.

```python
#!/usr/bin/env python3

import asyncio
import time
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
```
