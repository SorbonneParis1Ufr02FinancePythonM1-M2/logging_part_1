from helpers_logging import logging_status
from repository import get_data
from view import display_results


def main():
    if logging_status:
        print("Begin program")
    data = get_data()

    display_results(data)

    if logging_status:
        print("End program")


if __name__ == '__main__':
    main()

