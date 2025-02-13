import random  # Inserimento libreria per la generazione di numeri casuali

    # Configurazione dei parametri principali
def genera_quantita_prodotti(prodotti, max_quantita=1000):
    """
    Genera una quantità casuale per ciascun prodotto.
    """
    return {prodotto: random.randint(1, max_quantita) for prodotto in prodotti}

def genera_parametri_produzione(prodotti, max_tempo_unitario=15, max_capacita_giornaliera=2000):
    """
    Genera parametri casuali per la produzione:
    - Tempo di produzione per unità (in minuti)
    - Capacità massima giornaliera per prodotto
    """
    tempi_unitari = {prodotto: random.uniform(1, max_tempo_unitario) for prodotto in prodotti}
    capacita_giornaliera = {prodotto: random.randint(500, max_capacita_giornaliera) for prodotto in prodotti}
    return tempi_unitari, capacita_giornaliera

def calcola_tempo_totale_produzione(quantita, tempi_unitari):
    """
    Calcola il tempo totale di produzione per il lotto.
    """
    return sum(quantita[prodotto] * tempi_unitari[prodotto] for prodotto in quantita)

    # Simulazione
def simula_produzione():
    prodotti = ["RAM DDR5", "SSD NVMe", "Chiavette USB"]  # Lista dei prodotti
    max_quantita = 1000
    max_tempo_unitario = 15  # Minuti
    max_capacita_giornaliera = 2000  # Unità

    # Generazione dei dati
    quantita = genera_quantita_prodotti(prodotti, max_quantita)
    tempi_unitari, capacita_giornaliera = genera_parametri_produzione(prodotti, max_tempo_unitario, max_capacita_giornaliera)

    # Output dettagliato
    print("=== Parametri della Produzione ===")
    print(f"Quantità da produrre per prodotto: {quantita}")
    print(f"Tempo di produzione per unità (minuti): {tempi_unitari}")
    print(f"Capacità massima giornaliera per prodotto: {capacita_giornaliera}")

    # Calcolo del tempo totale
    tempo_totale = calcola_tempo_totale_produzione(quantita, tempi_unitari)
    print(f"\nTempo totale di produzione del lotto (minuti): {tempo_totale:.2f}")

    # Conversione in ore e giorni
    ore = tempo_totale / 60
    giorni = tempo_totale / (60 * 8)  # Supponendo turni di 8 ore
    print(f"Tempo totale in ore: {ore:.2f}")
    print(f"Tempo totale in giorni lavorativi: {giorni:.2f}")

    # Esecuzione della simulazione
if __name__ == "__main__":
    simula_produzione()