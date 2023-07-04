import tkinter as tk
from tkinter import messagebox

# Dane przykładowe - profil pacjenta
profil_pacjenta = {
    'Imię': '',
    'Nazwisko': '',
    'Historia chorób': '',
    'Aktualne leki': '',
    'Wyniki badań': '',
    'Alergie': ''
}

def aktualizuj_profil():
    imie = imie_entry.get()
    nazwisko = nazwisko_entry.get()
    historia_chorob = historia_chorob_text.get('1.0', tk.END)
    aktualne_leki = aktualne_leki_text.get('1.0', tk.END)
    wyniki_badan = wyniki_badan_text.get('1.0', tk.END)
    alergie = alergie_text.get('1.0', tk.END)

    profil_pacjenta['Imię'] = imie
    profil_pacjenta['Nazwisko'] = nazwisko
    profil_pacjenta['Historia chorób'] = historia_chorob
    profil_pacjenta['Aktualne leki'] = aktualne_leki
    profil_pacjenta['Wyniki badań'] = wyniki_badan
    profil_pacjenta['Alergie'] = alergie

    messagebox.showinfo('Sukces', 'Profil pacjenta został zaktualizowany!')

# Tworzenie głównego okna aplikacji
root = tk.Tk()
root.title('Profil pacjenta')

# Etykiety i pola tekstowe
imie_label = tk.Label(root, text='Imię:')
imie_label.pack()

imie_entry = tk.Entry(root)
imie_entry.pack()

nazwisko_label = tk.Label(root, text='Nazwisko:')
nazwisko_label.pack()

nazwisko_entry = tk.Entry(root)
nazwisko_entry.pack()

historia_chorob_label = tk.Label(root, text='Historia chorób:')
historia_chorob_label.pack()

historia_chorob_text = tk.Text(root, height=5, width=30)
historia_chorob_text.pack()

aktualne_leki_label = tk.Label(root, text='Aktualne leki:')
aktualne_leki_label.pack()

aktualne_leki_text = tk.Text(root, height=5, width=30)
aktualne_leki_text.pack()

wyniki_badan_label = tk.Label(root, text='Wyniki badań:')
wyniki_badan_label.pack()

wyniki_badan_text = tk.Text(root, height=5, width=30)
wyniki_badan_text.pack()

alergie_label = tk.Label(root, text='Alergie:')
alergie_label.pack()

alergie_text = tk.Text(root, height=5, width=30)
alergie_text.pack()

# Przycisk aktualizacji profilu
aktualizuj_button = tk.Button(root, text='Aktualizuj profil', command=aktualizuj_profil)
aktualizuj_button.pack()

# Wypełnienie pól danymi z profilu pacjenta (opcjonalne)
imie_entry.insert(tk.END, profil_pacjenta['Imię'])
nazwisko_entry.insert(tk.END, profil_pacjenta['Nazwisko'])
historia_chorob_text.insert(tk.END, profil_pacjenta['Historia chorób'])
aktualne_leki_text.insert(tk.END, profil_pacjenta['Aktualne leki'])
wyniki_badan_text.insert(tk.END, profil_pacjenta['Wyniki badań'])
alergie_text.insert(tk.END, profil_pacjenta['Alergie'])

# Uruchomienie pętli głównej aplikacji
root.mainloop()
