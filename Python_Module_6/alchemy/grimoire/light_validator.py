LIGHT_ALLOWED: list[str] = ["earth", "air", "fire", "water"]


def validate_ingredients(ingredients: str) -> str:
    lower = ingredients.lower()
    for ingredient in LIGHT_ALLOWED:
        if ingredient in lower:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
