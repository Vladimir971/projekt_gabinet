from tkinter import Tk, Button, Toplevel, Label, Entry

class GabinetLekarski:
    def __init__(self):
        self.window = Tk()
        self.window.title("Aplikacja gabinetu lekarskiego")

        self.button_pacjent = Button(self.window, text="Wejście jako pacjent", command=self.wejscie_jako_pacjent)
        self.button_pacjent.pack(pady=10)

        self.button_lekarz = Button(self.window, text="Wejście jako lekarz", command=self.wejscie_jako_lekarz)
        self.button_lekarz.pack(pady=10)

    def wejscie_jako_pacjent(self):
        print("Wejście jako pacjent")
        self.okno_rejestracji("Pacjent")

    def wejscie_jako_lekarz(self):
        print("Wejście jako lekarz")
        self.okno_rejestracji("Lekarz")

    def okno_rejestracji(self, rola):
        rejestracja_window = Toplevel(self.window)
        rejestracja_window.title("Okno rejestracji")

        label_imie = Label(rejestracja_window, text="Imię:")
        label_imie.pack()

        entry_imie = Entry(rejestracja_window)
        entry_imie.pack()

        label_haslo = Label(rejestracja_window, text="Hasło:")
        label_haslo.pack()

        entry_haslo = Entry(rejestracja_window, show="*")
        entry_haslo.pack()

        label_email = Label(rejestracja_window, text="Adres e-mail:")
        label_email.pack()

        entry_email = Entry(rejestracja_window)
        entry_email.pack()

        button_zarejestruj = Button(rejestracja_window, text="Zarejestruj", command=lambda: self.zarejestruj(rola, entry_imie.get(), entry_haslo.get(), entry_email.get()))
        button_zarejestruj.pack(pady=10)

    def zarejestruj(self, rola, imie, haslo, email):
        print(f"Zarejestrowano nowego {rola}:")
        print(f"Imię: {imie}")
        print(f"Hasło: {haslo}")
        print(f"Adres e-mail: {email}")

    def run(self):
        self.window.mainloop()

# Inicjalizacja aplikacji
app = GabinetLekarski()
app.run()
