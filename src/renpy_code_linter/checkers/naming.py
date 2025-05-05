import re
from .base import BaseChecker
from models import Issue, IssueType

class NamingChecker(BaseChecker):
    func_var_re = re.compile(r'^[a-z_][a-z0-9_]*$')
    class_re = re.compile(r'^[A-Z][a-zA-Z0-9]+$')

    def check(self, lines: list[str]) -> list[Issue]:
        for i, raw in enumerate(lines, start=1):
            s = raw.strip()

            if s.startswith("def "):
                name = s.split()[1].split("(")[0]
                if not self.func_var_re.match(name):
                    self.add_issue(
                        i,
                        IssueType.WARNING.value,
                        f"Имя функции '{name}' не в snake_case",
                        "Использовать lower_case_with_underscores"
                    )

            if s.startswith("class "):
                name = s.split()[1].split("(")[0].rstrip(":")
                if not self.class_re.match(name):
                    self.add_issue(
                        i,
                        IssueType.WARNING.value,
                        f"Имя класса '{name}' не в CamelCase",
                        "Использовать MyClassName"
                    )

        return self.issues