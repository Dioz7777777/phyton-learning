import argparse
import sys
import refactoring


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='file', help='File name to read grades from', type=str, default="grades1.txt")
    parser.add_argument('-s', dest='sort_by', help='Kind of sorting', type=str, default="N", choices=["N", "A"])
    args = parser.parse_args()

    refactoring.main(args.file, args.sort_by)


if __name__ == "__main__":
    sys.exit(main())
