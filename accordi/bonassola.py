"""Accordo Territoriale: Bonassola e altri 7 comuni (2018). Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Bonassola e altri 7 comuni (2018)'
COMUNI = 'Bonassola, Deiva Marina, Framura, Levanto, Monterosso al Mare, Portovenere, Riomaggiore, Vernazza'
FONTE = 'Accordo Territoriale microzona Bonassola, 2018 (data di deposito: da completare)'
VERIFICATO = False
DATA_ISTAT = '01/06/2021'
NOTE = ["Nella scansione di questo accordo non ho trovato l'Allegato 4 (elementi accessori): è usata la tabella degli altri accordi del 2018, da verificare."]

FASCE_PER_ZONA = {"U (unica)": {"MIN": (4.00, 7.00), "MEDIA": (4.50, 8.15), "MAX": (5.00, 9.00)}}
