# 0x01-python_async_function

This project focuses on asynchronous programming in Python, specifically using the `asyncio` module. It includes various tasks to demonstrate the use of asynchronous functions, coroutines, and tasks.

## Files and Descriptions

### Python Scripts

- **`0-basic_async_syntax.py`**: Contains the `wait_random` coroutine, which waits for a random delay between 0 and `max_delay` seconds and returns the delay.

- **`1-concurrent_coroutines.py`**: Implements the `wait_n` coroutine, which spawns `wait_random` multiple times concurrently and returns a list of delays in ascending order.

- **`2-measure_runtime.py`**: Defines the `measure_time` function to measure the average runtime of executing `wait_n`.

- **`3-tasks.py`**: Contains the `task_wait_random` function, which creates an `asyncio.Task` for the `wait_random` coroutine.

- **`4-tasks.py`**: Implements the `task_wait_n` coroutine, which executes multiple `asyncio` tasks concurrently and returns their results in the order of completion.

### Test Scripts

- **`0-main.py`**: Test script for `wait_random`.
- **`1-main.py`**: Test script for `wait_n`.
- **`2-main.py`**: Test script for `measure_time`.
- **`3-main.py`**: Test script for `task_wait_random`.
- **`4-main.py`**: Test script for `task_wait_n`.

### Configuration

- **`.vscode/settings.json`**: Contains settings for Python analysis in the workspace.

## Concepts Covered

- Asynchronous programming with `async` and `await`.
- Using `asyncio` for concurrency.
- Creating and managing `asyncio.Task` objects.
- Measuring execution time for asynchronous functions.
- Handling multiple coroutines with `asyncio.as_completed`.

## Usage

To run any of the scripts, use the following command:

```bash
./<script_name>.py
```

## Requirements
- Python 3.8 or higher
- Basic understanding of asynchronous programming in Python

## Author
Hassan Ahmed

This project is part of the ALX Backend Python curriculum.
