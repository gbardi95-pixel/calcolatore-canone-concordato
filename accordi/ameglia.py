"""Parametri dell'Accordo Territoriale per i Comuni di Ameglia, Bolano,
Castelnuovo Magra e Vezzano Ligure (L. 431/98, D.M. 16/01/2017).

Fonte: import/La Spezia e provincia/MicrozonaAmeglia_2018-ACCORDO-TERRITORIALE.pdf
(scansione letta a mano). In vigore dal 15/07/2018, durata 3 anni, poi fino al
nuovo accordo. Valori delle fasce (Allegato 2) confermati dal proprietario del
progetto; nessun accordo più recente risulta stipulato (3/11/2026).
"""

NOME = "Ameglia, Bolano, Castelnuovo Magra, Vezzano Ligure (2018)"
COMUNI = "Ameglia, Bolano, Castelnuovo Magra, Vezzano Ligure"
DATA_ISTAT = "15/07/2021"   # da quando i valori delle fasce si aggiornano al 100% ISTAT (art. 3)
NOTE: list[str] = []         # avvertenze mostrate nell'app
VERIFICATO = True
FONTE = ("Accordo Territoriale Ameglia/Bolano/Castelnuovo Magra/Vezzano Ligure, "
         "in vigore dal 15/07/2018 (data di deposito: da completare)")

CATEGORIE_CATASTALI = {
    "A/2": {"nome": "Abitazioni di tipo civile", "ammesso": True, "desc": "Fabbricati di tipo economico o medio dotati di buone finiture e impianti standard."},
    "A/3": {"nome": "Abitazioni di tipo economico", "ammesso": True, "desc": "Fabbricati con finiture e impianti di modesta entità."},
    "A/4": {"nome": "Abitazioni di tipo popolare", "ammesso": True, "desc": "Fabbricati con strutture e finiture di modesto livello."},
    "A/5": {"nome": "Abitazioni di tipo ultrapopolare", "ammesso": True, "desc": "Alloggi di ridottissimo livello abitativo e con servizi minimi."},
    "A/6": {"nome": "Abitazioni di tipo rurale", "ammesso": True, "desc": "Fabbricati a servizio delle attività agricole."},
    "A/7": {"nome": "Abitazioni in villini", "ammesso": True, "desc": "Fabbricato anche suddiviso in più unità con giardino o spazi verdi pertinenziali."},
    "A/1": {"nome": "Abitazioni di tipo signorile", "ammesso": True, "desc": "Prevista dall'Allegato 3 (riga «A/1 - A/7»): fascia MAX per il criterio catastale."},
    "A/11": {"nome": "Abitazioni ed alloggi tipici dei luoghi", "ammesso": False, "desc": "NON PREVISTA: la tabella catastale dell'accordo arriva fino ad A/7."},
    "A/8": {"nome": "Abitazioni in ville", "ammesso": False, "desc": "NON PREVISTA: la tabella catastale dell'accordo arriva fino ad A/7."},
    "A/9": {"nome": "Castelli e palazzi storici", "ammesso": False, "desc": "NON PREVISTA: la tabella catastale dell'accordo arriva fino ad A/7."},
}

# ---- Art. 4: superficie locativa --------------------------------------
# Coefficiente sulla superficie calpestabile dell'abitazione
SOGLIA_PICCOLO_MQ = 46.0     # sotto: coefficiente 1,20, con tetto 50,6 m²
COEFF_PICCOLO, TETTO_PICCOLO = 1.20, 50.6
SOGLIA_MEDIO_MQ = 70.0       # da 46 a 70: coefficiente 1,10, con tetto 70 m²; sopra: 1,00
COEFF_MEDIO, TETTO_MEDIO = 1.10, 70.0
COEFF_CANTINA = 0.25
COEFF_BALCONI = 0.25            # sottotetti solo se alti almeno 1,70 m nel punto più basso
COEFF_AREA_SCOPERTA = 0.15      # fino alla superficie dell'abitazione
COEFF_POSTO_AUTO_COMUNE = 0.20
COEFF_AUTORIMESSA = 0.50
COEFF_VERDE_CONDOMINIO = 0.10   # quota millesimale, fino alla superficie dell'abitazione

