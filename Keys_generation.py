# Importer le module bitstring
from bitstring import BitArray

# Définir la fonction de permutation H
H = [6, 5, 2, 7, 4, 1, 3, 0]

# Définir la clé principale K de longueur 8
K = BitArray('0b10100111')

# Appliquer la fonction de permutation H à K
K.permute(H)

# Diviser K en deux blocs de 4 bits: K'1 et K'2
K1, K2 = K[:4], K[4:]

# Calculer k1 = K'1 XOR K'2 et k2 = K'1 AND K'2
k1 = K1 ^ K2
k2 = K1 & K2

# Appliquer le décalage à gauche d'ordre 2 pour k1 et le décalage à droite d'ordre 1 pour k2
k1.rol(2)
k2.ror(1)

# Afficher les deux sous-clés k1 et k2
print(f"Les deux sous-clés sont: {k1.bin} et {k2.bin}")
