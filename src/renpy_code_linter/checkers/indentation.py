from checkers.base import BaseChecker
from models import Issue, IssueType

class IndentationChecker(BaseChecker):
    def check(self, lines: list[str]) -> list[Issue]:
        for i, raw in enumerate(lines, start=1):
            if raw.strip() == "":
                continue
            
            indent_part = raw[:len(raw) - len(raw.lstrip())]

            if "\t" in indent_part:
                self.add_issue(
                    i,
                    IssueType.ERROR.value,
                    "Используется табуляция вместо четырех пробелов",
                    "Заменить табуляцию на пробелы"
                )

            spaces = indent_part.count(" ")
            if spaces % 4 != 0:
                self.add_issue(
                    i,
                    IssueType.ERROR.value,
                    f"Отступ {spaces} пробелов не кратен четырем",
                    "Использовать отступ в количество пробелов кратных четырем"
                )

        return self.issues
