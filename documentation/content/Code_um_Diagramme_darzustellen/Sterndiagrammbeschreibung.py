import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------------------------------
# Pfad-Setup
# ---------------------------------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# ---------------------------------------------------------------------------
# Kategorien und Achsenbeschriftungen (identisch zum Anforderungskatalog, Kap. 05)
# ---------------------------------------------------------------------------
categories = [
    'Systemarchitektur\n& Webintegration',
    'Konnektivität\ndes Webservers',
    'Robustheit &\nLeistungsfähigkeit',
    'Programmierbarkeit\nder HMI-Oberflächen',
    'Benutzer-\nfreundlichkeit',
    'Zukunfts-\nfähigkeit',
]
N = len(categories)

# ---------------------------------------------------------------------------
# Bewertungsdaten - synchronisiert mit den Tabellen in Kapitel 07 (Skala 0-5)
# ACHTUNG: Bei jeder Änderung dieser Werte müssen die zugehörigen LaTeX-Tabellen
# (ErfTF1810, tab:erfuellung_webiq, tab:erfuellung_tf2000, tab:erfuellung_eigen)
# entsprechend angepasst werden, damit Text und Grafik konsistent bleiben.
# ---------------------------------------------------------------------------
systems = {
    'TF1810\n(bisherige Lösung)': {
        'values': [2, 5, 5, 3, 2, 1],
        'color': '#E05C5C',
        'linestyle': '--',
    },
    'TF2000\n(Beckhoff Server-Client)': {
        'values': [5, 5, 5, 5, 5, 4],
        'color': '#2E7D32',
        'linestyle': '-',
    },
    'WebIQ\n(Beijer Electronics)': {
        'values': [5, 4, 4, 5, 5, 3],
        'color': '#1565C0',
        'linestyle': '-',
    },
    'Eigenentwicklung\n(OPC-UA-Gateway)': {
        'values': [2, 2, 2, 1, 1, 1],
        'color': '#F57F17',
        'linestyle': '-.',
    },
}

# ---------------------------------------------------------------------------
# Winkel für die Achsen berechnen
# ---------------------------------------------------------------------------
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]


# ---------------------------------------------------------------------------
# Hilfsfunktion: Einzelnes Sterndiagramm zeichnen
# ---------------------------------------------------------------------------
def draw_radar(ax, values, color, linestyle, title):
    """Zeichnet ein einzelnes Sterndiagramm auf die übergebene Polar-Achse."""
    values_plot = values + values[:1]

    for r in [1, 2, 3, 4, 5]:
        ring_vals = [r] * (N + 1)
        ax.plot(angles, ring_vals,
                color='grey', linewidth=0.4, linestyle=':', alpha=0.5)

    ax.fill(angles, values_plot, alpha=0.20, color=color)
    ax.plot(angles, values_plot,
            'o-', linewidth=2.0, color=color,
            linestyle=linestyle, markersize=5)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=7.5, color='black')

    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'], size=6.5, color='grey')

    ax.set_title(title, size=9, weight='bold', pad=14, color=color)

    ax.grid(True, linestyle='--', alpha=0.4)
    ax.spines['polar'].set_visible(False)


# ===========================================================================
# ABBILDUNG 1: Vier Einzeldiagramme im 2x2-Layout
# ===========================================================================
fig1, axes = plt.subplots(
    2, 2,
    figsize=(14, 12),
    subplot_kw=dict(projection='polar')
)
fig1.suptitle(
    'Bewertung der HMI-Lösungskonzepte anhand der Anforderungskategorien\n'
    '(Skala: 0 = nicht erfüllt, 5 = vollständig erfüllt)',
    fontsize=11, weight='bold', y=1.01
)

axes_flat = axes.flatten()
for idx, (name, data) in enumerate(systems.items()):
    draw_radar(
        ax=axes_flat[idx],
        values=data['values'],
        color=data['color'],
        linestyle=data['linestyle'],
        title=name,
    )

plt.tight_layout(pad=3.0)

filename_einzel = 'Sterndiagramme_Einzeln.pdf'
if os.path.exists(filename_einzel):
    os.remove(filename_einzel)
fig1.savefig(filename_einzel, bbox_inches='tight', dpi=300)
print(f'Einzeldiagramme gespeichert: {os.path.join(script_dir, filename_einzel)}')


# ===========================================================================
# ABBILDUNG 2: Kombiniertes Übersichtsdiagramm (alle Systeme überlagert)
# ===========================================================================
fig2, ax2 = plt.subplots(figsize=(9, 9), subplot_kw=dict(projection='polar'))

for r in [1, 2, 3, 4, 5]:
    ring_vals = [r] * (N + 1)
    ax2.plot(angles, ring_vals,
             color='grey', linewidth=0.4, linestyle=':', alpha=0.5)
    ax2.text(
        np.pi / 2, r + 0.05, str(r),
        ha='center', va='bottom', size=7, color='grey'
    )

legend_handles = []
for name, data in systems.items():
    values_plot = data['values'] + data['values'][:1]
    ax2.fill(angles, values_plot, alpha=0.10, color=data['color'])
    line, = ax2.plot(
        angles, values_plot,
        'o-', linewidth=2.0,
        color=data['color'],
        linestyle=data['linestyle'],
        markersize=5,
        label=name.replace('\n', ' ')
    )
    legend_handles.append(line)

ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, size=9, color='black')
ax2.set_ylim(0, 5)
ax2.set_yticks([])
ax2.grid(True, linestyle='--', alpha=0.4)
ax2.spines['polar'].set_visible(False)

ax2.legend(
    handles=legend_handles,
    loc='upper right',
    bbox_to_anchor=(1.35, 1.15),
    fontsize=8.5,
    frameon=True,
    framealpha=0.9,
    title='HMI-Systeme',
    title_fontsize=9,
)

plt.tight_layout()

filename_vergleich = 'Sterndiagramme_Vergleich.pdf'
if os.path.exists(filename_vergleich):
    os.remove(filename_vergleich)
fig2.savefig(filename_vergleich, bbox_inches='tight', dpi=300)
print(f'Vergleichsdiagramm gespeichert: {os.path.join(script_dir, filename_vergleich)}')

# plt.show()