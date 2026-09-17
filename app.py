import streamlit as st

# ==========================================
# CONFIGURAZIONE PAGINA
# ==========================================
st.set_page_config(
    page_title="Calcolatore Canone Concordato Completo",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Simulatore Canone Concordato - Modello Analitico")
st.caption("Calcolo parametrico con superfici ponderate, dotazioni, classe APE e tipologie contrattuali (D.M. 16/01/2017)")

# ==========================================
# DATABASE CATEGORIE CATASTALI E PARAMETRI
# ==========================================
CATEGORIE_CATASTALI = {
    "A/2": {"nome": "Abitazioni di tipo civile", "ammesso": True, "desc": "Fabbricati di tipo economico o medio dotati di buone finiture e impianti standard."},
    "A/3": {"nome": "Abitazioni di tipo economico", "ammesso": True, "desc": "Fabbricati con finiture e impianti di modesta entità, risponde a requisiti di semplicità."},
    "A/4": {"nome": "Abitazioni di tipo popolare", "ammesso": True, "desc": "Fabbricati costruiti con strutture e finiture di modesto livello e dotazioni essenziali."},
    "A/5": {"nome": "Abitazioni di tipo ultramassimo", "ammesso": True, "desc": "Alloggi di ridottissimo livello abitativo e con servizi minimi (categoria residuale)."},
    "A/6": {"nome": "Abitazioni di tipo rurale", "ammesso": True, "desc": "Fabbricati a servizio delle attività agricole, con caratteristiche costruttive semplici."},
    "A/7": {"nome": "Abitazioni in villini", "ammesso": True, "desc": "Fabbricato anche suddiviso in più unità con giardino o spazi verdi pertinenziali."},
    "A/11": {"nome": "Abitazioni ed alloggi tipici dei luoghi", "ammesso": True, "desc": "Rifugi di montagna, trulli, dammusi, case padronali storiche locali o baite."},
    "A/1": {"nome": "Abitazioni di tipo signorile", "ammesso": False, "desc": "ESCLUSO PER LEGGE: Unità in fabbricati ad alto pregio architettonico/finiture superiori."},
    "A/8": {"nome": "Abitazioni in ville", "ammesso": False, "desc": "ESCLUSO PER LEGGE: Immobili caratterizzati da ampi parchi o giardini di uso esclusivo."},
    "A/9": {"nome": "Castelli e palazzi storici", "ammesso": False, "desc": "ESCLUSO PER LEGGE: Castelli o palazzi di eminente pregio artistico/storico."}
}

# Percentuali di ponderazione delle pertinenze rispetto alla superficie calpestabile
COEFF_PERTINENZE = {
    "cantina_soffitta": 0.25,      # 25% della superficie reale
    "balcone_terrazzo": 0.30,      # 30% della superficie reale
    "giardino_privato": 0.10,      # 10% della superficie reale
    "posto_auto_scoperto": 0.20,   # 20% della superficie reale
    "garage_posto_coperto": 0.50   # 50% della superficie reale
}

# ==========================================
# INTERFACCIA UTENTE
# ==========================================

st.subheader("1. Categoria Catastale e Inquadramento")

opzioni_cat = [f"{cod} - {dati['nome']}" for cod, dati in CATEGORIE_CATASTALI.items()]
scelta_cat_str = st.selectbox("Seleziona Categoria Catastale", options=opzioni_cat, index=1)
codice_cat = scelta_cat_str.split(" - ")[0]
info_cat = CATEGORIE_CATASTALI[codice_cat]

# Alert sullo stato dell'ammissibilità
if info_cat["ammesso"]:
    st.success(f"✅ **{codice_cat} ({info_cat['nome']})**: Categoria ammissibile. {info_cat['desc']}")
else:
    st.error(f"❌ **{codice_cat} ({info_cat['nome']})**: {info_cat['desc']}")
    st.stop()

st.divider()

col_sx, col_dx = st.columns(2)

with col_sx:
    st.subheader("2. Superfici dell'Immobile e Pertinenze")
    
    mq_abitazione = st.number_input("Abitazione - Superficie utile calpestabile (m²)", min_value=10.0, max_value=300.0, value=45.0, step=1.0)
    mq_cantina = st.number_input("Cantina / Soffitta (m²)", min_value=0.0, max_value=50.0, value=0.0, step=1.0)
    mq_balcone = st.number_input("Balconi / Terrazzi (m²)", min_value=0.0, max_value=100.0, value=0.0, step=1.0)
    mq_giardino = st.number_input("Giardino ad uso esclusivo (m²)", min_value=0.0, max_value=500.0, value=0.0, step=5.0)
    mq_garage = st.number_input("Garage o Posto auto coperto (m²)", min_value=0.0, max_value=60.0, value=0.0, step=1.0)
    mq_posto_scoperto = st.number_input("Posto auto scoperto riservato (m²)", min_value=0.0, max_value=50.0, value=0.0, step=1.0)

with col_dx:
    st.subheader("3. Tipologia Contrattuale e Condizioni")
    
    tipo_contratto = st.selectbox(
        "Tipologia di Contratto",
        options=[
            "Abitativo Agevolato Ordinario (3+2 o superiori)",
            "Transitorio Ordinario (1 - 18 mesi)",
            "Studenti Universitari (6 - 36 mesi)"
        ]
    )
    
    durata_estesa = False
    if "Ordinario" in tipo_contratto:
        durata_estesa = st.checkbox("Patto di durata maggiorata (es. 4+2, 5+2, 6+2)", value=False)
        
    arredato = st.checkbox("Immobile completamente arredato ed efficiente", value=True)
    
    ape = st.selectbox(
        "Attestato Prestazione Energetica (APE)",
        options=["A4 / A3 / A2 / A1", "B / C", "D / E", "F / G"],
        index=3
    )

st.divider()

st.subheader("4. Scheda Dotazioni ed Elementi di Pregio (Sistema a Punteggio)")
st.caption("Seleziona tutti gli elementi presenti nell'immobile per calcolare la sottofascia dell'Accordo Territoriale:")

col_d1, col_d2, col_d3 = st.columns(3)

with col_d1:
    el_ascensore = st.checkbox("Ascensore (o piano terra/primo)")
    el_doppi_servizi = st.checkbox("Doppi servizi igienici")
    el_riscaldamento = st.checkbox("Riscaldamento autonomo o contabilizzato")
    el_clima = st.checkbox("Impianto di climatizzazione / Pompa di calore")

with col_d2:
    el_vetri = st.checkbox("Doppi vetri / Serramenti ad alta tenuta")
    el_porta_blindata = st.checkbox("Porta blindata")
    el_videocitofono = st.checkbox("Videocitofono")
    el_cappotto = st.checkbox("Isolamento termico a cappotto / Facciata nuova")

with col_d3:
    el_verde = st.checkbox("Area verde condominiale o parco")
    el_fibra = st.checkbox("Impianto satellitare / Cablaggio Fibra FTTH")
    el_accessibile = st.checkbox("Assenza barriere architettoniche")
    el_ripostiglio = st.checkbox("Ripostiglio interno dedicato")

# ==========================================
# LOGICA DI CALCOLO
# ==========================================

# 1. Calcolo Superficie Convenzionale / Ponderata
superficie_pertinenze_ponderata = (
    (mq_cantina * COEFF_PERTINENZE["cantina_soffitta"]) +
    (mq_balcone * COEFF_PERTINENZE["balcone_terrazzo"]) +
    (mq_giardino * COEFF_PERTINENZE["giardino_privato"]) +
    (mq_garage * COEFF_PERTINENZE["garage_posto_coperto"]) +
    (mq_posto_scoperto * COEFF_PERTINENZE["posto_auto_scoperto"])
)

mq_totali_ponderati = mq_abitazione + superficie_pertinenze_ponderata

# Maggiorazione per piccoli tagli (< 46 mq)
if mq_abitazione < 46.0:
    mq_convenzionali_finali = mq_totali_ponderati * 1.20
    maggiorazione_taglio = True
else:
    mq_convenzionali_finali = mq_totali_ponderati
    maggiorazione_taglio = False

# 2. Calcolo Punteggio Dotazioni e Determinazione Sottofascia
punti_dotazioni = sum([
    el_ascensore, el_doppi_servizi, el_riscaldamento, el_clima,
    el_vetri, el_porta_blindata, el_videocitofono, el_cappotto,
    el_verde, el_fibra, el_accessibile, el_ripostiglio
])

if punti_dotazioni <= 3:
    sottofascia = "Fascia Minima"
    valore_base_min, valore_base_max = 4.00, 5.00
elif 4 <= punti_dotazioni <= 7:
    sottofascia = "Fascia Media"
    valore_base_min, valore_base_max = 5.00, 6.30
else:
    sottofascia = "Fascia Massima"
    valore_base_min, valore_base_max = 6.30, 7.50

# 3. Modificatori Percentuali (APE, Arredo, Contratto)
var_percentuale = 0.0

# Correzione APE
if ape == "A4 / A3 / A2 / A1":
    var_percentuale += 10.0
elif ape == "B / C":
    var_percentuale += 5.0
elif ape == "F / G":
    var_percentuale -= 5.0

# Arredamento
if arredato:
    var_percentuale += 15.0

# Durata contrattuale estesa
if durata_estesa:
    var_percentuale += 5.0

# Tipologia transitoria/studenti (maggiorazione prevista da diversi accordi per contratti brevi)
if "Transitorio" in tipo_contratto or "Studenti" in tipo_contratto:
    var_percentuale += 10.0

# 4. Calcolo Finale Canone
canone_min_base = mq_convenzionali_finali * valore_base_min
canone_max_base = mq_convenzionali_finali * valore_base_max

canone_min_finale = canone_min_base * (1 + (var_percentuale / 100))
canone_max_finale = canone_max_base * (1 + (var_percentuale / 100))
canone_medio_finale = (canone_min_finale + canone_max_finale) / 2

# ==========================================
# OUTPUT RISULTATI
# ==========================================

st.divider()
st.subheader("5. Prospetto di Calcolo e Risultato")

m1, m2, m3 = st.columns(3)

m1.metric("Superficie Convenzionale", f"{mq_convenzionali_finali:.2f} m²", delta="+20% piccolo taglio" if maggiorazione_taglio else "Standard")
m2.metric("Sottofascia Determinata", f"{sottofascia}", delta=f"{punti_dotazioni}/12 Elementi di pregio")
m3.metric("Variazione Totale Applicata", f"{var_percentuale:+.1f}%", delta="APE / Arredo / Contratto")

st.markdown(f"### **Canone Mensile Calcolato: € {canone_min_finale:.2f} – € {canone_max_finale:.2f}**")
st.caption(f"Valore di riferimento medio: **€ {canone_medio_finale:.2f} / mese**")

with st.expander("📊 Dettaglio analitico delle ponderazioni e maggiorazioni"):
    st.write(f"- **Superficie netta abitazione:** {mq_abitazione:.2f} m²")
    st.write(f"- **Superficie ponderata pertinenze:** {superficie_pertinenze_ponderata:.2f} m²")
    st.write(f"- **Superficie convenzionale complessiva:** {mq_convenzionali_finali:.2f} m²")
    st.write(f"- **Sottofascia individuata:** {sottofascia} (€ {valore_base_min:.2f} - € {valore_base_max:.2f} / m²/mese)")
    st.write(f"- **Punteggio elementi di pregio:** {punti_dotazioni} punti su 12")
    st.write(f"- **Dettaglio modificatori applicati:**")
    st.write(f"  - Arredamento completo: `+15%`" if arredato else "  - Arredamento: `Non presente`")
    st.write(f"  - Variazione Classe APE ({ape}): `{'+10%' if 'A4' in ape else ('+5%' if 'B' in ape else ('-5%' if 'F' in ape else '0%'))}`")
    if durata_estesa:
        st.write("  - Durata contrattuale estesa: `+5%`")
    if "Transitorio" in tipo_contratto or "Studenti" in tipo_contratto:
        st.write(f"  - Tipologia speciale ({tipo_contratto.split(' ')[0]}): `+10%`")