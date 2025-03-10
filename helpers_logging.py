from datetime import datetime

# logging_level = CRITICAL, ERROR, WARNING, INFO, DEBUG
logging_level = "DEBUG"
log_file_path = "app.log"


def log_message(message, level):
    levels = {"CRITICAL": 50, "ERROR": 40, "WARNING": 30, "INFO": 20, "DEBUG": 10}

    if levels.get(level, "DEBUG") >= levels[logging_level]:
        print(f"{level} | {message}")

        with open(log_file_path, "a") as log_file:
            log_file.write(f"{datetime.now()} | {level} | {message}\n")


if __name__ == "__main__":
    log_message("Debug message", "DEBUG")
    log_message("Info message", "INFO")
    log_message("Warning message", "WARNING")
    log_message("Error message", "ERROR")
    log_message("Critical message", "CRITICAL")
