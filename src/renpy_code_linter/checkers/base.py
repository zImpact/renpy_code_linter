from abc import ABC, abstractmethod
from models import Issue, IssueType

class BaseChecker(ABC):
    def __init__(self):
        self.current_file: str = ""
        self.issues: list[Issue] = []

    def add_issue(self, line: int, type_: IssueType, message: str, fix: str | None = None) -> None:
        self.issues.append(Issue(file=self.current_file, line=line, type=type_, message=message, fix=fix))

    @abstractmethod
    def check(self, lines: list[str]) -> list[Issue]:
        ...

    def run(self, filepath: str, lines: list[str]) -> list[Issue]:
        self.current_file = filepath
        self.issues.clear()
        self.check(lines)
        return self.issues