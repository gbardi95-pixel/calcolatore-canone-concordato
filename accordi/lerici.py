"""Accordo Territoriale: Lerici (17/02/2018). Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = "Lerici"
COMUNI = "Lerici"
FONTE = "Accordo Territoriale Comune di Lerici, 17/02/2018"
VERIFICATO = True
DATA_ISTAT = "01/03/2021"
NOTE = []

REGOLA_DUE_MEDIE_TRE_MINIME = False   # l'Allegato 3 di questo accordo non la prevede
STORICO_VINCOLATO = 20.0              # art. 7: immobili storici vincolati +20%

# Art. 5: qui l'arredo dà al massimo +20% (nessun +30%)
ARREDO = {
    "Non arredato": 0.0,
    "Completamente arredato, cucina con frigo, lavatrice, lavastoviglie, cucina economica, TV (fino a +20%)": 20.0,
}

FASCE_PER_ZONA = {
    "B1-C1 (Lerici Capoluogo, San Terenzo)": {"MIN": (6.40, 7.40), "MEDIA": (7.50, 8.50), "MAX": (8.60, 9.60)},
    "B3 (Lerici, San Terenzo fronte a mare)": {"MIN": (7.20, 8.20), "MEDIA": (8.30, 9.30), "MAX": (9.40, 10.40)},
    "D1-R2-R3 (Muggiano, collina alta, fascia lungo Fiume Senato)": {"MIN": (3.20, 3.90), "MEDIA": (4.00, 4.60), "MAX": (4.70, 5.20)},
    "D2-D6-R1 (Solaro, Pugliola, Pozzuolo, Falconara, Santa Teresa, Zanego, Montemarcello, costa residuale)": {"MIN": (5.60, 6.60), "MEDIA": (6.70, 7.20), "MAX": (7.30, 8.00)},
    "D3 (Catene, Serra, collina Fiascherino-Tellaro)": {"MIN": (6.40, 7.40), "MEDIA": (7.50, 8.50), "MAX": (8.60, 10.40)},
    "D4 (Guercio)": {"MIN": (4.00, 4.40), "MEDIA": (4.50, 4.80), "MAX": (4.90, 5.20)},
    "D7 (fascia costiera da Maralunga a Tellaro)": {"MIN": (8.00, 9.00), "MEDIA": (9.10, 10.10), "MAX": (10.20, 11.20)},
}
