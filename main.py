from helpers_logging import log_message
from repository import get_data
from view import display_results


def main():
    log_message("Begin program", level="INFO")
    data = get_data()

    display_results(data)

    log_message("End program", level="INFO")


if __name__ == '__main__':
    main()

