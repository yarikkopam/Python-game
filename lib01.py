import dungeon

rounds, won, health, loot = dungeon.fight("скелет", 100, 0, 20.5, 41.0)
hit, crit = dungeon.hero_hit(3, 20.5, 41.0)
gold, ok = dungeon.buy(dungeon.prices["зелье"], 50)

print(f"rounds={len(rounds)} won={won} health={health} loot={loot}")
print(f"hit={hit} crit={crit}")
print(f"gold={gold} ok={ok}")
