from typing import List, Tuple
from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    DefensiveStrategy,
)

Opponent = Tuple[CreatureFactory, BattleStrategy]


def battle(opponents: List[Opponent]) -> None:
    creatures = [
        (factory.create_base(), strategy)
        for factory, strategy in opponents
    ]

    names = [
        f"({c.name}+{s.__class__.__name__.replace('Strategy', '')})"
        for c, s in creatures
    ]
    print(f" {names}")
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")

    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature_a, strategy_a = creatures[i]
            creature_b, strategy_b = creatures[j]
            print()
            print("* Battle *")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    battle([(flame_factory, normal), (heal_factory, defensive)])

    print()
    print("Tournament 1 (error)")
    battle([(flame_factory, aggressive), (heal_factory, defensive)])

    print()
    print("Tournament 2 (multiple)")
    battle([
        (aqua_factory, normal),
        (heal_factory, defensive),
        (transform_factory, aggressive),
    ])
