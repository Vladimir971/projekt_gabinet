import tkinter as tk
from tkinter import messagebox

# Dane przykładowe - harmonogram lekarzy
harmonogram = {
    'Dr. Kowalski': ['Poniedziałek, 9:00-12:00', 'Wtorek, 14:00-18:00'],
    'Dr. Lebowski': ['Środa, 10:00-13:00', 'Piątek, 9:00-12:00'],
    'Dr. Wiśnia': ['Czwartek, 8:00-11:00', 'Sobota, 10:00-13:00']
}

def umow_wizyte():
    lekarz = lekarze_listbox.get(tk.ACTIVE)
    termin = termin_entry.get()
    stan_zdrowia = stan_entry.get()

    # Tutaj można dodać logikę umawiania wizyty, np. zapisanie jej do bazy danych

    messagebox.showinfo('Sukces', 'Wizyta została umówiona!')

def pokaz_harmonogram():
    lekarz = lekarze_listbox.get(tk.ACTIVE)
    harmonogram_lekarza = harmonogram.get(lekarz, [])

    messagebox.showinfo('Harmonogram lekarza', '\n'.join(harmonogram_lekarza))

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title('Umawianie wizyt')

# Etykieta i lista rozwijana z lekarzami
lekarze_label = tk.Label(root, text='Wybierz lekarza:')
lekarze_label.pack()

lekarze_listbox = tk.Listbox(root, width=30)
lekarze_listbox.pack()

# Dodawanie lekarzy do listy rozwijanej
for lekarz in harmonogram.keys():
    lekarze_listbox.insert(tk.END, lekarz)

# Przyciski i etykiety
termin_label = tk.Label(root, text='Wybierz termin:')
termin_label.pack()

termin_entry = tk.Entry(root)
termin_entry.pack()

stan_label = tk.Label(root, text='Stan zdrowia:')
stan_label.pack()

stan_entry = tk.Entry(root)
stan_entry.pack()

umow_button = tk.Button(root, text='Umów wizytę', command=umow_wizyte)
umow_button.pack()

harmonogram_button = tk.Button(root, text='Pokaż harmonogram', command=pokaz_harmonogram)
harmonogram_button.pack()

# Uruchomienie pętli głównej aplikacji
root.mainloop()
