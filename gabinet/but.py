import tkinter as tk

def handle_patient_login():
    print("Logowanie jako pacjent")

def handle_doctor_login():
    print("Logowanie jako lekarz")

# Tworzenie głównego okna aplikacji
window = tk.Tk()
window.title("Aplikacja Gabinetu Lekarskiego")

# Tworzenie przycisku "Wejście jako pacjent"
patient_button = tk.Button(window, text="Wejście jako pacjent", command=handle_patient_login)
patient_button.pack(pady=10)

# Tworzenie przycisku "Wejście jako lekarz"
doctor_button = tk.Button(window, text="Wejście jako lekarz", command=handle_doctor_login)
doctor_button.pack(pady=10)

# Uruchomienie pętli głównego okna aplikacji
window.mainloop()
