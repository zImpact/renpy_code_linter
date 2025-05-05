import os
from models import Issue, MARKDOWN_SAVE_FILENAME

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