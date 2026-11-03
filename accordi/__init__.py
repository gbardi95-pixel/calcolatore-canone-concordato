"""Elenco degli accordi territoriali disponibili.

Per aggiungerne uno: copiare accordi/ameglia.py in un nuovo file, sostituire i
valori con quelli del nuovo accordo e registrarlo qui sotto (vedi README).
"""
from . import ameglia, arcola, bonassola, lerici, luni, ricco, santo_stefano_magra, sarzana

ACCORDI = {m.NOME: m for m in (
    ameglia, arcola, bonassola, lerici, luni, ricco, santo_stefano_magra, sarzana,
)}