# ---- Allegato 2: fasce €/m² al mese, per zona (qui area omogenea unica "U") ----
FASCE_PER_ZONA = {
    "U (unica)": {
        "MIN": (4.00, 7.00),
        "MEDIA": (4.50, 8.15),
        "MAX": (5.00, 9.00),
    },
}

# ---- Art. 5 e art. 7: maggiorazioni/riduzioni sul canone base ----------
ARREDO = {
    "Non arredato": 0.0,
    "Mobilio completo (fino a +20%)": 20.0,
    "Completamente arredato, cucina con frigo, freezer, lavastoviglie, lavatrice, piano cottura, TV, forno (fino a +30%)": 30.0,
}
VIABILITA_TRAFFICO = -10.0
DURATA = {
    "3 anni (3+2)": 0.0,
    "4 anni (4+2): +2%": 2.0,
    "Oltre 4 anni (5+2, 6+2...): +8%": 8.0,
}
STORICO_VINCOLATO = 10.0

# ---- Allegato 4: elementi accessori (pregi) ---------------------------
ACCESSORI = [
    "Pavimenti in parquet", "Pavimenti in marmo o in cotto",
    "Finestre con doppi vetri in tutte le stanze", "Porta o serramenti blindati",
    "Serramenti interni di legno pregiato", "Parabola satellitare", "Impianto antifurto",
    "Impianto di videocitofono", "Rivestimento esterno del fabbricato in marmo o materiale pregiato",
    "Sistemi alternativi di riscaldamento", "Tapparelle elettriche", "Inferriate di protezione",
    "Cancello elettrico", "Affreschi interni od esterni", "Impianto fotovoltaico",
    "Impianto solare termico", "Impianto geotermico", "Cappotto esterno o interno", "Rete wifi",
    "Certificazione energetica A B C D", "Doppi servizi",
    "Rinuncia alla cauzione e a qualsiasi forma di garanzia",
    "Riduzione del preavviso a 2 mesi senza gravi motivi",
]
# (numero minimo di elementi, % di aumento), dal più alto al più basso
SOGLIE_ACCESSORI = [(4, 15.0), (3, 10.0), (2, 5.0)]

# ---- Allegato 3: criteri per la fascia (MIN / MEDIA / MAX) -------------
TIPOLOGIA_EDILIZIA = {
    "Casa singola o bifamiliare": "MAX",
    "Unità con accesso indipendente o su scala con accesso fino a 12 alloggi": "MEDIA",
    "Unità su scala con più di 12 alloggi": "MIN",
}
TIPOLOGIA_CATASTALE = {
    "A/1": "MAX", "A/7": "MAX", "A/2": "MAX", "A/3": "MEDIA",
    "A/4": "MIN", "A/5": "MIN", "A/6": "MIN",
}
VETUSTA = {
    "Nuova costruzione o manutenzione straordinaria entro 15 anni": "MAX",
    "Oltre 15 e fino a 50 anni": "MEDIA",
    "Oltre 50 anni": "MIN",
    "Integrale rifacimento documentato": "MAX",
}
# Accessori in dotazione: (chiave, etichetta, escluso per A/7)
ACCESSORI_DOTAZIONE = [
    ("posto_auto_interno", "Posto auto interno e/o autorimessa uso esclusivo", False),
    ("posto_auto_esterno", "Posto auto esterno esclusivo", True),
    ("area_esclusiva", "Area ad uso esclusivo", True),
    ("doppi_servizi", "Doppi servizi", False),
    ("terrazzi", "Terrazzi", False),
    ("soffitta_cantina", "Soffitta o cantina", True),
    ("terrazza_attico", "Terrazza sul piano attico", False),
]
SPAZI_COMUNI = {
    "Parco giochi": "MAX",
    "Attrezzature sportive fisse": "MAX",
    "Giardino condominiale piantumato oltre il 50% dell'area scoperta": "MAX",
    "Giardino condominiale piantumato tra il 20% e il 50% dell'area scoperta": "MEDIA",
    "Assenza di spazi attrezzati o giardino sotto il 10% dell'area scoperta": "MIN",
}
SERVIZI_TECNICI = [
    "Impianto di riscaldamento autonomo",
    "Impianto di condizionamento / raffrescamento",
    "Ascensore",
]
AUTORIMESSA = {
    "Due o più posti auto": "MAX",
    "Un solo posto auto o posto auto esclusivo interno": "MEDIA",
    "Assenza di autorimessa e/o posto auto esclusivo interno": "MIN",
}
