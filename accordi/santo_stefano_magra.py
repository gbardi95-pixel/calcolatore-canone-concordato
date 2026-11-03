"""Accordo Territoriale: Santo Stefano di Magra. Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Santo Stefano di Magra'
COMUNI = 'Santo Stefano di Magra'
FONTE = 'Accordo Territoriale Comune di Santo Stefano Magra (data di deposito: da completare)'
VERIFICATO = False
DATA_ISTAT = 'da completare'
NOTE = ['Criteri (Allegato 3), coefficienti di superficie e maggiorazioni non riletti per questo accordo: assunti uguali a quelli di Ameglia (stesso schema degli accordi 2018 della provincia).', 'Zona R1, fascia MEDIA: valore minimo 4,5 letto dalla scansione (più alto che nelle altre zone), da verificare.']

FASCE_PER_ZONA = {
    "C1-B1": {"MIN": (4.00, 6.00), "MEDIA": (4.50, 6.50), "MAX": (5.00, 7.00)},
    "D2-E1": {"MIN": (4.00, 5.50), "MEDIA": (4.00, 6.00), "MAX": (4.50, 6.50)},
    "R1": {"MIN": (4.00, 5.00), "MEDIA": (4.50, 5.50), "MAX": (4.50, 6.00)},
}
