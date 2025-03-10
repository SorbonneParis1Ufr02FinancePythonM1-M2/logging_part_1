# level = CRITICAL, ERROR, WARNING, INFO, DEBUG
logging_level = "DEBUG"


def log_message(message, level):
    levels = {"CRITICAL": 50, "ERROR": 40, "WARNING": 30, "INFO": 20, "DEBUG": 10}

    if levels.get(level, "DEBUG") >= levels[logging_level]:
        print(f"{level} | {message}")


if __name__ == "__main__":
    log_message("Debug message", "DEBUG")
    log_message("Info message", "INFO")
    log_message("Warning message", "WARNING")
    log_message("Error message", "ERROR")
    log_message("Critical message", "CRITICAL")
