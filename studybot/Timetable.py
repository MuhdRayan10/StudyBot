# import matplotlib.pyplot as plt
import pandas as pd


class TimeTable:
    """Class that represents a time table."""

    def __init__(self, days: int, periods: int, startDay="Mon", endDay="Sat") -> None:
        # create a nested table for the timetable
        self.table = [[None for _ in range(periods)] for _ in range(days)]

        # create a list of days, corresponding to the table headers from startDay to endDay
        valid_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        self.days = [
            day
            for day in valid_days
            if valid_days.index(day) >= valid_days.index(startDay)
            and valid_days.index(day) <= valid_days.index(endDay)
        ]
        print(self.days)

    def add_day(self, day: str, classes: list[str]) -> None:
        """Function to add an entire day's timetable, as a list to the table."""
        for period, class_name in enumerate(classes):
            self.table[self.days.index(day)][period] = class_name

    def get_class(self, day: str, period: int) -> str:
        """Function to get a class, when given the day and period. Note period starts from 1, and NOT from 0."""
        period += 1

        if day not in self.days or period >= len(self.table[self.days.index(day)]):
            return None
        return self.table[self.days.index(day)][period]

    def to_dataframe(self) -> pd.DataFrame:
        """
        Convert the timetable to a Pandas DataFrame.

        Returns:
            A Pandas DataFrame with the following columns:
                - day: The day of the week.
                - period: The period of the day.
                - class_name: The name of the class.
        """

        df = pd.DataFrame(self.table)
        df.columns = ["day", "period", "class_name"]
        return df


if __name__ == "__main__":
    t = TimeTable(6, 8)
    t.add_day(
        "Mon",
        [
            "English",
            "Biology",
            "Math",
            "Chemistry",
            "Language",
            "History",
            "Maths",
            "English",
        ],
    )
    t.add_day(
        "Tue",
        [
            "English",
            "Yoga",
            "Math",
            "Physics",
            "Chemistry",
            "English",
            "Language",
            "History",
        ],
    )
    t.add_day(
        "Wed",
        [
            "English",
            "Geography",
            "Language",
            "Math",
            "IT",
            "Counselling",
            "Language",
            "Math",
        ],
    )
    t.add_day(
        "Thu",
        [
            "English",
            "History",
            "Geography",
            "PT",
            "Language",
            "Library/Art",
            "Math",
            "Math",
        ],
    )
    t.add_day(
        "Fri",
        [
            "English",
            "Math",
            "Language",
            "History",
            "Biology",
            "Physics",
            "IT",
            "Geography",
        ],
    )
    t.add_day(
        "Sat",
        [
            "English",
            "IT/PHY",
            "History/Math",
            "(PT/Yoga)/Geo",
            "Math/Bio",
            "Language/History",
            "Chemistry/IT",
            "Bonding/(PT/Yoga)",
        ],
    )

    t.get_class("Mon", 1)
    t.get_timetable_png()
