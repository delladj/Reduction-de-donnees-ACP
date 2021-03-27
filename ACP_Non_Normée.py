import numpy as np

#ACP Non Normée :

#---1-Centrer les données---
def Centrer(dataset) :
  X=dataset
  #2-1-Centre de gravité
  g=np.mean(X,axis=0)
  #2-2-Matrice centrée
  Ig=[g]*len(X)
  Ig=np.array(Ig)
  Y=X-Ig
  return(Y)

#---2-Matrice Variance Covariance---
def Var_Covar(Y) :
  p=1/len(Y)
  Dp=np.diag([p]*len(Y))
  V=Y.transpose().dot(Dp).dot(Y)
  return(V)


def Vect_Val_Prop(R) :
#4-1-Vecteurs et valeurs propres :
  Val_Prop, Vect_Prop = np.linalg.eig(R)
  idx = Val_Prop.argsort()[::-1]   
  Val_Prop = Val_Prop[idx]
  Vect_Prop = Vect_Prop[:,idx]
#4-2-Choix des axes :
#4-2-1-Calcul de l'inertie totale :
  I_t = R.trace()
#4-2-2 Pourcentage des données exprimées par chaque valeur propre :
  Ex=[]
  for i in range(len(Val_Prop)) :
    Ex.append(Val_Prop[i]/I_t)
  Ex=np.array(Ex)
#4-2-3 Données exprimées cumulées :   
  for i in range(1,len(Val_Prop)) :
    Ex[i]=Ex[i]+Ex[i-1]      
#4-2-4- Axes Choisis (57% des données sont récupérés avec Landa 1 et Landa 2) :
  Landas = [Val_Prop[0],Val_Prop[1],Val_Prop[2]]
  U=[Vect_Prop[0],Vect_Prop[1],Vect_Prop[2]]
  return[Landas,U,Val_Prop]

#---5-Calcul des composantes principales :---
def Composantes(Y,U1,U2) :
  C1 = Y.dot(U1)
  C2 = Y.dot(U2)
  C=np.array([C1,C2])
  return(C)    

#---6-Corrélation entre anciennes et nouvelles variables :---
def New_Correl(U,Landas,V) :
  Correl=[]    
  for i in range(len(Landas)) :
    t=[]
    for j in range(len(V)) :
        t.append(np.sqrt(Landas[i])*U[i][j]/np.sqrt(V[j][j]))
    Correl.append(t)
  return(np.array(Correl))

#---7-Contribution absolue de chaque individu :---  
def Contribution(C,Landas,p) : 
  Contr = []
  for i in range(len(C)) :
    t=[]
    for j in range(len(C[0])) :
        t.append(p*C[i,j]/Landas[i])
    Contr.append(t)
  return(np.array(Contr))

def ACP_N_N(dataset) :
  Y=np.around(Centrer(dataset),6)
  print('La matrice centrée : \n'+str(Y))
  
  V=np.around(Var_Covar(Y),6)
  print('La matrice Variance Covariance : \n'+str(V))
  
  VVP=Vect_Val_Prop(V)
  Landas,U=np.around(VVP[0],6),np.around(VVP[1],6)
  print('Valeurs propres :\n'+str(Landas))
  print('Vecteurs propres : \nU1 :\n'+str(U[0])+'\n U2 : \n'+str(U[1]))
  
  C=np.around(Composantes(Y,U[0],U[1]),6)
  print('Composantes principale :\n'+str(C))
  
  Contr=np.around(Contribution(C,Landas,1/len(Y)),6)
  print('Contribution absolue de chaque individu :\n'+str(Contr))  
  
  Coef=np.around(New_Correl(U,Landas,V),6)
  print('Corrélation avec les nouvelles variable : \n'+str(Coef))
  
  return([C,Coef,VVP[2]])
