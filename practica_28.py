# Clase Pokemon
class Pokemon:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

# Clase Pokedex
class Pokedex:
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def search_pokemon_by_name(self, name):
        for pokemon in self.pokemon_list:
            if pokemon.get_name() == name:
                return pokemon
        return None

    def display_pokemon_details(self, pokemon):
        print("Name:", pokemon.get_name())
        print("Type:", pokemon.get_type())
        print("Description:", pokemon.get_description())

# Función para agregar un Pokémon de manera manual a la Pokédex
def add_pokemon_manually(pokedex):
    name = input("Enter the name of the Pokémon: ")
    type = input("Enter the type of the Pokémon: ")
    description = input("Enter the description of the Pokémon: ")

    new_pokemon = Pokemon(name, type, description)
    pokedex.add_pokemon(new_pokemon)

    print("Pokémon added successfully!")

# Función para crear un equipo Pokémon
def create_pokemon_team(pokedex):
    team = []
    team_size = int(input("Enter the size of the Pokémon team: "))

    for i in range(team_size):
        name = input("Enter the name of Pokémon {}: ".format(i + 1))
        pokemon = pokedex.search_pokemon_by_name(name)
        if pokemon:
            team.append(pokemon)
            print("Pokémon added to the team!")
        else:
            print("Pokémon not found in the Pokédex.")

    # Mostrar los detalles del equipo Pokémon
    print("Pokémon Team:")
    for pokemon in team:
        pokedex.display_pokemon_details(pokemon)
        print()

# Crear una instancia de la Pokedex
pokedex = Pokedex()
option = input("¿Quiere registrar pokemons nuevos? (S/N): ")

# Agregar algunos Pokémon a la Pokédex
while option.lower() == 's':
    add_pokemon_manually(pokedex)
    option = input("¿Quiere registrar pokemons nuevos? (S/N): ")

# Búsqueda y visualización de detalles de Pokémon
search_name = input("Enter the name of the Pokémon to search: ")
found_pokemon = pokedex.search_pokemon_by_name(search_name)

if found_pokemon:
    print("Pokémon found!")
    pokedex.display_pokemon_details(found_pokemon)
else:
    print("Pokémon not found.")

# crear equipo pokemon
create_pokemon_team(pokedex)
