import json
import tkinter as tk
from tkinter import filedialog, messagebox

def seleccionar_arxiu():
    """Obre un quadre de diàleg per seleccionar un fitxer .ipynb."""
    arxiu = filedialog.askopenfilename(
        title="Seleccionar fitxer .ipynb",
        filetypes=[("Jupyter Notebooks", "*.ipynb")]
    )
    return arxiu

def desar_contingut(contingut):
    """Obre un quadre de diàleg per desar el contingut en un fitxer."""
    arxiu_desat = filedialog.asksaveasfilename(
        title="Desar fitxer combinat",
        defaultextension=".txt",
        filetypes=[("Fitxers de text", "*.txt")]
    )
    if arxiu_desat:
        try:
            with open(arxiu_desat, 'w', encoding='utf-8') as output:
                output.write(contingut)
            messagebox.showinfo("Èxit", f"Contingut desat a:\n{arxiu_desat}")
        except Exception as e:
            messagebox.showerror("Error", f"S'ha produït un error en desar el fitxer:\n{e}")
    else:
        messagebox.showwarning("Avís", "No s'ha desat el fitxer.")

def processar_arxiu():
    """Processa el fitxer .ipynb seleccionat i desa el contingut combinat."""
    arxiu = seleccionar_arxiu()
    if not arxiu:
        messagebox.showwarning("Avís", "No s'ha seleccionat cap fitxer.")
        return
    
    try:
        # Llegeix el fitxer seleccionat
        with open(arxiu, 'r', encoding='utf-8') as file:
            notebook = json.load(file)
        
        # Combina el contingut de les cel·les
        contingut = ""
        for cel·la in notebook.get('cells', []):
            if cel·la.get('cell_type') in ['code', 'markdown']:
                contingut += ''.join(cel·la.get('source', [])) + "\n\n"
        
        # Desa el contingut combinat
        desar_contingut(contingut)
    except Exception as e:
        messagebox.showerror("Error", f"S'ha produït un error en processar el fitxer:\n{e}")

# Configura la interfície
finestra = tk.Tk()
finestra.title("Combinar cel·les de Jupyter Notebook")
finestra.geometry("400x200")

# Botó per iniciar el procés
boto = tk.Button(finestra, text="Seleccionar fitxer .ipynb", command=processar_arxiu, font=("Arial", 14))
boto.pack(pady=50)

# Executa la interfície
finestra.mainloop()
