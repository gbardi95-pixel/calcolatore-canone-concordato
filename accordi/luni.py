"""Accordo Territoriale: Luni. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Luni'
COMUNI = 'Luni'
FONTE = 'Accordo Territoriale Comune di Luni'
VERIFICATO = True
DATA_ISTAT = "01/07/2021"
NOTE = []

REGOLA_DUE_MEDIE_TRE_MINIME = False   # l'Allegato 3 di questo accordo non la prevede

FASCE_PER_ZONA = {
    "B1 (zona centrale)": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.80), "MAX": (5.00, 7.20)},
    "C1-C2-C3-D1-D2-R1 (zona semicentrale, periferica, extraurbana)": {"MIN": (4.00, 5.50), "MEDIA": (4.00, 6.00), "MAX": (4.50, 6.50)},
}
