import math
import numpy as np

X = 0
# Aprire un file in modalità scrittura ('w' per scrivere, sovrascrive il contenuto se il file esiste)
with open("output.txt", "a") as file:
    for i in range(1,5):
        for j in range(1,21):
            X = i+j
            file.write(str(X) + "\n")  # Converto valore in stringa prima di scrivere


