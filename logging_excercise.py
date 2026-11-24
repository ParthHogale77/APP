"""
Write a program to set up logging to record messages of different severity levels (DEBUG, INFO,
WARNING, ERROR, and CRITICAL) to both the console and a file. Show how to configure the logging
system and demonstrate the use of different logging levels.
"""
import logging

# 1. Configure the logging system (Get logger)
logger = logging.getLogger("Experiment14Logger")
logger.setLevel(logging.DEBUG)  # Capture all levels starting from DEBUG

# 2. Create handlers (Console & File)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("app_experiment14.log", mode="w", encoding="utf-8")

# 3. Set level for handlers
# Console will show INFO level and above (INFO, WARNING, ERROR, CRITICAL)
console_handler.setLevel(logging.INFO)

# File will log everything from DEBUG level and above
file_handler.setLevel(logging.DEBUG)

# 4. Create formatters and add them to handlers
console_format = logging.Formatter("{levelname} - {message}", style="{")
file_format = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{", datefmt="%Y-%m-%d %H:%M:%S")

console_handler.setFormatter(console_format)
file_handler.setFormatter(file_format)

# 5. Add handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 6. Add Logging messages
print("--- Starting Logging Demo ---")

logger.debug("This is a DEBUG message (Detailed info for developers).")
logger.info("This is an INFO message (General program status).")
logger.warning("This is a WARNING message (Something unexpected happened).")
logger.error("This is an ERROR message (A serious problem occurred).")
logger.critical("This is a CRITICAL message (System crash or severe failure).")

# Demonstrate capturing an exception stack trace
try:
    result = 10 / 0
except ZeroDivisionError:
    logger.exception("An exception occurred: Division by zero!")

# 7. Complete
print("--- Logging Complete. Check 'app_experiment14.log' file for output logs ---")

"""
--> Output
--- Starting Logging Demo ---
INFO - This is an INFO message (General program status).
WARNING - This is a WARNING message (Something unexpected happened).
ERROR - This is an ERROR message (A serious problem occurred).
CRITICAL - This is a CRITICAL message (System crash or severe failure).
ERROR - An exception occurred: Division by zero!
Traceback (most recent call last):
  File "c:\Users\Saurabh Jain\Desktop\PRASUK JAIN\VS Code\School\Advanced Python Programming\logging_excercise.py", line 40, in <module>
    result = 10 / 0
             ~~~^~~
ZeroDivisionError: division by zero
--- Logging Complete. Check 'app_experiment14.log' file for output logs ---
"""