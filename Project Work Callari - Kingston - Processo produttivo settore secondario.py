import random  # Libreria per la generazione di numeri casuali

class GeneratoreDati:
    def __init__(self, prodotti, max_quantita=1000, max_tempo_unitario=15, max_capacita_giornaliera=2000):
        self.prodotti = prodotti
        self.max_quantita = max_quantita
        self.max_tempo_unitario = max_tempo_unitario
        self.max_capacita_giornaliera = max_capacita_giornaliera

    def genera_quantita_prodotti(self):
        """
        Genera una quantità casuale per ciascun prodotto.
        Restituisce un dizionario {prodotto: quantità}.
        """
        return {prodotto: random.randint(1, self.max_quantita) for prodotto in self.prodotti}

    def genera_parametri_produzione(self):
        """
        Genera parametri casuali per la produzione:
        - Tempo di produzione per unità (in minuti)
        - Capacità massima giornaliera per prodotto
        Restituisce una tupla (tempi_unitari, capacita_giornaliera).
        """
        tempi_unitari = {prodotto: random.uniform(1, self.max_tempo_unitario) for prodotto in self.prodotti}
        capacita_giornaliera = {prodotto: random.randint(500, self.max_capacita_giornaliera) for prodotto in self.prodotti}
        return tempi_unitari, capacita_giornaliera

class CalcolatoreProduzione:
    @staticmethod
    def calcola_tempo_totale_produzione(quantita, tempi_unitari):
        """
        Calcola il tempo totale di produzione per il lotto.
        Somma il prodotto tra la quantità e il tempo unitario per ciascun prodotto.
        """
        return sum(quantita[prodotto] * tempi_unitari[prodotto] for prodotto in quantita)

class SimulatoreProduzione:
    def __init__(self, prodotti=None, max_quantita=1000, max_tempo_unitario=15, max_capacita_giornaliera=2000):
        if prodotti is None:
            prodotti = ["RAM DDR5", "SSD NVMe", "Chiavette USB"]
        self.prodotti = prodotti
        self.generatore = GeneratoreDati(prodotti, max_quantita, max_tempo_unitario, max_capacita_giornaliera)
        self.calcolatore = CalcolatoreProduzione()

    def simula_produzione(self):
        """
        Esegue l'intero processo produttivo:
        - Genera dati di produzione
        - Calcola e visualizza il tempo totale di produzione
        - Converte il tempo totale in ore e in giorni lavorativi (supponendo turni di 8 ore)
        """
        quantita = self.generatore.genera_quantita_prodotti()
        tempi_unitari, capacita_giornaliera = self.generatore.genera_parametri_produzione()

        print("=== Parametri della Produzione ===")
        print(f"Quantità da produrre per prodotto: {quantita}")
        print(f"Tempo di produzione per unità (minuti): {tempi_unitari}")
        print(f"Capacità massima giornaliera per prodotto: {capacita_giornaliera}")

        tempo_totale = self.calcolatore.calcola_tempo_totale_produzione(quantita, tempi_unitari)
        print(f"\nTempo totale di produzione del lotto (minuti): {tempo_totale:.2f}")

        ore = tempo_totale / 60
        giorni = tempo_totale / (60 * 8)
        print(f"Tempo totale in ore: {ore:.2f}")
        print(f"Tempo totale in giorni lavorativi: {giorni:.2f}")

if __name__ == "__main__":
    simulatore = SimulatoreProduzione()
    simulatore.simula_produzione()
