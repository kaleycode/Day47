
beast = {}
def prettyPrint():
  print(f"\tName\t\tType \t  HP\t MP")
  print()
  for key, value in beast.items():
    print(f"""{key:^12}|{value["type"]:^10}|{value["hp"]:^6}|{value["mp"]:^6}""")
    print()
while True:
  print()
  print("Add your Beast!")
  print()
  name = input("Name > ").title()
  type = input("Type > ").title()
  hp = int(input("HP > "))
  mp = int(input("MP > "))
  beast[name] = { "type": type, "hp": hp, "mp": mp}
  print("-----------------------")
  print()
  prettyPrint()