import pytest

from calcolo import (Input, calcola, fascia_globale, mq_abitazione_convenzionale,
                     pct_accessori_pregio)

TIP_MIN = "Unità su scala con più di 12 alloggi"
VET_MIN = "Oltre 50 anni"
SPAZI_MIN = "Assenza di spazi attrezzati o giardino sotto il 10% dell'area scoperta"
AUTO_MIN = "Assenza di autorimessa e/o posto auto esclusivo interno"


def base(**kw):
    args = dict(categoria="A/4", mq_abitazione=60.0, tipologia_edilizia=TIP_MIN, vetusta=VET_MIN,
                spazi_comuni=SPAZI_MIN, autorimessa_livello=AUTO_MIN)
    args.update(kw)
    return calcola(Input(**args))


@pytest.mark.parametrize("mq,atteso", [(45.0, 50.6), (40.0, 48.0), (46.0, 50.6),
                                       (70.0, 70.0), (60.0, 66.0), (80.0, 80.0)])
def test_coefficiente_taglio(mq, atteso):
    assert mq_abitazione_convenzionale(mq) == pytest.approx(atteso)


def test_tutti_minimi_fascia_min():
    r = base()
    assert r.fascia == "MIN"
    assert (r.canone_min, r.canone_max) == (round(66 * 4.0, 2), round(66 * 7.0, 2))


def test_pertinenze_e_tetti():
    r = base(mq_abitazione=80.0, cantina=10, balconi=10, autorimessa=10, area_scoperta=200)
    # 10*.25 + 10*.25 + 10*.5 + (area scoperta limitata a 80 m²)*.15
    assert r.superficie_convenzionale == pytest.approx(80 + 2.5 + 2.5 + 5 + 12)


@pytest.mark.parametrize("livelli,atteso", [
    (["MAX"] * 4 + ["MIN"] * 3, "MAX"),
    (["MIN"] * 4 + ["MEDIA"] * 3, "MIN"),
    (["MAX"] * 2 + ["MEDIA"] * 2 + ["MIN"] * 3, "MEDIA"),
    (["MAX"] * 3 + ["MIN"] * 3 + ["MEDIA"], "MEDIA"),
    (["MAX"] * 3 + ["MEDIA"] * 3 + ["MIN"], "MAX"),
    (["MEDIA"] * 3 + ["MIN"] * 3 + ["MAX"], "MEDIA"),
])
def test_fascia_globale(livelli, atteso):
    assert fascia_globale(livelli) == atteso


@pytest.mark.parametrize("n,pct", [(0, 0), (1, 0), (2, 5), (3, 10), (4, 15), (10, 15)])
def test_pct_pregi(n, pct):
    assert pct_accessori_pregio(n) == pct


def test_maggiorazioni_sul_canone_base():
    r = base(arredo_pct=30.0, durata_pct=8.0, storico_vincolato=True, n_accessori_pregio=2,
             viabilita_traffico=True)
    assert r.variazione_pct == 30 + 8 + 10 + 5 - 10
    assert r.canone_min == round(66 * 4.0 * 1.43, 2)


def test_categoria_non_in_tabella_salta_criterio():
    r = base(categoria="A/11")
    assert r.livelli["2 Tipologia catastale"] is None


def test_a1_e_max():
    assert base(categoria="A/1").livelli["2 Tipologia catastale"] == "MAX"


def test_a7_non_conta_accessori_esclusi():
    r = base(categoria="A/7", accessori_dotazione=("posto_auto_esterno", "area_esclusiva", "soffitta_cantina"))
    assert r.livelli["4 Accessori in dotazione"] == "MIN"


def test_istat():
    r = base(istat_pct=10.0)
    assert r.canone_min == round(66 * 4.0 * 1.1, 2)
