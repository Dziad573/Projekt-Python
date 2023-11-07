import tkinter as tk

przyciski = [
     '7', '8', '9', '-',
     '(', ')','\u21BA', 'C',
     '7', '8', '9','-',
     '4', '5', '6','/',
     '1', '2', '3','*',
     'x^2', '0', '+','=',
]


def infix_na_onp(wyrazenie):
    dzialania = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }

    stos = []
    onp = ''
    for w in wyrazenie:
        if w == '(':
            stos.append(w)
        elif w == ')':
            while stos and stos[-1] != '(':
                onp += stos.pop()
            stos.pop()  # Usuń otwierający nawias '('
        elif w in dzialania:
            while stos and stos[-1] != '(' and dzialania.get(stos[-1], 0) >= dzialania.get(w, 0):
                onp += stos.pop()
            stos.append(w)
        else:
            onp += w
    while stos:
        onp += stos.pop()
    print(onp)
    return onp

def oblicz_onp(onp):
    stos = []
    for znak in onp:
        if znak.isdigit():
            stos.append(float(znak))
        elif znak in "+-*/^":
            b = stos.pop()
            a = stos.pop()
            if znak == '+':
                stos.append(a + b)
            elif znak == '-':
                stos.append(a - b)
            elif znak == '*':
                stos.append(a * b)
            elif znak == '/':
                stos.append(a / b)
            elif znak == '^':
                stos.append(a ** b)
    if len(stos) == 1:
        return stos[0]
    else:
        return "Błąd"


def inicjalizacjaOkna():
    root = tk.Tk()
    root.geometry('1016x712')
    root.title('Kalkulator')
    return root

def inicjalizacjaEkranu(root):
    ekran = tk.Text(root, bg="black", width=77, height=10, borderwidth=0, padx=10, pady=7, fg='white')
    ekran.grid(row=0, column=0, columnspan=3, sticky="n")
    return ekran

def inicjalizacjaKonteneraEkranu(root):
    kontenerEkranu = tk.Label(root, bg='#4e4e4e', fg='white', width=90, height=53, pady=11)
    kontenerEkranu.grid(row=0, column=0, columnspan=3)
    return kontenerEkranu

def inicjalizacjaKonteneraHistorii(root):
    kontenerHistorii = tk.Text(root, bg='#292929', fg='white', width=45, height=43, pady=12, padx=10)
    kontenerHistorii.grid(row=0, rowspan=5, column=5, columnspan=3, sticky="n")
    return kontenerHistorii

def label(kontenerEkranu):
    label = tk.Label(kontenerEkranu, bg="red", pady=24)
    label.grid(row=1, column=0, columnspan=3)
    return label

def klik(ekran, przycisk, oblicz):
    def obsluga():
        if przycisk == '=':
            wyrazenie = ekran.get('1.0', tk.END).strip()
            onp = infix_na_onp(wyrazenie)
            wynik = oblicz_onp(onp)
            ekran.delete('1.0', tk.END)
            ekran.insert(tk.END, str(wynik))
            kontenerHistorii.insert(tk.END, str(wyrazenie) + ' = ' + str(wynik) + '\n')
        elif przycisk == 'C':
            ekran.delete('1.0', tk.END)
        elif przycisk == 'x^2':
            tekst = przycisk if przycisk != 'x^2' else '^2'
            ekran.insert(tk.END, tekst)
        elif przycisk == '\u21BA':
            bufor = ekran.get(1.0, 'end-2c')
            ekran.delete(1.0, tk.END)
            ekran.insert(1.0, bufor)
        else:
            ekran.insert(tk.END, przycisk)
    return obsluga


def oblicz(ekran, kontenerHistorii):
    wyrazenie = ekran.get('1.0', tk.END)
    wyrazenie = wyrazenie.strip()  # Usuń białe znaki na początku i końcu
    try:
        #wynik = str(eval(wyrazenie))
        #kontenerHistorii.insert(tk.END, wyrazenie + ' = ' + wynik + '\n')
        ekran.delete('1.0', tk.END)
        #ekran.insert(tk.END, wynik)
    except Exception as e:
        ekran.delete('1.0', tk.END)
        ekran.insert(tk.END, 'Błąd')


def inicjalizacjaPrzyciskow(kontenerEkranu, ekran):
    button = {}
    j = 1
    for i, przycisk in enumerate(przyciski):
        if i % 4 == 0:
            j += 1
        button[i] = tk.Button(kontenerEkranu, text=przycisk, width=18, height=4, pady=18, padx=11, borderwidth=1)
        button[i].grid(row=j, column=i % 4, columnspan=1, pady=2, padx=2)
        button[i].configure(command=klik(ekran, przycisk, oblicz))

    return button

if __name__ == '__main__':
    root = inicjalizacjaOkna()
    kontenerEkranu = inicjalizacjaKonteneraEkranu(root)
    ekran = inicjalizacjaEkranu(root)
    label = label(kontenerEkranu)
    button = inicjalizacjaPrzyciskow(kontenerEkranu, ekran)
    kontenerHistorii = inicjalizacjaKonteneraHistorii(root)
    root.mainloop()