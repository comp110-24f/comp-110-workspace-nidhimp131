"""For loops Practice"""

pets: list[str] = ["Louie", "Bo", "Bear"]

for item in pets:
    print("Good boy, " + item + "!")


names: list[str] = ["Alyssa", "Janet", "Vrinda"]

for idx in range(0, len(names)):
    print(f"{idx}: {names[idx]}")
