from datetime import datetime

# logging_level = CRITICAL, ERROR, WARNING, INFO, DEBUG
console_logging_level = "DEBUG"
file_logging_level = "DEBUG"
log_file_path = "app.log"


def log_message(message, level):
    levels = {"CRITICAL": 50, "ERROR": 40, "WARNING": 30, "INFO": 20, "DEBUG": 10}

    _level = levels.get(level, "DEBUG")
    if _level >= levels[console_logging_level]:
        print(f"{level} | {message}")

    if _level >= levels[file_logging_level]:
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.now()} | {level} | {message}\n")


if __name__ == "__main__":
    log_message("Debug message", "DEBUG")
    log_message("Info message", "INFO")
    log_message("Warning message", "WARNING")
    log_message("Error message", "ERROR")
    log_message("Critical message", "CRITICAL")
