"""Accordo Territoriale: Arcola. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Arcola'
COMUNI = 'Arcola'
FONTE = 'Accordo Territoriale Comune di Arcola (data di deposito: da completare)'
VERIFICATO = False
DATA_ISTAT = '30/06/2021'
NOTE = []

FASCE_PER_ZONA = {
    "B1-B2-D1 (centrale, suburbana, semicentrale)": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.80), "MAX": (5.00, 7.20)},
    "E1-R1 (semicentrale, periferica)": {"MIN": (4.00, 5.00), "MEDIA": (4.00, 5.50), "MAX": (4.50, 6.00)},
}
