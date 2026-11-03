"""Controlli di coerenza sui dati di tutti gli accordi e prova a tappeto del calcolo."""
import random

import pytest

from accordi import ACCORDI
from calcolo import LIVELLI, Input, calcola

NOMI = list(ACCORDI)
CAMPI_OBBLIGATORI = (
    "NOME", "COMUNI", "FONTE", "VERIFICATO", "DATA_ISTAT", "NOTE", "FASCE_PER_ZONA", "CATEGORIE_CATASTALI",
    "TIPOLOGIA_CATASTALE", "TIPOLOGIA_EDILIZIA", "VETUSTA", "SPAZI_COMUNI", "AUTORIMESSA", "SERVIZI_TECNICI",
    "ACCESSORI_DOTAZIONE", "ACCESSORI", "SOGLIE_ACCESSORI", "ARREDO", "DURATA", "STORICO_VINCOLATO",
    "VIABILITA_TRAFFICO", "REGOLA_DUE_MEDIE_TRE_MINIME",
)


@pytest.mark.parametrize("nome", NOMI)
def test_campi_presenti(nome):
    acc = ACCORDI[nome]
    assert [c for c in CAMPI_OBBLIGATORI if not hasattr(acc, c)] == []
    assert acc.NOME == nome and acc.FASCE_PER_ZONA


@pytest.mark.parametrize("nome", NOMI)
def test_fasce_coerenti(nome):
    for zona, fasce in ACCORDI[nome].FASCE_PER_ZONA.items():
        assert set(fasce) == set(LIVELLI), zona
        for livello, (lo, hi) in fasce.items():
            assert 0 < lo < hi, f"{zona} {livello}"
        mn, md, mx = (fasce[k] for k in ("MIN", "MEDIA", "MAX"))
        assert mn[0] <= md[0] <= mx[0], f"{zona}: minimi non crescenti"
        assert mn[1] <= md[1] <= mx[1], f"{zona}: massimi non crescenti"


@pytest.mark.parametrize("nome", NOMI)
def test_tabelle_criteri(nome):
    acc = ACCORDI[nome]
    for tabella in (acc.TIPOLOGIA_EDILIZIA, acc.VETUSTA, acc.SPAZI_COMUNI, acc.AUTORIMESSA, acc.TIPOLOGIA_CATASTALE):
        assert set(tabella.values()) <= set(LIVELLI)
    chiavi = [c for c, _, _ in acc.ACCESSORI_DOTAZIONE]
    assert len(chiavi) == len(set(chiavi))
    assert len(acc.ACCESSORI) == len(set(acc.ACCESSORI))
    assert acc.DURATA and 0.0 in acc.DURATA.values() and 0.0 in acc.ARREDO.values()
    assert acc.VIABILITA_TRAFFICO < 0 < acc.STORICO_VINCOLATO
    assert all(c in acc.CATEGORIE_CATASTALI for c in acc.TIPOLOGIA_CATASTALE)


@pytest.mark.parametrize("nome", NOMI)
def test_prova_a_tappeto(nome):
    acc, rnd = ACCORDI[nome], random.Random(nome)
    chiavi = [c for c, _, _ in acc.ACCESSORI_DOTAZIONE]
    for _ in range(200):
        r = calcola(Input(
            accordo=acc, zona=rnd.choice(list(acc.FASCE_PER_ZONA)), categoria=rnd.choice(list(acc.CATEGORIE_CATASTALI)),
            mq_abitazione=rnd.uniform(10, 300), cantina=rnd.uniform(0, 50), balconi=rnd.uniform(0, 100),
            area_scoperta=rnd.uniform(0, 500), autorimessa=rnd.uniform(0, 60), verde_condominio=rnd.uniform(0, 500),
            tipologia_edilizia=rnd.choice(list(acc.TIPOLOGIA_EDILIZIA)), vetusta=rnd.choice(list(acc.VETUSTA)),
            accessori_dotazione=tuple(c for c in chiavi if rnd.random() < 0.5),
            spazi_comuni=rnd.choice(list(acc.SPAZI_COMUNI)), servizi_tecnici=rnd.randint(0, 3),
            autorimessa_livello=rnd.choice(list(acc.AUTORIMESSA)), arredo_pct=rnd.choice(list(acc.ARREDO.values())),
            viabilita_traffico=rnd.random() < 0.5, durata_pct=rnd.choice(list(acc.DURATA.values())),
            storico_vincolato=rnd.random() < 0.5, n_accessori_pregio=rnd.randint(0, len(acc.ACCESSORI)),
            istat_pct=rnd.uniform(0, 20),
        ))
        assert 0 < r.canone_min <= r.canone_max
