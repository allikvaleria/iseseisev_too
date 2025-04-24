class Player:
    def __init__(self, hp, energy, food):
        self.hp = hp         
        self.energy = energy  
        self.food = food     

    def rest(self):
        if self.food > 0:
            self.food -= 1
            self.energy += 3
            print("Sa puhkasid. Energia +3.")
        else:
            print("Sul ei ole piisavalt toitu, et puhata.")

    def search_food(self):
        print("Sa otsid toitu...")
        self.energy -= 2
        if self.energy <= 0:
            print("Sa oled liiga väsinud ja ei leidnud midagi.")
            return
        self.food += 1
        print("Sa leidsid ühe toidu!")

    def show_status(self):
        print(f"Tervis: {self.hp}")
        print(f"Energia: {self.energy}")
        print(f"Toit: {self.food}")

    def is_alive(self):
        return self.hp > 0 and self.energy > 0


# Mängutsükkel
player = Player(10, 5, 3)

while player.is_alive():
    player.show_status()
    print("\nVali tegevus:")
    print("1 - Puhka")
    print("2 - Otsi toitu")
    print("3 - Jäta vahele")

    choice = input("Sinu valik: ")
    if choice == "1":
        player.rest()
    elif choice == "2":
        player.search_food()
    elif choice == "3":
        player.energy -= 1
        print("Sa ei teinud midagi. Energia -1.")
    else:
        print("Vigane valik. Sa kaotasid 1 energia.")
        player.energy -= 1

print("\nSa ei jäänud ellu. Puhastusöö sai sind kätte.")