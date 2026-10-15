# ft_count_harvest_recursive.py
def print_days_recursive(current: int, total: int) -> None:
    if current > total:
        print("Harvest time!")
        return
    print(f"Day {current}")
    print_days_recursive(current + 1, total)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    print_days_recursive(1, days)
