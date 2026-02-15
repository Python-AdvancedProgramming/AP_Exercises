from typing import Iterable, Iterator

logs = [
    "INFO: Server started",
    "ERROR: Database not reachable",
    "WARNING: Disk space low",
    "ERROR: Timeout"
]


def filter_errors(logs: Iterable[str]) -> Iterator[str]:
    for log in logs:
        if "ERROR" in log:
            yield log


def add_prefix(logs: Iterable[str]) -> Iterator[str]:
    for log in logs:
        yield f"LOG: {log}"


pipeline = add_prefix(filter_errors(logs))

for entry in pipeline:
    print(entry)
