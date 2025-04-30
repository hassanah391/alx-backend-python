# 0x02-python_async_comprehension

This project focuses on asynchronous programming in Python, specifically using asynchronous generators, comprehensions, and measuring runtime for concurrent tasks.

## Files

### 0-async_generator.py
This module contains the `async_generator` function:
- An asynchronous generator that yields 10 random floating-point numbers between 0 and 10.
- Each number is yielded after a 1-second delay.

### 1-async_comprehension.py
This module contains the `async_comprehension` function:
- A coroutine that collects 10 random numbers from `async_generator` using an asynchronous list comprehension.
- Returns a list of 10 random floating-point numbers.

### 2-measure_runtime.py
This module contains the `measure_runtime` function:
- A coroutine that measures the total runtime of running `async_comprehension` four times concurrently using `asyncio.gather`.
- Returns the total runtime in seconds.

### main_files/
This directory contains test scripts for the modules:
- `0-main.py`: Tests the `async_generator` function by printing the yielded values.
- `1-main.py`: Tests the `async_comprehension` function by printing the collected list of random numbers.
- `2-main.py`: Tests the `measure_runtime` function by printing the total runtime.

## How to Run
1. Ensure you have Python 3.7+ installed.
2. Run the test scripts in the `main_files` directory to verify the functionality of each module:
   ```bash
   python3 main_files/0-main.py
   python3 main_files/1-main.py
   python3 main_files/2-main.py

## Concepts Covered
- Asynchronous programming with `async` and `await`.
- Using asynchronous generators.
- Collecting data with asynchronous comprehensions.
- Measuring runtime for concurrent tasks with `asyncio.gather`.

## Requirements
- python 3.7 or higher.
- Basic understanding of asynchronous programming in Python.
