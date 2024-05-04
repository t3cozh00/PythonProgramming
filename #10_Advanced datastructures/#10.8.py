##8
#-*- coding: cp1252 -*-
import pickle
  
listexample = ["Pineapple", "Atlas", ("Shaft", "Blade"), 1150]
filename = open("saveme.dat","wb")
print(listexample)
pickle.dump(listexample,filename)

filename.close()

filename = open("saveme.dat","rb")
justread = pickle.load(filename)
  
print("Following was just read: ",justread)
print(justread[2],justread[3])
filename.close()