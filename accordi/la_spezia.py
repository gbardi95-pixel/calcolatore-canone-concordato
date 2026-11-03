"""Accordo Territoriale: La Spezia, valido per contratti sottoscritti e registrati
dal 01/01/2026 al 31/12/2028. Letto dalla scansione in import/La Spezia e provincia;
superfici (art. 4), durata, storico e viabilità come Ameglia (letti nel documento)."""
from .ameglia import *  # noqa: F401,F403

NOME = "La Spezia (2026-2028)"
COMUNI = "La Spezia"
FONTE = "Accordo Territoriale Comune di La Spezia, valido dal 01/01/2026 al 31/12/2028"
VERIFICATO = True
DATA_ISTAT = None   # i valori valgono fino al 31/12/2028, poi le parti si riconvocano: nessun adeguamento ISTAT
NOTE = [
    "Zona B4-B5-B6: per tipologia edilizia (fino a 18 alloggi) e vetustà (fino a 100 anni) le soglie sono diverse "
    "(note con asterisco dell'Allegato 3). Per un edificio tra 50 e 100 anni in quella zona scegli «Oltre 15 e fino a 50 anni»: "
    "il testo indica la fascia MEDIA fino a 100 anni.",
]

REGOLA_DUE_MEDIE_TRE_MINIME = True

ARREDO = {
    "Non arredato": 0.0,
    "Mobilio necessario alla fruizione dell'alloggio (fino a +20%)": 20.0,
    "Completamente arredato, cucina con frigo, freezer, lavastoviglie, lavatrice, piano cottura, TV, forno (fino a +25%)": 25.0,
    "Ex locazione breve con annullamento del CIN, completamente arredato (fino a +30%)": 30.0,
}

TIPOLOGIA_EDILIZIA = {
    "Casa singola o bifamiliare": "MAX",
    "Unità con accesso indipendente o su scale con accesso fino a 12 alloggi (zona B4-B5-B6: fino a 18)": "MEDIA",
    "Unità su scala con più di 12 alloggi (zona B4-B5-B6: più di 18)": "MIN",
}
VETUSTA = {
    "Nuova costruzione o manutenzione straordinaria entro 15 anni, anche parziale se documentata da fatture": "MAX",
    "Oltre 15 e fino a 50 anni (zona B4-B5-B6: fino a 100 anni)": "MEDIA",
    "Oltre 50 anni": "MIN",
    "Integrale rifacimento documentato": "MAX",
}
ACCESSORI_DOTAZIONE = [
    ("posto_auto_aperto", "Posto auto all'aperto", False),
    ("spazio_esclusivo", "Spazio ad uso esclusivo", False),
    ("doppi_servizi", "Doppi servizi", False),
    ("terrazzi_balconi", "Terrazzi / balconi", False),
    ("cantina", "Cantina", True),
    ("terrazza_attico", "Terrazza sul piano attico", False),
]
SPAZI_COMUNI = {
    "Parco giochi": "MAX",
    "Attrezzature sportive fisse": "MAX",
    "Spazio condominiale di superficie superiore al 50% dell'area del fabbricato": "MAX",
    "Spazio condominiale tra il 50% e il 10% dell'area occupata dal fabbricato": "MEDIA",
    "Spazio condominiale inferiore al 10% dell'area del fabbricato": "MIN",
}
AUTORIMESSA = {
    "Due o più posti auto": "MAX",
    "Un solo posto auto": "MEDIA",
    "Assenza di autorimessa o box": "MIN",
}

ACCESSORI = [
    "Pavimenti in parquet (se presenti in sala e camere)", "Pavimenti in marmo o in cotto",
    "Finestre con doppi vetri in tutte le stanze", "Porta o serramenti blindati",
    "Serramenti interni di legno pregiato o vetro", "Parabola satellitare", "Impianto antifurto",
    "Impianto di videocitofono", "Rivestimento esterno del fabbricato in marmo o materiale pregiato",
    "Sistemi alternativi di riscaldamento", "Tapparelle motorizzate",
    "Inferriate di protezione (intero o parziale appartamento)", "Cancello elettrico",
    "Affreschi interni od esterni", "Impianto fotovoltaico", "Impianto solare termico",
    "Impianto geotermico", "Cappotto esterno o interno", "Rete wifi", "Certificazione energetica A B C D",
    "Doppi servizi", "Rinuncia alla cauzione e a qualsiasi forma di garanzia",
    "Riduzione del preavviso a 2 mesi senza gravi motivi", "Presenza di portiere",
]

# Allegato 2: €/m² al mese, per zona OMI (minimo, massimo) di ogni fascia
FASCE_PER_ZONA = {
    "B4-B5-B6-B7-C6": {"MIN": (2.32, 6.98), "MEDIA": (2.991, 8.73), "MAX": (3.80, 9.00)},
    "D9-D10": {"MIN": (2.32, 6.40), "MEDIA": (2.91, 7.57), "MAX": (3.48, 8.14)},
    "E6-E7": {"MIN": (2.32, 5.82), "MEDIA": (2.91, 6.98), "MAX": (3.48, 7.50)},
    "E8-R4": {"MIN": (2.32, 5.50), "MEDIA": (2.91, 6.50), "MAX": (3.48, 7.00)},
    "R6": {"MIN": (2.32, 7.45), "MEDIA": (2.91, 9.20), "MAX": (4.08, 11.00)},
    "R7": {"MIN": (2.32, 5.34), "MEDIA": (2.91, 6.40), "MAX": (3.48, 6.98)},
}
