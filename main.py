import tkinter as tk

def inicjalizacjaOkna():
    root = tk.Tk()
    root.geometry('1022x820')
    root.title('Kalkulator')
    #root.resizable(False, False)
    return root

def inicjalizacjakontenerEkranu(root):
    kontenerEkranu = tk.Label(root, bg='#4e4e4e', width=90, height=53, pady=11)
    kontenerEkranu.grid(row=0, column=0,)
    return kontenerEkranu

def inicjalizacjaEkranu(root, kontenerEkranu):
    ekran = tk.Text(root, bg="black",width=77, height=10, borderwidth=0, padx=10, pady=10)
    ekran.grid(row=0, column=0, sticky="n")
    #info = tk.Label(root, bg="yellow", width=77, height=10, borderwidth=0, padx=10, pady=10)
    #info.grid(row=0, column=0, sticky="w")
    return ekran
def inicjalizacjaKontenera(root):
    kontener = tk.Frame(root, bg='green', width=60, height=50)
    kontener.grid(row=0, column=1)
    return kontener

#ROZMIAR DLA 1 = 70 (WYSOKOŚĆ)
def inicjalizacjakontenerEkranuOperacji(kontener):
    czcionka = ("monospace", 25)
    kontenerEkranuOperacji = [tk.Label(kontener, text="to jest text", font=czcionka, anchor='w', fg="white", bg='#292929', width=19, height=2, padx=12) for i in range(10)]
    for i in range(len(kontenerEkranuOperacji)):
        kontenerEkranuOperacji[i].grid(row=i, column=1)
    return kontenerEkranuOperacji

if __name__ == '__main__':
    root = inicjalizacjaOkna()
    kontenerEkranu = inicjalizacjakontenerEkranu(root)
    ekran = inicjalizacjaEkranu(root, 1)
    kontener = inicjalizacjaKontenera(root)
    kontenerEkranuOperacji = inicjalizacjakontenerEkranuOperacji(kontener)
    root.mainloop()