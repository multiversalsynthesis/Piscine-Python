from ex1 import (
    HealingCreatureFactory,
    TransformCreatureFactory,
    HealCapability,
    TransformCapability,
)
from ex0.creature import Creature


def test_healing(factory: HealingCreatureFactory) -> None:
    print("Testing Creature with healing capability")
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        print(creature.attack())
        if isinstance(creature, HealCapability):
            print(creature.heal())


def test_transform(factory: TransformCreatureFactory) -> None:
    print("Testing Creature with transform capability")
    for label, creature in [
        ("base", factory.create_base()),
        ("evolved", factory.create_evolved()),
    ]:
        print(f" {label}:")
        print(creature.describe())
        if isinstance(creature, (Creature, TransformCapability)):
            print(creature.attack())  # type: ignore[union-attr]
        if isinstance(creature, TransformCapability):
            print(creature.transform())
            print(creature.attack())  # type: ignore[union-attr]
            print(creature.revert())


if __name__ == "__main__":
    heal_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    test_healing(heal_factory)
    print()
    test_transform(transform_factory)
