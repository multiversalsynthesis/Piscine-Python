import sys
from typing import Dict, List


def main() -> None:
    """Inventory system."""
    print("=== Inventory System Analysis ===")

    if len(sys.argv) < 2:
        print("No items provided.")
        return

    inventory: Dict[str, int] = {}

    for arg in sys.argv[1:]:
        if ':' not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            item, qty_str = arg.split(':', 1)
            qty: int = int(qty_str)
            if item in inventory:
                print(f"Redundant item '{item}' - discarding")
            else:
                inventory[item] = qty
        except ValueError:
            print(f"Quantity error for '{arg}': invalid literal for int()")

    if not inventory:
        print("No valid inventory items.")
        return

    print(f"Got inventory: {inventory}")

    item_list: List[str] = list(inventory.keys())
    print(f"Item list: {item_list}")

    total_qty: int = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_qty}")

    for item, qty in inventory.items():
        percentage: float = (qty / total_qty) * 100 if total_qty > 0 else 0
        print(f"Item {item} represents {percentage:.1f}%")

    # Most and least
    if inventory:
        m_item = max(inventory, key=inventory.get)  # type: ignore
        l_item = min(inventory, key=inventory.get)  # type: ignore
        print(
            f"Item most abundant: {m_item} with quantity {inventory[m_item]}"
        )
        print(
            f"Item least abundant: {l_item} with quantity {inventory[l_item]}"
        )

    # Add new item
    inventory["magic_item"] = 1
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
