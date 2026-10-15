import functools
import operator
from collections.abc import Callable
from typing import Any


_OPERATIONS: dict[str, Callable] = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min,
}


def spell_reducer(spells: list[int], operation: str) -> int:
    """Reduce a list of spell powers using the given operation."""
    if not spells:
        return 0
    if operation not in _OPERATIONS:
        raise ValueError(f"Unknown operation: '{operation}'")
    op = _OPERATIONS[operation]
    return functools.reduce(op, spells)


def partial_enchanter(
    base_enchantment: Callable
) -> dict[str, Callable]:
    """Return 3 specialized versions of base_enchantment via partial."""
    return {
        'fire': functools.partial(base_enchantment, power=50, element='fire'),
        'ice': functools.partial(base_enchantment, power=50, element='ice'),
        'lightning': functools.partial(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Return the nth Fibonacci number, with lru_cache memoization."""
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """Return a singledispatch function that handles int, str, and list."""

    @functools.singledispatch
    def dispatch(spell: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(target: str, power: int, element: str) -> str:
        cap = element.capitalize()
        return f"{cap} enchantment on {target} (power {power})"

    variants = partial_enchanter(base_enchant)
    for name, fn in variants.items():
        print(f"  {name}: {fn(target='Sword')}")

    print("\nTesting memoized fibonacci...")
    for n in [0, 1, 10, 15]:
        print(f"Fib({n}): {memoized_fibonacci(n)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["bolt", "heal", "shield"]))
    print(dispatch(3.14))
