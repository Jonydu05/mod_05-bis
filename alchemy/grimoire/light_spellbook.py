def light_spell_allowed_ingredients() -> list[str]:
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    valid_ingredients = validate_ingredients(ingredients)
    if valid_ingredients.find("INVALID"):
        return f"Spell rejected: {spell_name} ({valid_ingredients})"
    else:
        return f"Spell recorded: {spell_name} ({valid_ingredients})"
