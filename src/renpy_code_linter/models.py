from dataclasses import dataclass
from typing import Optional
from enum import Enum

class IssueType(Enum):
    ERROR = "Error"
    WARNING = "Warning"

@dataclass
class Issue:
    file: str
    line: int
    type: IssueType
    message: str
    fix: Optional[str] = None