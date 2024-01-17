
if __name__ == '__main__':

    print("Hallo Sandro!")
    print("Hallo Datio!")

import tkinter as tk

def on_close():
    root.destroy()

root = tk.Tk()
root.title("Weißes Fenster")
root.configure(bg="white")

# Schließkästchen hinzufügen
close_button = tk.Button(root, text="Schließen", command=on_close)
close_button.pack(side=tk.BOTTOM, pady=10)

# Andere UI-Elemente oder Funktionen können hier hinzugefügt werden.

root.mainloop()
