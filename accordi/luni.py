"""Accordo Territoriale: Luni. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Luni'
COMUNI = 'Luni'
FONTE = 'Accordo Territoriale Comune di Luni (data di deposito: da completare)'
VERIFICATO = False
DATA_ISTAT = 'da completare'
NOTE = ['Criteri (Allegato 3), coefficienti di superficie e maggiorazioni non riletti per questo accordo: assunti uguali a quelli di Ameglia (stesso schema degli accordi 2018 della provincia).']

FASCE_PER_ZONA = {
    "B1": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.80), "MAX": (5.00, 7.20)},
    "C1-C2-C3-D1-D2-R1": {"MIN": (4.00, 5.50), "MEDIA": (4.00, 6.00), "MAX": (4.50, 6.50)},
}
