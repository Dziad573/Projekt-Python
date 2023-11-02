import tkinter as tk

przyciski = ['%', 'x^2', 'C', '\u21BA', '=', '0', ',', '+', '\u221A', '(', ')', 'pi', '7', '8', '9', '/', '4', '5', '6', 'x', '1', '2', '3', '-', '=', '0', ',', '+']

def inicjalizacjaOkna():
    root = tk.Tk()
    root.geometry('1022x820')
    root.title('Kalkulator')
    # root.resizable(False, False)
    return root

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
def inicjalizacjaPrzyciskow(kontenerEkranu):
    przyciska = [tk.Button(kontenerEkranu, text=przycisk, width=18, height=4, pady=18, padx=11, borderwidth=1) for przycisk in przyciski]

    j = 1
    for i in range(len(przyciski)):
        if i % 4 == 0:
            j += 1
        przyciska[i].grid(row=j, column=i % 4, columnspan=1, pady=2, padx=2)

    return przyciska

def inicjalizacjaKontenera(root):
    kontener = tk.Frame(root, bg='green', width=60, height=50)
    kontener.grid(row=0, columnspan=2, column=3)
    return kontener

# ROZMIAR DLA 1 = 70 (WYSOKOŚĆ)
def inicjalizacjaKonteneraEkranuOperacji(kontener):
    czcionka = ("Arial", 25)
    kontenerEkranuOperacji = [tk.Label(kontener, text="to jest text", font=czcionka, anchor='w', fg="white", bg='#292929', width=19, height=2, padx=12) for i in range(10)]
    for i in range(len(kontenerEkranuOperacji)):
        kontenerEkranuOperacji[i].grid(row=i, column=4, columnspan=2)
    return kontenerEkranuOperacji

if __name__ == '__main__':
    root = inicjalizacjaOkna()
    kontenerEkranu = inicjalizacjaKonteneraEkranu(root)
    ekran = inicjalizacjaEkranu(root)
    label = label(kontenerEkranu)
    przyciska = inicjalizacjaPrzyciskow( kontenerEkranu)
    kontener = inicjalizacjaKontenera(root)
    kontenerEkranuOperacji = inicjalizacjaKonteneraEkranuOperacji(kontener)
    root.mainloop()
