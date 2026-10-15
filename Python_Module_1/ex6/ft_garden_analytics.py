#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float = 0.0, age: int = 0) -> None:
        self.name = name
        self.height = float(height)
        self.age = age
        self._stats = self.Stats()

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)
        self._stats.grow_count += 1

    def age_day(self) -> None:
        self.age += 1
        self._stats.age_count += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        self._stats.show_count += 1

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def create_anonymous(cls):
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0

        def display(self, extra: str = "") -> None:
            print(f"Stats: {self.grow_count} grow, {self.age_count} age, "
                  f"{self.show_count} show{extra}")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color.lower()}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_count = 0

    def produce_shade(self) -> None:
        self.shade_count += 1
        print(f"Tree {self.name} now produces a shade of {self.height}cm "
              f"long and {self.trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self.seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.seeds}")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    if isinstance(plant, Tree):
        extra = f" {plant.shade_count} shade"
        plant._stats.display(extra)
    else:
        plant._stats.display()


def main():
    print("=== Garden statistics ===")

    print("=== Check year-old ===")
    print("Is 30 days more than a year? ->", Plant.is_older_than_year(30))
    print("Is 400 days more than a year? ->", Plant.is_older_than_year(400))

    print("\n=== Flower ===")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)

    print("\n=== Tree ===")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_stats(oak)

    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)

    print("\n=== Seed ===")
    sunflower = Seed("Sunflower", 80.0, 45, "Yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_day()
    sunflower.bloom()
    sunflower.show()
    display_plant_stats(sunflower)

    print("\n=== Anonymous ===")
    unknown = Plant.create_anonymous()
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    main()
