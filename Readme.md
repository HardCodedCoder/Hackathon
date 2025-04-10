## Projektidee: Virtueller Buffet Bot

**Beschreibung:**  
Ein virtueller Roboter, dargestellt mit einfacher 2D-Grafik (z. B. Python Turtle, Pygame oder Unity), der Bestellungen vom Buffet entgegennimmt und diese an virtuelle Tische ausliefert.

### Team Mitglieder
- Hossein Amir
- Andreas Graf
- Gino Pensuni

### 🛠️ Technikstack:
- **Python** mit **Pygame** oder **Processing**
- Simuliertes Bewegungssystem mit einfacher Steuerungslogik
- GUI zur Auswahl von Speisen, die der Bot "holen" soll

### 🌟 Bonus-Features:
- Intelligente Pfadsuche mit **Dijkstra-Algorithmus** oder A*
- Einfache Animationen und **Soundeffekte**
- Visualisierte „Buffetstationen“ und Tische als Icons oder Blöcke
- Erweiterbar mit einer Punkte-/Gamification-Logik („Tisch 3 bekommt Bonus für schnellste Bedienung“)

---

## ✅ Anforderungen & Aufgabenverteilung

### Software & Tools
- Python 3.x
- Pygame (für 2D-Visualisierung)
- Optional: Tiled Map Editor (für Kartendesign)
- Entwicklungsumgebung: VS Code
- Git

### Python Dependencies
```bash
pip install pygame
```

---

## 📋 Taskliste für das Team

| Aufgabe | Beschreibung | Zeitaufwand | Schwierigkeit |
|--------|--------------|-------------|----------------|
| 🧱 Projektstruktur erstellen | Ordnerstruktur, main.py, Setup Pygame Loop | 30 min | 🟢 Einfach |
| 🎮 Spielfeld zeichnen | Einfache Karte mit Buffetstationen und Tischen | 30–45 min | 🟢 Einfach |
| 🤖 Bot-Bewegung | Steuerung oder automatische Bewegung des Bots | 45 min | 🟡 Mittel |
| 🍽️ GUI / Menü | Auswahl von Speisen zum Servieren | 30–45 min | 🟢 Einfach |
| 🧠 Pfadsuche (Bonus) | Dijkstra / A* für smarte Wege zum Tisch | 60–90 min | 🔴 Anspruchsvoll |
| 🔊 Sounds & Animationen | Einfache Sounds beim Servieren oder Bewegen | 20–30 min | 🟢 Einfach |
| 🖼️ Assets einfügen | Bilder für Bot, Buffet, Tische etc. | 20–30 min | 🟢 Einfach |
| 🧪 Testen & Debuggen | Funktionstest des Spiels | 30–45 min | 🟡 Mittel |
| 🧾 Präsentation vorbereiten | Slides, Demo-Script, Team vorstellen | 30–45 min | 🟢 Einfach |

---

### MVP-Ziele (Minimum Viable Product)
- Spielfeld mit Buffetstationen und Tischen
- Beweglicher Bot
- Auswahl eines Essens in der GUI
- Bot bringt das Essen an einen virtuellen Tisch
- Kurze visuelle oder akustische Rückmeldung
