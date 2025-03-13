import tkinter as tk
import time
 
class Waehrungsrechner:
    def __init__(self, fenster):
        self.fenster = fenster
        self.fenster.title("Währungsrechner")
       
        self.deutsch = True
       
        self.label_info = tk.Label(fenster, text="Gib den Betrag ein:")
        self.label_info.pack()
       
        self.eingabe = tk.Entry(fenster)
        self.eingabe.pack()
       
        self.label_waehrung = tk.Label(fenster, text="Währung auswählen:")
        self.label_waehrung.pack()
       
        self.waehrungen = ["Yen", "Dollar", "Lek"]
        self.waehrung_liste = tk.Listbox(fenster, height=len(self.waehrungen))
        for w in self.waehrungen:
            self.waehrung_liste.insert(tk.END, w)
        self.waehrung_liste.pack()
       
        self.knopf = tk.Button(fenster, text="Konvertieren", command=lambda: self.umrechnen())
        self.knopf.pack()
       
        self.knopf2 = tk.Button(fenster, text="Sprache ändern", command=self.sprache)
        self.knopf2.pack()
        
        self.knopf3 = tk.Button(fenster, text="Färben", command=self.farben)
        self.knopf3.pack()
        
        self.ergebnis = tk.Label(fenster, text="")
        self.ergebnis.pack()
       
    def sprache(self):
        self.deutsch = not self.deutsch
        if self.deutsch:
            self.label_info.config(text="Gib den Betrag ein:")
            self.knopf.config(text="Konvertieren")
            self.knopf2.config(text="Sprache ändern")
            self.label_waehrung.config(text="Währung auswählen:")
        else:
            self.label_info.config(text="Enter the amount:")
            self.knopf.config(text="Convert")
            self.knopf2.config(text="Change language")
            self.label_waehrung.config(text="Select currency:")
        
    def farben(self):
        self.label_waehrung.config(bg="yellow",fg="black")
        self.label_info.config(bg="purple")
        self.knopf.config(bg="red")
        self.knopf2.config(bg="orange")
        self.knopf2.config(bg="blue")

    def umrechnen(self):
        try:
            betrag = float(self.eingabe.get())
            wahl = self.waehrung_liste.curselection()
            if not wahl:
                self.ergebnis.config(text="Bitte eine Währung wählen")
                return
            waehrung = self.waehrungen[wahl[0]]
            kurse = {"Yen": 156.62, "Dollar": 1.04, "Lek": 99.14}
            umgerechnet = betrag * kurse[waehrung]
            self.ergebnis.config(text=f"{umgerechnet} {waehrung}")
        except ValueError:
            self.ergebnis.config(text="Ungültige Eingabe")        
 
if __name__ == "__main__":
    fenster = tk.Tk()
    Waehrungsrechner(fenster)
    fenster.mainloop()