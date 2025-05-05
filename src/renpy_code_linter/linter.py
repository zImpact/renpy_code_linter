from utils import gather_rpy_files, load_file
from checkers.indentation import IndentationChecker
from checkers.naming import NamingChecker
from checkers.spacing import SpacingChecker

class RenpyCodeLinter:
    def __init__(self):
        self.checkers = [
            IndentationChecker(),
            NamingChecker(),
            SpacingChecker()
        ]

    def run(self, paths):
        all_issues = []
        files = gather_rpy_files(paths)
        for path in files:
            lines = load_file(path)
            for checker in self.checkers:
                issues = checker.run(path, lines)
                all_issues.extend(issues)
        return all_issues