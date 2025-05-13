import os
import re
from models import Issue, MARKDOWN_SAVE_FILENAME

def to_snake_case(s: str) -> str:
    s = re.sub(r"[ \-\.]+", "_", s)
    s = re.sub(r"(?<=[a-z0-9])([A-Z])", r"_\1", s)
    s = s.lower()
    s = re.sub(r"_+", "_", s).strip("_")
    return s

def to_camel_case(s: str) -> str:
    parts = re.split(r"[ _\-\.\t]+", s)
    parts = [p for p in parts if p]
    transformed = [p[0].upper() + p[1:] for p in parts]
    result = "".join(transformed)
    return result

def gather_rpy_files(paths: list[str]) -> list[str]:
    result = []
    for path in paths:
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    if file.endswith(".rpy"):
                        result.append(os.path.join(root, file))
        elif path.endswith(".rpy"):
            result.append(path)
    return result


def load_file(path):
    with open(path, encoding="utf-8") as file:
        return file.read().splitlines()
    
def format_text_report(issues: list[Issue]):
    out = []
    for issue in issues:
        out.append(f"{issue.file}:{issue.line}: {issue.type}: {issue.message}"
                   + (f" – Suggestion: {issue.fix}" if issue.fix else ""))
    return "\n\n".join(out)

def save_report(report: str) -> None:
    filename = os.getenv("GITHUB_STEP_SUMMARY", MARKDOWN_SAVE_FILENAME)
    mode = "a" if os.getenv("GITHUB_STEP_SUMMARY") else "w"

    with open(filename, mode, encoding="utf-8") as f:
        f.write("```\n")
        f.write(report + "\n")
        f.write("```\n")