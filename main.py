import tkinter as tk

def inicjalizacjaOkna():
    root = tk.Tk()
    root.geometry('1022x820')
    root.title('Kalkulator')
    #root.resizable(False, False)
    return root

def inicjalizacjaEkranu(root):
    ekran = tk.Label(root, bg='#4e4e4e', width=90, height=50, pady=33)
    ekran.grid(row=0, column=0)
    return ekran

def inicjalizacjaKontenera(root):
    kontener = tk.Frame(root, bg='green', width=60, height=50)
    kontener.grid(row=0, column=1)
    return kontener

#ROZMIAR DLA 1 = 70 (WYSOKOŚĆ)
def inicjalizacjaEkranuOperacji(kontener):
    czcionka = ("monospace", 25)
    ekranOperacji = [tk.Label(kontener, text="to jest text", font=czcionka, fg="white", bg='#292929', width=20, height=2) for i in range(10)]
    for i in range(len(ekranOperacji)):
        ekranOperacji[i].grid(row=i, column=1)
    return ekranOperacji

if __name__ == '__main__':
    root = inicjalizacjaOkna()
    ekran = inicjalizacjaEkranu(root)
    kontener = inicjalizacjaKontenera(root)
    ekranOperacji = inicjalizacjaEkranuOperacji(kontener)
    root.mainloop()