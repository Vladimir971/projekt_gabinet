import tkinter as tk


def update_profile():
    historia_chorob_text.delete('1.0', tk.END)
    historia_chorob_text.insert(tk.END, 'Choroba X, 2018\nChoroba Y, 2019')

    aktualne_leki_text.delete('1.0', tk.END)
    aktualne_leki_text.insert(tk.END, 'Lek A, dawka: 2x dziennie\nLek B, dawka: 1x dziennie')

    wyniki_badan_text.delete('1.0', tk.END)
    wyniki_badan_text.insert(tk.END, 'Badanie X, wynik: pozytywny\nBadanie Y, wynik: negatywny')

    alergie_text.delete('1.0', tk.END)
    alergie_text.insert(tk.END, 'Alergia na pyłki kwiatów\nAlergia na orzechy')


# Tworzenie okna głównego
root = tk.Tk()
root.title('Profil Pacjenta')

# Tworzenie etykiet i pól tekstowych dla danych profilu
historia_chorob_label = tk.Label(root, text='Historia Chorób:')
historia_chorob_label.pack()
historia_chorob_text = tk.Text(root, height=5, width=30)
historia_chorob_text.pack()

aktualne_leki_label = tk.Label(root, text='Aktualne Leki:')
aktualne_leki_label.pack()
aktualne_leki_text = tk.Text(root, height=5, width=30)
aktualne_leki_text.pack()

wyniki_badan_label = tk.Label(root, text='Wyniki Badań:')
wyniki_badan_label.pack()
wyniki_badan_text = tk.Text(root, height=5, width=30)
wyniki_badan_text.pack()

alergie_label = tk.Label(root, text='Alergie:')
alergie_label.pack()
alergie_text = tk.Text(root, height=5, width=30)
alergie_text.pack()

# Przycisk do aktualizacji danych profilu
update_button = tk.Button(root, text='Aktualizuj', command=update_profile)
update_button.pack()

# Wywołanie funkcji update_profile() po starcie aplikacji, aby wypełnić dane przykładowymi informacjami
update_profile()

# Uruchomienie pętli głównego okna
root.mainloop()
