import time
import functools
from collections.abc import Callable
from typing import Any


def spell_timer(func: Callable) -> Callable:
    """Decorator that measures and prints function execution time."""
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """Decorator factory that rejects calls where power < min_power."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None:
                power = args[-1] if args else 0
            if power < min_power:
                return "Insufficient power for this spell"
            return func(*args, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """Decorator factory that retries a spell up to max_attempts times."""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    """A guild that validates mage names and casts spells."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """Return True if name >= 3 chars and only letters/spaces."""
        return (
            len(name) >= 3
            and all(c.isalpha() or c.isspace() for c in name)
        )

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Cast a spell if power is sufficient."""
        return f"Successfully cast {spell_name} with {power} power"


def _demo_spell_timer() -> None:
    """Demo spell_timer decorator."""
    print("Testing spell timer...")

    @spell_timer
    def fireball(target: str) -> str:
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball("Dragon")
    print(f"Result: {result}")


def _demo_retry_spell() -> None:
    """Demo retry_spell decorator."""
    print("\nTesting retrying spell...")
    _state: dict[str, int] = {'count': 0}

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("always fails")

    print(always_fails())

    _state['count'] = 0

    @retry_spell(max_attempts=3)
    def eventually_works() -> str:
        _state['count'] += 1
        if _state['count'] < 3:
            raise RuntimeError("Not ready")
        return "Waaaaaaagh spelled !"

    print(eventually_works())


def _demo_mage_guild() -> None:
    """Demo MageGuild class."""
    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    _demo_spell_timer()
    _demo_retry_spell()
    _demo_mage_guild()
