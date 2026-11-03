"""Logica di calcolo del canone concordato secondo l'Accordo Territoriale
(senza interfaccia, testabile). I valori stanno in parametri.py."""
from dataclasses import dataclass, field

import parametri as P

LIVELLI = ("MIN", "MEDIA", "MAX")


@dataclass(frozen=True)
class Input:
    categoria: str
    mq_abitazione: float
    cantina: float = 0.0
    balconi: float = 0.0
    area_scoperta: float = 0.0
    posto_auto_comune: float = 0.0
    autorimessa: float = 0.0
    verde_condominio: float = 0.0
    # livelli già scelti per i criteri dell'Allegato 3 (None = criterio non applicabile)
    tipologia_edilizia: str = ""
    vetusta: str = ""
    accessori_dotazione: tuple[str, ...] = ()   # chiavi di P.ACCESSORI_DOTAZIONE
    spazi_comuni: str = ""
    servizi_tecnici: int = 0
    autorimessa_livello: str = ""
    # maggiorazioni
    arredo_pct: float = 0.0
    viabilita_traffico: bool = False
    durata_pct: float = 0.0
    storico_vincolato: bool = False
    n_accessori_pregio: int = 0
    istat_pct: float = 0.0


@dataclass(frozen=True)
class Risultato:
    mq_abitazione_convenzionale: float
    pertinenze: dict[str, float]
    superficie_convenzionale: float
    livelli: dict[str, str | None]
    fascia: str
    valore_min: float
    valore_max: float
    maggiorazioni: list[tuple[str, float]] = field(default_factory=list)
    variazione_pct: float = 0.0
    canone_min: float = 0.0
    canone_max: float = 0.0

    @property
    def canone_medio(self) -> float:
        return (self.canone_min + self.canone_max) / 2


def mq_abitazione_convenzionale(mq: float) -> float:
    """Art. 4: coefficiente 1,20 (<46 mq, max 50,6), 1,10 (46-70, max 70), 1,00 oltre."""
    if mq < P.SOGLIA_PICCOLO_MQ:
        return min(mq * P.COEFF_PICCOLO, P.TETTO_PICCOLO)
    if mq <= P.SOGLIA_MEDIO_MQ:
        return min(mq * P.COEFF_MEDIO, P.TETTO_MEDIO)
    return mq


def pertinenze_ponderate(i: Input) -> dict[str, float]:
    return {
        "Cantina": i.cantina * P.COEFF_CANTINA,
        "Balconi / terrazzi / sottotetti": i.balconi * P.COEFF_BALCONI,
        "Area scoperta esclusiva": min(i.area_scoperta, i.mq_abitazione) * P.COEFF_AREA_SCOPERTA,
        "Posto auto in comune": i.posto_auto_comune * P.COEFF_POSTO_AUTO_COMUNE,
        "Autorimessa singola": i.autorimessa * P.COEFF_AUTORIMESSA,
        "Verde condominiale (quota millesimale)": min(i.verde_condominio, i.mq_abitazione) * P.COEFF_VERDE_CONDOMINIO,
    }


def livello_accessori(n: int) -> str:
    return "MAX" if n >= 3 else "MEDIA" if n == 2 else "MIN"


def livello_servizi(n: int) -> str:
    return "MAX" if n >= 2 else "MEDIA" if n == 1 else "MIN"


def fascia_globale(livelli: list[str]) -> str:
    """Classificazione globale (Allegato 3): prevale il livello più frequente."""
    n = {k: livelli.count(k) for k in LIVELLI}
    if (n["MIN"], n["MEDIA"], n["MAX"]) == (3, 2, 2):   # caso esplicito dell'accordo
        return "MEDIA"
    top = max(n.values())
    in_testa = {k for k in LIVELLI if n[k] == top}
    if len(in_testa) == 1:
        return in_testa.pop()
    if in_testa == {"MAX", "MEDIA"}:
        return "MAX"
    return "MEDIA"                                      # MEDIA/MIN, MAX/MIN o parità a tre


def pct_accessori_pregio(n: int) -> float:
    for soglia, pct in P.SOGLIE_ACCESSORI:
        if n >= soglia:
            return pct
    return 0.0


def livelli_criteri(i: Input) -> dict[str, str | None]:
    escluso_a7 = {chiave: escluso for chiave, _, escluso in P.ACCESSORI_DOTAZIONE}
    n_acc = sum(1 for k in i.accessori_dotazione
                if not (i.categoria == "A/7" and escluso_a7[k]))
    return {
        "1 Tipologia edilizia": P.TIPOLOGIA_EDILIZIA[i.tipologia_edilizia],
        "2 Tipologia catastale": P.TIPOLOGIA_CATASTALE.get(i.categoria),
        "3 Vetustà": P.VETUSTA[i.vetusta],
        "4 Accessori in dotazione": livello_accessori(n_acc),
        "5 Spazi comuni attrezzati": P.SPAZI_COMUNI[i.spazi_comuni],
        "6 Servizi tecnici": livello_servizi(i.servizi_tecnici),
        "7 Autorimessa": P.AUTORIMESSA[i.autorimessa_livello],
    }


def calcola(i: Input) -> Risultato:
    mq_abit = mq_abitazione_convenzionale(i.mq_abitazione)
    pert = pertinenze_ponderate(i)
    mq_tot = mq_abit + sum(pert.values())

    livelli = livelli_criteri(i)
    fascia = fascia_globale([v for v in livelli.values() if v])
    vmin, vmax = P.FASCE[fascia]
    k_istat = 1 + i.istat_pct / 100
    vmin, vmax = vmin * k_istat, vmax * k_istat

    magg: list[tuple[str, float]] = []
    if i.arredo_pct:
        magg.append(("Arredamento", i.arredo_pct))
    if i.durata_pct:
        magg.append(("Durata superiore a 3 anni", i.durata_pct))
    if i.storico_vincolato:
        magg.append(("Immobile storico vincolato", P.STORICO_VINCOLATO))
    pct_pregi = pct_accessori_pregio(i.n_accessori_pregio)
    if pct_pregi:
        magg.append((f"Elementi accessori Allegato 4 ({i.n_accessori_pregio})", pct_pregi))
    if i.viabilita_traffico:
        magg.append(("Viabilità ad elevato traffico", P.VIABILITA_TRAFFICO))
    var = sum(p for _, p in magg)
    f = 1 + var / 100
    return Risultato(mq_abit, pert, mq_tot, livelli, fascia, vmin, vmax, magg, var,
                     round(mq_tot * vmin * f, 2), round(mq_tot * vmax * f, 2))
