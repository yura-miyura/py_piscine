#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.processed_data: list[Any] = []
        self.counter: int = -1

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        try:
            data: str = self.processed_data.pop(0)
            self.counter += 1
        except IndexError:
            return (-1, "")
        return (self.counter, data)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(d, (int, float)) for d in data)
        return isinstance(data, (int, float))

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.processed_data.extend([nb for nb in data])
            else:
                self.processed_data.append(data)
        else:
            print("Improper numeric data")


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            return all(isinstance(d, str) for d in data)
        return isinstance(data, str)

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.processed_data.extend([nb for nb in data])
            else:
                self.processed_data.append(data)
        else:
            print("Improper text data")


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        def is_str_dict(d: Any) -> bool:
            return isinstance(d, dict) and all(
                isinstance(k, str) and isinstance(v, str) for k, v in d.items()
            )

        if isinstance(data, list):
            return all(is_str_dict(d) for d in data)
        return is_str_dict(data)

    def ingest(self, data: Any) -> None:
        if self.validate(data):
            if isinstance(data, list):
                self.processed_data.extend([nb for nb in data])
            else:
                self.processed_data.append(data)
        else:
            print("Improper log data")

    def output(self) -> tuple[int, str]:
        try:
            data: dict[str, str] = self.processed_data.pop(0)
            msg: str = ": ".join(data.values())
            self.counter += 1
        except IndexError:
            return (-1, "")
        return (self.counter, msg)


class TestProcessor:
    def __init__(self, processor: DataProcessor) -> None:
        print(f"Testing {type(processor).__name__}...")
        self._processor = processor

    def validate(self, input: Any) -> None:
        print(f" Trying to validate input '{input}':",
              self._processor.validate(input))

    def invalid_ingestion(self, input: Any) -> None:
        print(
            f" Test invalid ingestion of {type(input).__name__} "
            f"'{input}' without prior validation:"
        )
        print(" Got exception: ", end="")
        self._processor.ingest(input)

    def proces_data(self, data: Any) -> None:
        self._processor.ingest(data)
        print(" Processing data:", data)

    def output_data(self, amount: int) -> None:
        msg: str = "value"
        if isinstance(self._processor, NumericProcessor):
            msg = "Numeric " + msg
        elif isinstance(self._processor, TextProcessor):
            msg = "Text " + msg
        else:
            msg = "Log entry"
        extracting_msg: str = f"Extracting {amount} value"
        if amount > 1:
            extracting_msg += "s"
        print(" " + extracting_msg + "...")
        for _ in range(amount):
            i, k = self._processor.output()
            print(f" {msg} {i}: {k}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")
    print()
    numeric_test = TestProcessor(NumericProcessor())
    numeric_test.validate(42)
    numeric_test.validate("Hello")
    numeric_test.invalid_ingestion("foo")
    numeric_test.proces_data([1, 2, 3, 4, 5])
    numeric_test.output_data(3)
    print()
    text_test = TestProcessor(TextProcessor())
    text_test.validate(42)
    text_test.proces_data(["Hello", "Nexus", "World"])
    text_test.output_data(1)
    print()
    log_test = TestProcessor(LogProcessor())
    log_test.validate("Hello")
    log_test.proces_data(
        [
            {"log_level": "NOTICE", "log_message": "Connection to server"},
            {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
        ]
    )
    log_test.output_data(2)


if __name__ == "__main__":
    main()
