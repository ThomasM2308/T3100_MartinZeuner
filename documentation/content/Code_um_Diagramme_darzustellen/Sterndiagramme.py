import matplotlib.pyplot as plt
import numpy as np
import os

# Setze Working Directory auf den Ordner des Skripts
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Kategorien exakt entsprechend des Anforderungskatalogs aus Kapitel 05
categories = [
    'Systemarchitektur\nmit Webintegration',
    'Konnektivität des\nWebservers',
    'Robustheit und\nLeistungsfähigkeit',
    'Benutzerfreundliche\nErstellung der HMI-Oberflächen',
    'Benutzerfreundlichkeit\nbei der Bedienung',
    'Zukunftsfähigkeit'
]
N = len(categories)

# Bewertungen (0-5) je System, entnommen aus den Einzeltabellen in Kapitel 07
tf1810          = [2, 5, 5, 3, 2, 1]
webiq           = [5, 4, 4, 5, 5, 3]
tf2000          = [5, 5, 5, 5, 5, 4]
eigenentwicklung = [2, 2, 2, 1, 1, 1]

angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# 1x4 Layout (nebeneinander)
fig, axes = plt.subplots(1, 4, figsize=(16, 4), subplot_kw=dict(projection='polar'))

systems = [
    ('TF1810', tf1810, 'blue'),
    ('WebIQ', webiq, 'red'),
    ('TF2000', tf2000, 'green'),
    ('Eigenentwicklung', eigenentwicklung, 'orange')
]

for idx, (name, values, color) in enumerate(systems):
    ax = axes[idx]
    values_plot = values + values[:1]
    ax.plot(angles, values_plot, 'o-', linewidth=2, color=color)
    ax.fill(angles, values_plot, alpha=0.25, color=color)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=7)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_title(name, size=12, weight='bold')
    ax.grid(True)

plt.tight_layout()

# Bestehende Datei löschen, falls vorhanden
filename = 'Sterndiagramme_Vergleich.pdf'
if os.path.exists(filename):
    os.remove(filename)
    print(f"Alte Datei gelöscht: {filename}")

# Neue Datei speichern
plt.savefig(filename, bbox_inches='tight', dpi=300)
print(f"Sterndiagramme gespeichert in: {script_dir}")
# plt.show()