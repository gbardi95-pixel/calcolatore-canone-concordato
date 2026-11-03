"""Accordo Territoriale: Sarzana. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Sarzana'
COMUNI = 'Sarzana'
FONTE = 'Accordo Territoriale Comune di Sarzana (data di deposito: da completare)'
VERIFICATO = False
DATA_ISTAT = 'da completare'
NOTE = ['Criteri (Allegato 3), coefficienti di superficie e maggiorazioni non riletti per questo accordo: assunti uguali a quelli di Ameglia (stesso schema degli accordi 2018 della provincia).']

FASCE_PER_ZONA = {
    "B1-B2-E2": {"MIN": (4.00, 6.00), "MEDIA": (5.00, 8.00), "MAX": (6.00, 8.50)},
    "C1-D1": {"MIN": (4.00, 5.50), "MEDIA": (4.50, 6.00), "MAX": (5.00, 7.00)},
    "R1-R2": {"MIN": (4.00, 5.00), "MEDIA": (4.00, 5.50), "MAX": (5.00, 6.00)},
}
