"""Accordo Territoriale: Riccò del Golfo e altri 13 comuni (2018). Valori letti dalla scansione in
import/La Spezia e provincia; il resto delle regole è ereditato da Ameglia."""
from .ameglia import *  # noqa: F401,F403

NOME = 'Riccò del Golfo e altri 13 comuni (2018)'
COMUNI = 'Riccò del Golfo, Beverino, Varese Ligure, Sesta Godano, Brugnato, Calice al Cornoviglio, Borghetto Vara, Rocchetta Vara, Maissana, Pignone, Carro, Zignago, Carrodano, Follo'
FONTE = 'Accordo Territoriale microzona Riccò del Golfo, 2018'
VERIFICATO = True
DATA_ISTAT = '15/07/2021'
NOTE = []

FASCE_PER_ZONA = {"U (unica)": {"MIN": (4.00, 7.00), "MEDIA": (4.50, 8.15), "MAX": (5.00, 9.00)}}
