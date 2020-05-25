class Mineral:
    geology = 'igneous'
    material = 'solid'
    planet = 'Earth'
    

    def rockQuiz(self):
        entry_geology = input("Enter mineral's geology: ")
        entry_material = input("Enter material's type: ")
        entry_planet = Mineral.planet
        if (entry_geology == self.geology and entry_material == self.material):
            print("The mineral is from: {}!".format(entry_planet))
        else:
            print("The mineral is not from Earth.")
            


class Carbonate(Mineral):
    geology = 'sedimentary'
    hardness = '3'
    name = 'Barite'
    

    def rockQuiz(self):
        entry_geology = input("Enter mineral's geology: ")
        entry_hardness = input("Enter material's hardness: ")
        entry_name = Carbonate.name
        if (entry_geology == self.geology and entry_hardness == self.hardness):
            print("The mineral is: {}!".format(entry_name))
        else:
            print("The mineral is not Barite.")
            


class Silicate(Mineral):
    geology = 'metamorphic'
    color = 'red'
    location = 'Schist'
    name = 'Garnet'
    

    def rockQuiz(self):
        entry_geology = input("Enter mineral's geology: ")
        entry_color = input("Enter material's color: ")
        entry_location = input("Rock matrix type: ")
        entry_name = Silicate.name
        if (entry_geology == self.geology and entry_color == self.color and entry_location == self.location):
            print("The mineral is: {}!".format(entry_name))
        else:
            print("The mineral is not Garnet.")


rock = Mineral()
rock.rockQuiz()

carb = Carbonate()
carb.rockQuiz()

silica = Silicate()
silica.rockQuiz()




