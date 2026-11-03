"""Accordo Territoriale: Arcola. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Arcola'
COMUNI = 'Arcola'
FONTE = 'Accordo Territoriale Comune di Arcola'
VERIFICATO = True
DATA_ISTAT = '30/06/2021'
NOTE = []

REGOLA_DUE_MEDIE_TRE_MINIME = False   # l'Allegato 3 di questo accordo non la prevede

FASCE_PER_ZONA = {
    "B1-B2-D1 (centrale, suburbana, semicentrale)": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.80), "MAX": (5.00, 7.20)},
    "E1-R1 (semicentrale, periferica)": {"MIN": (4.00, 5.00), "MEDIA": (4.00, 5.50), "MAX": (4.50, 6.00)},
}
