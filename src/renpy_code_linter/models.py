from dataclasses import dataclass
from typing import Optional
from enum import Enum

MARKDOWN_SAVE_FILENAME = "REPORT.MD"

class IssueType(Enum):
    ERROR = "Error"
    WARNING = "Warning"

class OutputType(Enum):
    CONSOLE = "console"
    MARKDOWN = "markdown"

OUTPUT_FORMATS = [
    OutputType.CONSOLE,
    OutputType.MARKDOWN,
]

@dataclass
class Issue:
    file: str
    line: int
    type: IssueType
    message: str
    fix: Optional[str] = None