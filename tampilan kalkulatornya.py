import tkinter as tk
from tkinter import messagebox

def klik(tombol):
    if tombol == "=":
        try:
            hasil = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, hasil)
        except:
            messagebox.showerror("Error", "Input tidak valid!")
    elif tombol == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, tombol)

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("300x400")
root.configure(bg="#1e1e1e")

# Entry tempat menampilkan input dan hasil
entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.FLAT, justify="right", bg="#2e2e2e", fg="#ffffff")
entry.pack(pady=20, padx=10, fill=tk.BOTH)

# Tombol-tombol kalkulator
tombol_frame = tk.Frame(root, bg="#1e1e1e")
tombol_frame.pack(padx=10, fill=tk.BOTH, expand=True)

tombol_list = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for baris in tombol_list:
    baris_frame = tk.Frame(tombol_frame, bg="#1e1e1e")
    baris_frame.pack(expand=True, fill="both")
    for tombol in baris:
        btn = tk.Button(baris_frame, text=tombol, font=("Arial", 20), bd=0, bg="#3e3e3e", fg="white",
                        activebackground="#5e5e5e", activeforeground="white",
                        command=lambda t=tombol: klik(t))
        btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)

root.mainloop()
