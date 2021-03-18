import numpy as np
import ACP_Non_Normée as a_n_n

#ACP Normée :
    
#Centrer et réduire les données :
def Centr_Red(X) :
  Y=np.around(a_n_n.Centrer(X),6)
  V=np.around(a_n_n.Var_Covar(Y),6)
  t=V
  for i in range(len(t)) :
      t[i][i]=np.sqrt(t[i][i])
  Dp=np.linalg.inv(np.diag(np.diag(t)))
  Z=Y.dot(Dp)
  return Z

#Matrice de corrélation :
def Correl(Z) :
     p=1/len(Z)
     Dp=np.diag([p]*len(Z))
     R=Z.transpose().dot(Dp).dot(Z)
     return(R)

#---pour la suite de l'acp , on utilise les fonction déja codés dans l'acp non normée---

def ACP_N(dataset) :
  Z=np.around(Centr_Red(dataset),6)
  print('La matrice centrée réduite : \n'+str(Z))
  R=np.around(Correl(Z),6)
  print('Matrice de corrélation : \n'+str(R))
  VVP=a_n_n.Vect_Val_Prop(R)
  Landas,U=np.around(VVP[0],6),np.around(VVP[1],6)
  print('Valeurs propres :\n'+str(Landas))
  print('Vecteurs propres : \nU1 :\n'+str(U[0])+'\n U2 : \n'+str(U[1]))
  C=np.around(a_n_n.Composantes(Z,U[0],U[1]),6)
  print('Composantes principale :\n'+str(C))
  Contr=np.around(a_n_n.Contribution(C,Landas,1/len(Z)),6)
  print(Contr)
  #print('Contribution absolue de chaque individu :\n'+str(Contr))  
  Coef=np.around(a_n_n.New_Correl(U,Landas,R),6)
  print('Corrélation avec les nouvelles variable : \n'+str(Coef))
  return([C,Coef])
