class FormatNotSupported(Exception):
    """Raises when filename format is not in .csv format
    """

    def __init__(self, filename: str):
        self.filename = filename.split(".")[1]

    def __str__(self) -> str:
        return f".{self.filename} file is not supported"


class MaxTargetValueException(Exception):
    """Raises when target column contains types of value more than 2
    """

    def __init__(self, countss: int):
        self.count = countss

    def __str__(self) -> str:
        return f"Target Column contains {self.count} Type of values it should be of 2 Types"


class ValueNotFoundException(Exception):
    """Raises when the value from the sample list is not in the loaded filename.csv
    """

    def __init__(self, filename: str, value: str):
        self.filename = filename
        self.value = value

    def __str__(self) -> str:
        return f"{self.value} not found in {self.filename}"


class WrongTargetColumnException(Exception):
    """Wrong target column Exception when the column is not present in the data"""

    def __init__(self, filename):
        self.name = filename

    def __str__(self) -> str:
        return f"The target column name should be same as in {self.name}"
