# main.py
from game_utils import solve_riddle, end_game

# Liste der Räume
rooms = {
    "start": {
        "description": "Du bist im Startbereich. Du siehst Türen nach Norden und Osten.",
        "exits": {"norden": "raum1", "osten": "raum2"}
    },
    "raum1": {
        "description": "Du betrittst Raum 1. Es ist dunkel und ein Rätsel erwartet dich.",
        "riddle": "Was hat Flügel und kann doch nicht fliegen?",
        "answer": "Eine Tür",
        "exits": {"süden": "start", "osten": "raum3"}
    },
    "raum2": {
        "description": "Du bist in Raum 2. Hier gibt es einen weiteren Hinweis.",
        "riddle": "Je mehr du wegnimmst, desto größer werde ich. Was bin ich?",
        "answer": "Ein Loch",
        "exits": {"westen": "start"}
    },
    "raum3": {
        "description": "Du hast Raum 3 erreicht. Der Schatz ist nah!",
        "riddle": "Was kann brechen, ohne gehalten zu werden?",
        "answer": "Ein Versprechen",
        "exits": {"westen": "raum1", "süden": "schatz"}
    },
    "schatz": {
        "description": "Herzlichen Glückwunsch! Du hast den Schatz gefunden!",
        "exits": {}
    }
}

# Begrüßungsfunktion
def greeting():
    print("Willkommen bei 'Die verlorene Schatzsuche'!")
    print("Navigiere durch die Räume, löse Rätsel und finde den Schatz.")
    print("Verwende Befehle wie 'norden', 'süden', 'osten', 'westen', um dich zu bewegen.\n")

# Funktion zum Betreten eines Raums
def enter_room(room):
    current_room = rooms[room]
    print(current_room["description"])
    
    if "riddle" in current_room:
        if not solve_riddle(current_room["riddle"], current_room["answer"]):
            print("Du bist gescheitert. Das Spiel endet hier.")
            end_game()
            return False

    return True

def main():
    greeting()
    current_location = "start"
    
    while True:
        if current_location == "schatz":
            print("Du hast das Spiel gewonnen! Der Schatz gehört dir!")
            end_game()
            break
        
        # Betritt den aktuellen Raum
        if not enter_room(current_location):
            break
        
        # Benutzer nach der nächsten Aktion fragen
        direction = input("\nIn welche Richtung möchtest du gehen? ").strip().lower()
        if direction in rooms[current_location]["exits"]:
            current_location = rooms[current_location]["exits"][direction]
        else:
            print("Diese Richtung ist nicht möglich. Versuche eine andere Richtung.")
