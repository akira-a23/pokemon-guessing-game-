import random

# ----------------------------
# ASCII Pokémon Database
# ----------------------------
POKEMON_LIST = [
    {"name": "pikachu", "art": r"""
 (\__/)
 (o^.^)
 z(_(")(")
""" , "hint": "Electric-type, evolves into a thunderbolt rat."},
    {"name": "charmander", "art": r"""
     _.--""`-..
   ,'          `.
 ,'          __  `.
|          (__)   |
|         _______ |
 \       `--. .-' /
  `._        `-'|
     `--.___,-'
""" , "hint": "Fire-type, has a flame on its tail."},
    {"name": "bulbasaur", "art": r"""
   /\__/\
  ( o.o  )
  > ^ <    (plant bulb on back)
""" , "hint": "Grass/Poison-type, has a bulb on its back that grows into a plant."},
    {"name": "squirtle", "art": r"""
    ____  
  /      \
 |  O  O |
 |   ∆   |
  \____/
   (____)
""" , "hint": "Water-type, starts with a turtle-like form."},
    {"name": "jigglypuff", "art": r"""
   ( .-. )
  ( (o o) )
   (  -  )
   /  _  \
  | (_)  |
""" , "hint": "Fairy-type, sings to put others to sleep."},
    {"name": "meowth", "art": r"""
   |\---/|
   | o_o |
    \_^_/   <--- meowth being sus
""" , "hint": "Normal-type, loves coins and has a big personality."},
    {"name": "psyduck", "art": r"""
   ( ._. )
   <( )__)>   <-- holding head
   (___)
""" , "hint": "Water-type, constantly has headaches."},
    {"name": "snorlax", "art": r"""
   zZZZz
  ( -.- )
  (  -  )___
  |     |___)
""" , "hint": "Normal-type, sleeps most of the time."},
    {"name": "eevee", "art": r"""
  (\__/)
  ( . .) 
  / >🍂   <-- floofy tail
""" , "hint": "Normal-type, has many evolutions."},
    {"name": "gengar", "art": r"""
   .-"      "-.
  /     o  o   \
 |     .----.   |
 \   '      '  /
  '-.______.-'
""" , "hint": "Ghost/Poison-type, has a mischievous smile."},
    {"name": "magikarp", "art": r"""
 ><(((º>
(   splash  )
 ><(((º>
""" , "hint": "Water-type, known for its evolution into Gyarados."},
    {"name": "cubone", "art": r"""
  (o_o)
  /| |\
 /_| |_\
  /   \    <-- bone helmet vibes
""" , "hint": "Ground-type, wears its mother’s skull as a helmet."},
]

# ----------------------------
# Random Messages
# ----------------------------
INTRO_MESSAGES = [
    "Who's That Pokémon!?",
    "A wild mystery appears!",
    "Can you guess the Pokémon?",
    "Name this shadowy figure!",
    "Time for a Poké-challenge!"
]

CORRECT_REACTIONS = [
    "✅ Correct! It's {}.",
    "🎉 Nice one! That was {}!",
    "💯 You're on fire — it's {}!",
    "🔥 Trainer of the year! {} it is!",
    "😎 You're built different. That was {}!"
]

WRONG_REACTIONS = [
    "❌ Oof, it's actually {}.",
    "😅 Not quite... it's {}!",
    "👀 Were you even trying? It's {}.",
    "🙃 You sure you're a real trainer? It was {}.",
    "🫣 So close (not really). It's {}."
]

# ----------------------------
# Game State (Pokemon Collection)
# ----------------------------
player_collection = []

# ----------------------------
# Game Logic
# ----------------------------
def get_random_pokemon():
    return random.choice(POKEMON_LIST)

def display_collection():
    print("\n--- Your Pokémon Collection ---")
    if player_collection:
        for pokemon in player_collection:
            print(f"- {pokemon.title()}")
    else:
        print("You haven't caught any Pokémon yet. Keep playing!")

def play_game():
    print("\n" + random.choice(INTRO_MESSAGES) + "\n")
    pokemon = get_random_pokemon()
    print(pokemon["art"])
    
    guess = input("\nYour guess: ").strip().lower()

    if guess == pokemon["name"]:
        # Add Pokémon to the collection
        if pokemon["name"] not in player_collection:
            player_collection.append(pokemon["name"])
            print("\n" + random.choice(CORRECT_REACTIONS).format(pokemon["name"].title()))
        else:
            print("\nYou already caught this one! It's {}.".format(pokemon["name"].title()))
    else:
        print("\n" + random.choice(WRONG_REACTIONS).format(pokemon["name"].title()))
        print("\nHint: " + pokemon["hint"])
    
    display_collection()

# ----------------------------
# Game Loop
# ----------------------------
if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing, Pokémon Master! 👋")
            break
y
