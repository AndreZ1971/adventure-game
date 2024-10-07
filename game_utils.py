# game_utils.py

def solve_riddle(riddle, correct_answer):
    print("\nRätsel: ", riddle)
    answer = input("Deine Antwort: ").strip().lower()
    if answer == correct_answer.lower():
        print("Richtig! Du kannst weitermachen.")
        return True
    else:
        print("Falsch! Die Antwort war: ", correct_answer)
        return False

def end_game():
    print("Danke fürs Spielen! Auf Wiedersehen.")
    exit()
