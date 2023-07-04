import tkinter as tk
from tkinter import messagebox


def prescribe_medication():
    diagnosis = diagnosis_entry.get()
    medication = medication_entry.get()

    # Tutaj można umieścić kod obsługujący przepisywanie leków na podstawie diagnozy
    # np. zapisanie przepisanego leku do bazy danych lub wysłanie powiadomienia do pacjenta
    messagebox.showinfo("Przepisanie leków", "Leki zostały przepisane.")


def show_prescribed_medication():
    # Tutaj można umieścić kod obsługujący wyświetlanie przepisanych leków dla pacjenta
    # np. pobranie danych z bazy danych i wyświetlenie ich w interfejsie graficznym
    prescribed_meds = "Lek 1\nLek 2\nLek 3"  # Przykładowe dane
    messagebox.showinfo("Przepisane leki", prescribed_meds)


# Tworzenie okna głównego
root = tk.Tk()
root.title('Przepisywanie Leków')

# Tworzenie pól tekstowych do wprowadzania informacji
diagnosis_label = tk.Label(root, text='Diagnoza:')
diagnosis_label.pack()
diagnosis_entry = tk.Entry(root, width=30)
diagnosis_entry.pack()

medication_label = tk.Label(root, text='Przepisane leki:')
medication_label.pack()
medication_entry = tk.Entry(root, width=30)
medication_entry.pack()

# Przycisk do przepisywania leków
prescribe_button = tk.Button(root, text='Przepisz leki', command=prescribe_medication)
prescribe_button.pack()

# Przycisk do wyświetlania przepisanych leków
show_button = tk.Button(root, text='Przeglądaj przepisane leki', command=show_prescribed_medication)
show_button.pack()

# Uruchomienie pętli głównego okna
root.mainloop()
