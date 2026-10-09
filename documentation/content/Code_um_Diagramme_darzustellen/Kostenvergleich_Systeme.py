import matplotlib.pyplot as plt
import numpy as np
import os

# Setze Working Directory auf den Ordner des Skripts
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# -------------------------------------------------------
# Kostendaten der vier HMI-Systeme
# Einmalkosten:        Lizenz + Einarbeitung bestehendes Personal
# Laufend pro Monat:   (Jährl. Folgekosten ohne Risiko) / 12
# Risiko pro Monat:    Stillstandskosten (Fehlerrate x Dauer x Pauschale)
# -------------------------------------------------------
systems = {
    'TF1800 / TF1810': {
        'einmal':            326.20,       # Lizenz (163,10 €) + 0 € Einarbeitung
        'laufend_pro_monat': 600 / 12,    # 600 €/Jahr (Wartung + Personal)
        'color':             '#2196F3',    # Blau
        'marker':            'o'
    },
    'WebIQ (Smart HMI)': {
        'einmal':            7507,         # 1.385 + 122 + 6.000 €
        'laufend_pro_monat': 2380 / 12,    # 380 + 2.000 + 2.400 €/Jahr
        'color':             '#F44336',    # Rot
        'marker':            's'
    },
    'TF2000': {
        'einmal':            5283,         # 783 + 2.100 €
        'laufend_pro_monat': 1500 / 12,    # 700 + 1.200 €/Jahr
        'color':             '#4CAF50',    # Grün
        'marker':            '^'
    },
    'Eigenentwicklung': {
        'einmal':            10622,        # 122 + 10.500 €
        'laufend_pro_monat': 3500 / 12,    # 3.500 + 3.600 €/Jahr
        'color':             '#9C27B0',    # Lila
        'marker':            'd'
    }
}

# Zeitrahmen: 0 bis 24 Monate
monate = np.arange(0, 25, 1)

# -------------------------------------------------------
# Plot erstellen
# -------------------------------------------------------
fig, ax = plt.subplots(figsize=(12, 7))

for name, data in systems.items():
    kosten = np.zeros_like(monate, dtype=float)
    kosten[0] = data['einmal']
    for m in range(1, len(monate)):
        kosten[m] = (data['einmal']
                     + m * data['laufend_pro_monat'])
                     #+ m * data['risiko_pro_monat'] )

    ax.plot(monate, kosten,
            marker=data['marker'],
            linestyle='-',
            linewidth=2,
            label=name,
            color=data['color'],
            markevery=2,
            markersize=6)

# -------------------------------------------------------
# Achsenbeschriftung und Formatierung
# -------------------------------------------------------
ax.set_xlabel('Zeit in Monaten', fontsize=12, weight='bold')
ax.set_ylabel('Summierte Gesamtkosten (€)', fontsize=12, weight='bold')
ax.set_title('Kostenvergleich der HMI-Lösungen über 24 Monate',
             fontsize=14, weight='bold')
ax.legend(loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax.yaxis.set_major_formatter(
    plt.FuncFormatter(lambda x, p: f'€{int(x/1000)}k')
)

ax.set_xticks(np.arange(0, 25, 2))
ax.set_xlim(0, 24)
ax.set_ylim(bottom=0)

plt.tight_layout()

# -------------------------------------------------------
# Speichern als PDF
# -------------------------------------------------------
filename = 'Kostenvergleich_Systeme.pdf'
if os.path.exists(filename):
    os.remove(filename)
    print(f"Alte Datei gelöscht: {filename}")

plt.savefig(filename, bbox_inches='tight', dpi=300)
print(f"Kostenvergleich gespeichert in: {script_dir}")