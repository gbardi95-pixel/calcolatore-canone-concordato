# Calcolatore Canone Concordato

App [Streamlit](https://streamlit.io) che stima il canone mensile di un contratto di locazione
a canone concordato (L. 431/98, D.M. 16/01/2017) applicando le regole di un Accordo Territoriale:
superficie convenzionale, fascia di oscillazione (MIN / MEDIA / MAX) e maggiorazioni.

> ⚠️ **È una stima indicativa**, non un'attestazione di rispondenza né una consulenza.
> L'attestazione ufficiale spetta alle organizzazioni firmatarie dell'accordo.

## Accordi disponibili

| Accordo | Stato |
|---|---|
| Ameglia, Bolano, Castelnuovo Magra, Vezzano Ligure (dal 15/07/2018) | verificato |
| Riccò del Golfo e altri 13 comuni, Bonassola e altri 7 comuni, Arcola, Luni, Sarzana, Santo Stefano di Magra, Lerici | disponibili, da ricontrollare (l'app mostra un avviso) |
| La Spezia (validità 2026-2028) | non ancora inserito: ha una struttura diversa |

Il programma è pensato per supportare più aree: ogni accordo è un file in `accordi/`.

## Avvio

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Test

```bash
pip install pytest
pytest
```

## Struttura

- `app.py` – interfaccia Streamlit
- `calcolo.py` – logica di calcolo, senza interfaccia
- `accordi/` – un modulo per ogni accordo territoriale (valori €/m², coefficienti, criteri, maggiorazioni)
- `test_calcolo.py` – test

## Aggiungere un nuovo accordo

1. Copiare `accordi/ameglia.py` in `accordi/nome_comune.py`.
2. Sostituire tutti i valori con quelli del nuovo accordo (fasce per zona in `FASCE_PER_ZONA`,
   coefficienti di superficie, tabelle dei criteri, maggiorazioni) e compilare `NOME`, `FONTE` e `VERIFICATO`.
3. Registrarlo in `accordi/__init__.py`.
4. Aggiungere i test e lanciare `pytest`.

Il motore di calcolo attuale gestisce accordi con la stessa struttura di quello di Ameglia
(fasce per zona, sette criteri dell'Allegato 3, maggiorazioni percentuali). Accordi con regole
diverse (altri criteri, altri tipi di maggiorazione) richiedono di estendere `calcolo.py`.

## Limiti noti

- L'adeguamento ISTAT dei valori delle fasce è un campo da compilare a mano: l'indice non è incluso.
- Per transitori e studenti valgono le stesse regole dell'agevolato, senza la maggiorazione per durata.
- Categorie catastali ammesse: quelle previste dalla tabella dell'accordo (per Ameglia da A/1 ad A/7).
- I valori sono stati trascritti da scansioni dei testi degli accordi: in caso di dubbio fa fede il testo ufficiale.

## Licenza

[MIT](LICENSE)
