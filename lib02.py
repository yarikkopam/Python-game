import dungeon

if __name__ == "__main__":
    rounds, won, hp, loot = dungeon.fight("скелет", 100, 0, 20.5, 41.0)
    print(f"self-test: {len(rounds)} rounds, won={won}, loot={loot}")
