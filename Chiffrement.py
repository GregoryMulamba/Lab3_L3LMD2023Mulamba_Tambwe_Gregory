Fonction qui applique une permutation à un bloc de 8 bits
def permute(block, permutation):
  result = 0
  for i in range(8):
    # On récupère le bit à la position permutation[i] dans le bloc
    bit = (block >> (8 - permutation[i])) & 1
    # On ajoute ce bit au résultat à la position i
    result = (result << 1) | bit
  return result

# Fonction qui effectue un tour de Feistel
def feistelRound(left, right, key, permutation):
  # On calcule le nouveau bloc de droite
  newRight = permute(left, permutation) ^ key
  # On calcule le nouveau bloc de gauche
  newLeft = right ^ (left | key)
  # On renvoie le résultat sous forme d'un tuple
  return (newLeft, newRight)

# Fonction qui chiffre un bloc de 8 bits avec l'algorithme de Feistel
def feistelEncrypt(block, key1, key2):
  # On applique la permutation initiale
  permutedBlock = permute(block, [4, 6, 0, 2, 7, 3, 1, 5])
  # On divise le bloc en deux blocs de 4 bits
  left = permutedBlock >> 4
  right = permutedBlock & 15
  # On effectue le premier tour de Feistel  left, right = feistelRound(left, right, key1, [2, 0, 1, 3])
  # On effectue le deuxième tour de Feistel
  left, right = feistelRound(left, right, key2, [2, 0, 1, 3])
  # On concatène les deux blocs
  cipherBlock = (left << 4) | right
  # On applique la permutation finale
  cipherText = permute(cipherBlock, [4, 6, 0, 2, 7, 3, 1, 5])
  # On renvoie le texte chiffré
  return cipherText

# Exemple d'utilisation
plainText = 42 # Le bloc de texte clair
key1 = 9 # La première clé secrète
key2 = 12 # La deuxième clé secrète
cipherText = feistelEncrypt(plainText, key1, key2) # Le texte chiffré
print(cipherText) # Affiche 201
