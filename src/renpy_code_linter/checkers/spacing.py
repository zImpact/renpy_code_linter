import re
from checkers.base import BaseChecker
from models import Issue, IssueType

class SpacingChecker(BaseChecker):
    op_pattern = re.compile(
        r"(?:\+=|-=|\*=|/=|%=|//=|\*\*=|&=|\|=|\^=|>>=|<<=|==|!=|<=|>=|<|>|="
        r"|\band\b|\bor\b|\bnot\b)"
    )
    string_literals = re.compile(r"(\"[^\"]*\"|'[^']*')")
    trailing = re.compile(r'[ \t]+$')

    def check(self, lines: list[str]) -> list[Issue]:
        paren_depth = 0

        for i, raw in enumerate(lines, start=1):
            text = raw.rstrip("\n")
            stripped = text.strip()

            if stripped == "":
                paren_depth = max(paren_depth + text.count("(") - text.count(")"), 0)
                continue

            text_without_literals = self.string_literals.sub("", text)
            for m in self.op_pattern.finditer(text_without_literals):
                op = m.group(0)
                start, end = m.span(0)

                prefix = text_without_literals[:start]
                local_depth = prefix.count("(") - prefix.count(")")
                if paren_depth + local_depth > 0:
                    continue
                
                left = text_without_literals[start - 1] if start - 1 >= 0 else ""
                right = text_without_literals[end] if end < len(text_without_literals) else ""
                if not (left.isspace() and right.isspace()):
                    self.add_issue(
                        i,
                        IssueType.WARNING.value,
                        f"Оператор '{op}' без пробелов вокруг",
                        f"Добавить пробелы вокруг '{op}'"
                    )
                   
            if self.trailing.search(raw):
                self.add_issue(
                    i,
                    IssueType.WARNING.value,
                    "Лишние пробелы или табы в конце строки",
                    "Удалить все пробелы и табуляции после последнего символа"
                )

            paren_depth = max(paren_depth + text.count("(") - text.count(")"), 0)

        return self.issues