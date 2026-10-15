#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = float(height)
        self.age = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age_day(self) -> None:
        self.age += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main():
    print("=== Garden Plant Growth ===")
    rose = Plant("Rose", 25.0, 30)
    rose.show()

    total_growth = 0.0
    for day in range(1, 8):
        print(f"=== Day {day} ===")
        initial_height = rose.height
        rose.grow()
        rose.age_day()
        rose.show()
        total_growth += (rose.height - initial_height)

    print(f"Growth this week: {round(total_growth, 1)}cm")


if __name__ == "__main__":
    main()
