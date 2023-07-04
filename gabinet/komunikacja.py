import tkinter as tk


def send_message():
    symptoms = symptoms_entry.get()
    duration = duration_entry.get()
    severity = severity_entry.get()

    # Tutaj można umieścić kod obsługujący wysłanie wiadomości do lekarza
    # wraz z informacjami o objawach, czasie choroby i poziomie ciężkości
    # np. wysłanie wiadomości poprzez API lub zapisanie jej w bazie danych
    # Można również wyświetlić potwierdzenie wysłania wiadomości w interfejsie graficznym


# Tworzenie okna głównego
root = tk.Tk()
root.title('Komunikacja z Lekarzem')

# Tworzenie pól tekstowych do wprowadzania informacji
symptoms_label = tk.Label(root, text='Objawy:')
symptoms_label.pack()
symptoms_entry = tk.Entry(root, width=30)
symptoms_entry.pack()

duration_label = tk.Label(root, text='Czas choroby:')
duration_label.pack()
duration_entry = tk.Entry(root, width=30)
duration_entry.pack()

severity_label = tk.Label(root, text='Poziom ciężkości choroby:')
severity_label.pack()
severity_entry = tk.Entry(root, width=30)
severity_entry.pack()

# Przycisk do wysłania wiadomości
send_button = tk.Button(root, text='Wyślij', command=send_message)
send_button.pack()

# Uruchomienie pętli głównego okna
root.mainloop()
