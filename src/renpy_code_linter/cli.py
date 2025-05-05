import argparse
import models
import os
from utils import format_text_report, save_report
from linter import RenpyCodeLinter
from models import MARKDOWN_SAVE_FILENAME

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "paths",
        nargs="+",
        help="Файлы или директории для проверки"
    )
    parser.add_argument(
        "--output-type",
        choices=[output.value for output in models.OUTPUT_FORMATS],
        default=models.OutputType.CONSOLE.value
    )
    args = parser.parse_args()

    linter = RenpyCodeLinter()
    issues = linter.run(paths=args.paths)

    report = format_text_report(issues)
    if args.output_type == models.OutputType.CONSOLE.value:
        print(report)

    elif args.output_type == models.OutputType.MARKDOWN.value:
        save_report(report)

        if not os.environ.get("GITHUB_STEP_SUMMARY"):
            print(f"Результат сохранён в файле: {MARKDOWN_SAVE_FILENAME}")

if __name__ == "__main__":
    main()