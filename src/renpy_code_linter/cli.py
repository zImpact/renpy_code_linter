import argparse
from utils import format_text_report
from linter import RenpyCodeLinter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Файлы или директории для проверки")
    args = parser.parse_args()

    linter = RenpyCodeLinter()
    issues = linter.run(paths=args.paths)
    print(format_text_report(issues))

if __name__ == "__main__":
    main()