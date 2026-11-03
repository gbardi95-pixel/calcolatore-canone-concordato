"""Accordo Territoriale: Sarzana. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Sarzana'
COMUNI = 'Sarzana'
FONTE = 'Accordo Territoriale Comune di Sarzana'
VERIFICATO = True
DATA_ISTAT = "01/07/2021"
NOTE = []

REGOLA_DUE_MEDIE_TRE_MINIME = False   # l'Allegato 3 di questo accordo non la prevede

FASCE_PER_ZONA = {
    "B1-B2-E2 (zona centrale, centrale esterna al centro storico, suburbana)": {"MIN": (4.00, 6.00), "MEDIA": (5.00, 8.00), "MAX": (6.00, 8.50)},
    "C1-D1 (zona semicentrale, periferica)": {"MIN": (4.00, 5.50), "MEDIA": (4.50, 6.00), "MAX": (5.00, 7.00)},
    "R1-R2 (zona extraurbana)": {"MIN": (4.00, 5.00), "MEDIA": (4.00, 5.50), "MAX": (5.00, 6.00)},
}
