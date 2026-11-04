def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    from alchemy.grimoire.dark_spellbook import dark_spell_record
    spell = dark_spell_record("Misterio", "bats, arsenic and eyeball")
    print(f"Testing record dark spell: {spell}")


if __name__ == "__main__":
    main()
