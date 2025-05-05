import re
from .base import BaseChecker
from models import Issue, IssueType

class SpacingChecker(BaseChecker):
    trailing_re = re.compile(r'[ \t]+$')

    def check(self, lines: list[str]) -> list[Issue]:
        for i, raw in enumerate(lines, start=1):
            if self.trailing_re.search(raw):
                self.add_issue(
                    i,
                    IssueType.WARNING.value,
                    "Лишние пробелы или табы в конце строки",
                    "Удалить все пробелы и табуляции после последнего символа"
                )

        return self.issues