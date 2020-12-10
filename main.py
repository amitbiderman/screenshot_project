import sys
from core import WebSnapShooter


def main():
    if len(sys.argv) < 2:
        print("Error: no URL supplied.")
        exit(1)

    url_arg = sys.argv[1]

    snapshooter = WebSnapShooter()
    if not snapshooter.init_driver():
        print("Error: failed to initialize WebSnapShooter")
        exit(1)

    if not snapshooter.take_screenshot(url_arg):
        print("Error: failed to take a screenshot")
        exit(1)

    print("Finished successfully")
    exit(0)


if __name__ == '__main__':
    main()
