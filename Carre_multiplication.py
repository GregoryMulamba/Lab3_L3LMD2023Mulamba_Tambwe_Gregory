#Fonction qui calcule x^b (mod n) par l'algorithme des carrés et des multiplications
def squareAndMultiply(x, b, n):
  # On convertit b en binaire
  b = bin(b)[2:]
  # On initialise le résultat à 1
  result = 1
  # On parcourt les bits de b de gauche à droite
  for bit in b:
    # On élève le résultat au carré
    result = (result * result) % n
    # Si le bit est 1, on multiplie le résultat par x
    if bit == "1":
      result = (result * x) % n
      # on renvoie le résultat

 return result

# Exemple d'utilisation
# On demande à l'utilisateur de saisir les valeurs de x, b et n
x = int(input("Entrez la valeur de x : "))
b = int(input("Entrez la valeur de b : "))
n = int(input("Entrez la valeur de n : "))
# On calcule x^b (mod n) par l'algorithme des carrés et des multiplications
result = squareAndMultiply(x, b, n)
# On affiche le résultat
print(f"{x}^{b} (mod {n}) = {result}")

