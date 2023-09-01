import matplotlib.pyplot as plt

# Funktion zur Erstellung eines benutzerdefinierten Balkendiagramms
def create_bar_chart():
    data = []
    labels = []

    num_bars = int(input("Gib die Anzahl der Balken ein: "))

    for i in range(num_bars):
        label = input(f"Gib die Bezeichnung für Balken {i + 1} ein: ")
        value = float(input(f"Gib den Wert für Balken {i + 1} ein: "))
        data.append(value)
        labels.append(label)

    plt.bar(labels, data)
    plt.xlabel("Bezeichnung")
    plt.ylabel("Wert")
    plt.title("Benutzerdefiniertes Balkendiagramm")
    plt.show()

# Hauptprogramm
if __name__ == "__main__":
    print("Willkommen zu einem Balkendiagramm-Generator!")

    create_bar_chart()
