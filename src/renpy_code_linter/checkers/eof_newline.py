from checkers.base import BaseChecker
from models import Issue, IssueType

class EofNewlineChecker(BaseChecker):
    def check(self, lines: list[str]) -> list[Issue]:
        if not lines:
            return self.issues
        
        try:
            with open(self.current_file, "rb") as file:
                file.seek(-1, 2)
                last_byte = file.read(1)

        except (OSError, ValueError):
            return self.issues
        
        if last_byte != b"\n":
            self.add_issue(
                len(lines),
                IssueType.WARNING.value,
                "Нет пустой строки в конце файла",
                "Добавить пустую строку в конец файла"
            )

        return self.issues