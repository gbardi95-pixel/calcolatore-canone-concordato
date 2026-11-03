"""Accordo Territoriale: Santo Stefano di Magra. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Santo Stefano di Magra'
COMUNI = 'Santo Stefano di Magra'
FONTE = 'Accordo Territoriale Comune di Santo Stefano Magra'
VERIFICATO = True
DATA_ISTAT = "01/07/2021"
NOTE = []

REGOLA_DUE_MEDIE_TRE_MINIME = False   # l'Allegato 3 di questo accordo non la prevede

FASCE_PER_ZONA = {
    "C1-B1 (zona centrale, semicentrale)": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.50), "MAX": (5.00, 7.00)},
    "D2-E1 (zona periferica, suburbana, Ponzano Superiore)": {"MIN": (4.00, 5.50), "MEDIA": (4.00, 6.00), "MAX": (4.50, 6.50)},
    "R1 (zona extraurbana)": {"MIN": (4.00, 5.00), "MEDIA": (4.50, 5.50), "MAX": (4.50, 6.00)},
}
