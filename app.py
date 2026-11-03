import streamlit as st

import parametri as P
from calcolo import Input, calcola

st.set_page_config(
    page_title="Calcolatore Canone Concordato - Ameglia",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Simulatore Canone Concordato - Ameglia (SP)")
st.caption("Accordo Territoriale Ameglia / Bolano / Castelnuovo Magra / Vezzano Ligure (L. 431/98, D.M. 16/01/2017) - area omogenea unica")

if not P.VERIFICATO:
    st.warning(f"⚠️ **Stima indicativa.** Parametri non ancora verificati. Fonte: {P.FONTE}.")
else:
    st.caption(f"Fonte: {P.FONTE}. Stima indicativa: l'attestazione di rispondenza spetta alle organizzazioni firmatarie.")

# ==========================================
# 1. CATEGORIA CATASTALE
# ==========================================
st.subheader("1. Categoria Catastale")
codici = list(P.CATEGORIE_CATASTALI)
codice_cat = st.selectbox(
    "Categoria catastale", options=codici, index=codici.index("A/3"),
    format_func=lambda c: f"{c} - {P.CATEGORIE_CATASTALI[c]['nome']}",
)
info_cat = P.CATEGORIE_CATASTALI[codice_cat]
if info_cat["ammesso"]:
    st.success(f"✅ **{codice_cat} ({info_cat['nome']})**: {info_cat['desc']}")
else:
    st.error(f"❌ **{codice_cat} ({info_cat['nome']})**: {info_cat['desc']}")
    st.stop()

st.divider()

# ==========================================
# 2-3. SUPERFICI E CONTRATTO
# ==========================================
col_sx, col_dx = st.columns(2)

with col_sx:
    st.subheader("2. Superfici (art. 4)")
    mq_abitazione = st.number_input("Abitazione - superficie calpestabile (m²)", min_value=10.0, max_value=300.0, value=45.0, step=1.0)
    mq_cantina = st.number_input("Cantina (m²) - 25%", min_value=0.0, max_value=50.0, value=0.0, step=1.0)
    mq_balconi = st.number_input("Balconi, terrazze, sottotetti h ≥ 1,70 m (m²) - 25%", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    mq_area_scoperta = st.number_input("Area scoperta esclusiva, es. giardino (m²) - 15%", min_value=0.0, max_value=500.0, value=0.0, step=5.0)
    mq_posto_comune = st.number_input("Posto auto in comune (m²) - 20%", min_value=0.0, max_value=50.0, value=0.0, step=1.0)
    mq_autorimessa = st.number_input("Autorimessa singola (m²) - 50%", min_value=0.0, max_value=60.0, value=0.0, step=1.0)
    mq_verde = st.number_input("Verde condominiale, quota millesimale (m²) - 10%", min_value=0.0, max_value=500.0, value=0.0, step=5.0)

with col_dx:
    st.subheader("3. Contratto e maggiorazioni (art. 5 e 7)")
    tipo_contratto = st.selectbox(
        "Tipologia di contratto",
        ["Agevolato (3+2 o superiori)", "Transitorio (fino a 18 mesi)", "Studenti universitari (6 - 36 mesi)"],
    )
    agevolato = tipo_contratto.startswith("Agevolato")
    durata_pct = 0.0
    if agevolato:
        durata_pct = P.DURATA[st.selectbox("Durata del contratto", list(P.DURATA))]
    arredo_pct = P.ARREDO[st.selectbox("Arredamento", list(P.ARREDO))]
    viabilita = st.checkbox("Adiacente a viabilità ad elevato traffico (−10%, attestato da un'organizzazione)")
    storico = st.checkbox("Immobile storico vincolato (+10%)")
    istat = st.number_input(
        "Adeguamento ISTAT da applicare ai valori €/m² (%)", min_value=0.0, max_value=50.0, value=0.0, step=0.1,
        help=("Art. 3 dell'accordo: i valori delle fasce si aggiornano al 100% della variazione ISTAT dal "
              "15/07/2021 per i contratti nuovi. Indice da completare. Non è l'aggiornamento annuale del "
              "canone in corso (art. 5, max 75%), a cui si rinuncia con la cedolare secca."),
    )

st.divider()

# ==========================================
# 4. CRITERI PER LA FASCIA (Allegato 3)
# ==========================================
st.subheader("4. Individuazione della fascia (Allegato 3)")
c1, c2, c3 = st.columns(3)

with c1:
    tip_edilizia = st.selectbox("1. Tipologia edilizia", list(P.TIPOLOGIA_EDILIZIA))
    vetusta = st.selectbox("3. Vetustà", list(P.VETUSTA), index=1)
    spazi = st.selectbox("5. Spazi comuni attrezzati", list(P.SPAZI_COMUNI), index=len(P.SPAZI_COMUNI) - 1)
with c2:
    st.markdown("**4. Accessori in dotazione**")
    accessori_dot = tuple(
        chiave for chiave, etichetta, escluso_a7 in P.ACCESSORI_DOTAZIONE
        if st.checkbox(etichetta + (" (non per A/7)" if escluso_a7 else ""), key=f"dot_{chiave}")
    )
with c3:
    st.markdown("**6. Servizi tecnici**")
    n_servizi = sum(st.checkbox(s, key=f"srv_{i}") for i, s in enumerate(P.SERVIZI_TECNICI))
    autorimessa_liv = st.selectbox("7. Dotazione di autorimessa", list(P.AUTORIMESSA), index=len(P.AUTORIMESSA) - 1)

st.divider()

# ==========================================
# 5. ELEMENTI ACCESSORI (Allegato 4)
# ==========================================
st.subheader("5. Elementi accessori di pregio (Allegato 4)")
st.caption("Da 2 elementi +5%, da 3 +10%, da 4 in su +15% sul canone base.")
pregi = st.multiselect("Elementi presenti", P.ACCESSORI)

# ==========================================
# CALCOLO E RISULTATI
# ==========================================
r = calcola(Input(
    categoria=codice_cat, mq_abitazione=mq_abitazione, cantina=mq_cantina, balconi=mq_balconi,
    area_scoperta=mq_area_scoperta, posto_auto_comune=mq_posto_comune, autorimessa=mq_autorimessa,
    verde_condominio=mq_verde, tipologia_edilizia=tip_edilizia, vetusta=vetusta,
    accessori_dotazione=accessori_dot, spazi_comuni=spazi, servizi_tecnici=n_servizi,
    autorimessa_livello=autorimessa_liv, arredo_pct=arredo_pct, viabilita_traffico=viabilita,
    durata_pct=durata_pct, storico_vincolato=storico, n_accessori_pregio=len(pregi), istat_pct=istat,
))

st.divider()
st.subheader("6. Risultato")

m1, m2, m3 = st.columns(3)
m1.metric("Superficie convenzionale", f"{r.superficie_convenzionale:.2f} m²")
m2.metric("Fascia", r.fascia, delta=f"€ {r.valore_min:.2f} - {r.valore_max:.2f} /m²/mese", delta_color="off")
m3.metric("Maggiorazioni totali", f"{r.variazione_pct:+.0f}%")

st.markdown(f"### **Canone mensile: € {r.canone_min:.2f} – € {r.canone_max:.2f}**")
st.caption(
    f"Valore medio: € {r.canone_medio:.2f} / mese. Le parti concordano un valore unitario "
    "dentro la fascia. Le maggiorazioni sono i massimi consentiti."
)
if not agevolato:
    st.info("Per transitori e studenti l'accordo rimanda alle stesse regole di calcolo, senza la maggiorazione per durata.")

with st.expander("📊 Dettaglio del calcolo"):
    st.write(f"- **Abitazione calpestabile:** {mq_abitazione:.2f} m² → convenzionale {r.mq_abitazione_convenzionale:.2f} m²")
    for nome, mq in r.pertinenze.items():
        if mq:
            st.write(f"- {nome}: {mq:.2f} m²")
    st.write(f"- **Superficie convenzionale totale:** {r.superficie_convenzionale:.2f} m²")
    st.write("- **Livelli dell'Allegato 3:**")
    for nome, liv in r.livelli.items():
        st.write(f"  - {nome}: `{liv or 'non applicabile'}`")
    st.write(f"- **Fascia globale:** {r.fascia}")
    if r.maggiorazioni:
        st.write("- **Maggiorazioni sul canone base:**")
        for descr, pct in r.maggiorazioni:
            st.write(f"  - {descr}: `{pct:+.0f}%`")
