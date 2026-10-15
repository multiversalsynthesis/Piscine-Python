import random
from typing import Generator, Tuple, List


def gen_event() -> Generator[Tuple[str, str], None, None]:
    """Endless generator for game events."""
    players: List[str] = ["bob", "alice", "dylan", "charlie"]
    actions: List[str] = [
        "run", "eat", "sleep",
        "grab", "move", "climb", "swim", "release", "use"
    ]
    while True:
        name: str = random.choice(players)
        action: str = random.choice(actions)
        yield (name, action)


def consume_event(
    events: List[Tuple[str, str]]
) -> Generator[Tuple[str, str], None, None]:
    """Consume events randomly from list."""
    while events:
        idx: int = random.randint(0, len(events) - 1)
        event: Tuple[str, str] = events.pop(idx)
        yield event


def main() -> None:
    """Data stream processor."""
    print("=== Game Data Stream Processor ===")

    event_gen = gen_event()

    print("First 15 events (sample):")
    for i in range(15):
        event: Tuple[str, str] = next(event_gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    # List of 10
    events_list: List[Tuple[str, str]] = [
        next(event_gen) for _ in range(10)
    ]
    print(f"\nBuilt list of 10 events: {events_list}")

    # Consume
    consumer = consume_event(events_list)
    print("\nConsuming events:")
    for _ in range(len(events_list) + 2):  # extra to show empty
        try:
            event = next(consumer)
            print(f"Got event from list: {event}")
            print(f"Remains in list: {events_list}")
        except StopIteration:
            print("No more events.")
            break


if __name__ == "__main__":
    main()
