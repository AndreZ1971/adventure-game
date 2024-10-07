# Die verlorene Schatzsuche

Die verlorene Schatzsuche ist ein textbasiertes Abenteuerspiel, in dem du durch verschiedene Räume gehst, Rätsel löst und am Ende einen Schatz findest. Ich erkläre dir hier, wie das Spiel funktioniert und was es alles kann.

## Funktionen
Es gibt verschiedene Funktionen im Spiel:

- **`greeting()`**: Begrüßt dich und erklärt, wie das Spiel läuft.
- **`enter_room(room)`**: Beschreibt, wie der Raum aussieht, in dem du dich befindest, und welche Aktionen möglich sind.
- **`solve_riddle(riddle)`**: Zeigt dir ein Rätsel und prüft, ob deine Antwort richtig ist.
- **`end_game()`**: Beendet das Spiel und verabschiedet sich.

Um den Code ordentlich zu halten, habe ich zwei Funktionen in eine separate Datei namens **`game_utils.py`** ausgelagert.

## Spielstruktur
Das Spiel hat mehrere Räume:

1. **Startbereich**: Hier beginnst du und kannst in zwei Richtungen gehen.
2. **Raum 1**: Dieser Raum enthält ein Rätsel, das du lösen musst, um weiterzukommen.
3. **Raum 2**: Ein weiterer Raum mit einem anderen Rätsel, das anders ist als im ersten Raum.
4. **Raum 3**: Der letzte Raum vor dem Schatz mit dem letzten Rätsel.
5. **Schatz**: Wenn du alle Rätsel gelöst hast, findest du hier den Schatz.

## Navigation
Du kannst dich mit Befehlen wie **„norden“, „süden“, „osten“** und **„westen“** durch die Räume bewegen.

## Erweiterungen (optional)
- **Inventarsystem**: Füge ein Inventar hinzu, damit du Gegenstände sammeln und verwenden kannst.
- **Punktesystem**: Implementiere ein Punktesystem, um deine Leistung zu bewerten.
- **Mehr Räume und Rätsel**: Erweitere das Spiel um weitere Räume und Rätsel, um es noch spannender zu machen.

## Fazit
Das Spiel zeigt dir, wie du Funktionen nutzt und wie du ein interaktives Programm entwickeln kannst. Es ist eine gute Übung, um die Strukturierung von Code und die Auslagerung in externe Dateien zu lernen.
