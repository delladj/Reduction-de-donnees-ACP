import pandas as pd
import Pretrait as pt
import Graphique as grph
import ACP_Normée as a_n
import ACP_Non_Normée as a_n_n

#introduire ce fichier par l'interface graphique
dataset = pd.read_csv("dataset.csv",header=0)

#
dataset=dataset.iloc[range(len(dataset)),[9,10,11,12,13,14]]  
X=pt.pretrait(dataset).to_numpy()

#Elle retourne les valeurs prorpes + les composantes principales 
#+ la corrélation des anciennes variables avec les nouvelles
ACP_N_N=a_n_n.ACP_N_N(X)

#fonction d'affichage ( afficher les graphes dans l'interface graphique ) 
#a coder dans le fichier Graphique.py
grph.Afficher(ACP_N_N)

#Elle retourne les valeurs prorpes + les composantes principales 
#+ la corrélation des anciennes variables avec les nouvelles
ACP_N=a_n.ACP_N(X)

grph.Afficher(ACP_N)
