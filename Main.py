import pandas as pd
import Pretrait as pt
import Graphique as grph
import ACP_Normée as a_n
import ACP_Non_Normée as a_n_n
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
#introduire ce fichier par l'interface graphique
def main(path, norme=True):
    dataset = pd.read_csv(path,header=0)
    dataset=dataset.iloc[range(len(dataset)),[9,10,11,12,13,14]]  
    X=pt.pretrait(dataset).to_numpy()
    if norme:
        return a_n.ACP_N(X)
    return a_n_n.ACP_N_N(X)


root = Tk()
root.title("projet ACP")
root.geometry("800x200")
url = None
x = ''
def open_file ():
    global url
    url = filedialog.askopenfilename(title= "open csv file", filetypes = (("csv files", "*.csv"),))
    lab.config(text = "le lien est :"+ str(url))

def hna(c1, c2, mat):
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    circle = Circle((0, 0), 1, facecolor="none", edgecolor="blue", linewidth=3)
    # affichage du cercle de correlation
    ax[0].spines["top"].set_color("none")
    ax[0].spines["left"].set_position("zero")
    ax[0].spines["right"].set_color("none")
    ax[0].spines["bottom"].set_position("zero")
    ax[0].set_xlabel("c1")
    ax[0].set_ylabel("c2")
    ax[0].add_patch(circle)

    ax[0].scatter(mat[0], mat[1], color="blue")
    ax[0].set(xlim=(-1, 1), ylim=(-1, 1))
    ax[0].set_title(
        "cercle de correlation entre\n les anciennes et nouvelles variables"
    )

    # affichage de compo principales
    ax[1].scatter(c1, c2, color="blue", label="projection des individus")
    ax[1].set_title(
        "la projection des individus sur les composantes \n principlae(C1, C2)"
    )
    ax[1].set_xlabel("c1")
    ax[1].set_ylabel("c2")
    plt.show()

norme = tk.IntVar()
n_norme = tk.IntVar()
lab = Label(root, text = x)
lab.pack()
def lancer():
    global url
    global lab
    if url == None or url == '':
        lab.config(text = "vous devez choisir le data set puis lancer le programme")
    else:
        global norme
        global n_norme
        (composants, coreelation) = main(url, True)
        if n_norme.get() == 1:
            (composants, coreelation) = main(url, False)

        hna(composants[0], composants[1], coreelation)


norme_button =  tk.Checkbutton(root, text='Normé',variable=norme, onvalue=1, offvalue=0)
norme_button.pack()

n_norme_button = tk.Checkbutton(root, text='Non Normé',variable=n_norme, onvalue=1, offvalue=0)

n_norme_button.pack()

button = Button(root, text = "open file", command = open_file)
button.pack()

lanceur = Button(root, text = "lancer le programme", command = lancer)
lanceur.pack()


root.mainloop()
