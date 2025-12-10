# 📘 Jupyter Notebook Cell Combiner

This Python + Tkinter application allows you to select a **.ipynb** file and automatically combine the contents of all **code** and **markdown** cells into a single text file.

It's especially useful for:
- Exporting notebook content as plain text  
- Reviewing or sharing notebook content without opening Jupyter  
- Creating printable versions of notebooks  

---

## 🚀 Features

- Simple graphical interface built with Tkinter  
- Select a `.ipynb` file from your system  
- Automatically extracts `code` and `markdown` cell content  
- Combines all extracted content in the correct order  
- Saves the merged result as a `.txt` file  
- Clear user feedback with success, warning, and error pop-ups  

---

## 🛠️ Requirements

- Python 3.x  
- Standard libraries (included by default):
  - `json`
  - `tkinter`

No additional installation is required.

---

## 📦 Installation

Clone this repository:

```bash
git clone https://github.com/coconutpr/ipynb-to-txt-converter.git
cd ipynb-to-txt-converter
