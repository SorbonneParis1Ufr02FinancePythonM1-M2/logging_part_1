from repository import get_data
from view import display_results


def main():
    print("Begin program")
    data = get_data()

    display_results(data)

    print("End program")


if __name__ == '__main__':
    main()
