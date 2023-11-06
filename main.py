import tkinter as tk

przyciski = ['0', '0', '0', '0', '\u221A', '%', 'x^2', 'C', '\u21BA', '(', ')', 'pi', '7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '-', '=', '0', ',', '+']

def inicjalizacjaOkna():
    root = tk.Tk()
    root.geometry('1022x820')
    root.title('Kalkulator')
    # root.resizable(False, False)
    return root

# Ekran wyświetlania operacji
def inicjalizacjaEkranu(root):
    ekran = tk.Text(root, bg="black", width=77, height=10, borderwidth=0, padx=10, pady=7, fg='white')
    ekran.grid(row=0, column=0, columnspan=3, sticky="n")
    return ekran

def inicjalizacjaKonteneraEkranu(root):
    kontenerEkranu = tk.Label(root, bg='#4e4e4e', width=90, height=53, pady=11)
    kontenerEkranu.grid(row=0, column=0, columnspan=3)
    return kontenerEkranu

def label(kontenerEkranu):
    label = tk.Label(kontenerEkranu, bg="red", pady=24)
    label.grid(row=1, column=0, columnspan=3)
    return label

# Operacje na przyciskach
def klik(ekran, przycisk, oknoHistorii):
    def obsluga():
        if przycisk == '\u21BA':
            bufor = ekran.get(1.0, 'end-2c')
            ekran.delete(1.0, tk.END)
            ekran.insert(1.0, bufor)
        elif przycisk == 'C':
            ekran.delete(1.0, tk.END)
        elif przycisk == '=':
            zaktualizujHistorie(ekran)()
        else:
            tekst = przycisk if przycisk != 'x^2' else '^2'
            ekran.insert(tk.END, tekst)
    return obsluga

def zaktualizujHistorie(ekran):
    def f():
        tekst = ekran.get(1.0, 'end-1c')
        for i in range(len(oknoHistorii)):
            if not oknoHistorii[i]['text']:
                oknoHistorii[i]['text'] = oknoHistorii[i - 1]['text']
                oknoHistorii[i]['text'] = tekst
                break
    return f

def inicjalizacjaPrzyciskow(kontenerEkranu, oknoHistorii):
    przyciska = [tk.Button(kontenerEkranu, text=przycisk, width=18, height=4, pady=18, padx=11, borderwidth=1) for przycisk in przyciski]

    j = 1
    for i in range(len(przyciski)):
        if i % 4 == 0:
            j += 1
        przyciska[i].grid(row=j, column=i % 4, columnspan=1, pady=2, padx=2)
        przyciska[i].configure(command=klik(ekran, przyciska[i]['text'], oknoHistorii))

    return przyciska

def inicjalizacjaKonteneraHistorii(root):
    kontenerHistorii = tk.Frame(root, bg='green', width=60, height=50)
    kontenerHistorii.grid(row=0, columnspan=2, column=3)
    return kontenerHistorii

# ROZMIAR DLA 1 = 70 (WYSOKOŚĆ)
def inicjalizacjaOknaHistorii(kontenerHistorii):
    czcionka = ("Arial", 25)
    oknoHistorii = [tk.Label(kontenerHistorii, text="", font=czcionka, anchor='w', fg="white", bg='#292929', width=19, height=2, padx=12) for i in range(10)]
    for i in range(len(oknoHistorii)):
        oknoHistorii[i].grid(row=i, column=4, columnspan=2)
    return oknoHistorii

if __name__ == '__main__':
    root = inicjalizacjaOkna()
    kontenerEkranu = inicjalizacjaKonteneraEkranu(root)
    ekran = inicjalizacjaEkranu(root)
    label = label(kontenerEkranu)
    przyciska = inicjalizacjaPrzyciskow(kontenerEkranu, 1)
    kontenerHistorii = inicjalizacjaKonteneraHistorii(root)
    oknoHistorii = inicjalizacjaOknaHistorii(kontenerHistorii)
    root.mainloop()
