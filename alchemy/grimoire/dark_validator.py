from dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed_ingredients = dark_spell_allowed_ingredients()
    ingredients = ingredients.lower()
    is_valid = any(item in ingredients for item in allowed_ingredients)
    status = "VALID" if is_valid else "INVALID"
    return f"{allowed_ingredients} - {status}"
