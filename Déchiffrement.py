#Importer le module bitstring
from bitstring import BitArray

#Définir la permutation π
pi = [4, 6, 0, 2, 7, 3, 1, 5]

# Définir la permutation inverse de π
pi_inv = [2, 6, 3, 5, 0, 7, 1, 4]

#Définir la permutation P
P = [2, 0, 1, 3]

# Définir la fonction f
def f(x, k):
    # Calculer 2^i * k
    i = k.count(1) # compter le nombre de bits à 1 dans k
    p = 2 ** i * k.uint # convertir k en entier non signé
    # Calculer p ^ x
    q = p ^ x.uint # convertir x en entier non signé
    # Calculer q % (2^32 - 1)
    r = q % (2 ** 32 - 1)
    # Convertir r en bitarray de longueur 32
    s = BitArray(uint=r, length=32)
    # Retourner s
    return s

# Définir la fonction de déchiffrement de Feistel
def feistel_decrypt(N, k1, k2):
    # Appliquer la permutation π à N
    N.permute(pi)
    # Diviser N en deux blocs de 4 bits: G0 et D0
    G0, D0 = N[:4], N[4:]
    # Premier round, calculer:
    # D1 = P(G0) ⊕ k1 et
    # G1 = D0 ⊕ (G0 ∨ k1)
    D1 = P(G0) ^ k1
    G1 = D0 ^ (G0 | k1)
    # Deuxième round, calculer:
    # D2 = P(G1) ⊕ k2 et
    # G2 = D1 ⊕ (G1 ∨ k2)
    D2 = P(G1) ^ k2
    G2 = D1 ^ (G1 | k2)
    # C = G2 D2 (la concaténation)
    C = G2 + D2
    # Appliquer l'inverse de la permutation π à C
    C.permute(pi_inv)
    # Retourner C
    return C

# Définir la clé principale K de longueur 8
K = BitArray('0b10100111')

# Appliquer la fonction de permutation H
H = [6, 5, 2, 7, 4, 1, 3, 0]
K.permute(H)

# Diviser K en deux blocs de 4 bits: K'1 et K'2
K1, K2 = K[:4], K[4:]

# Calculer k1 = K'1 XOR K'2 et k2 = K'1 AND K'2
k1 = K1 ^ K2
k2 = K1 & K2

# Appliquer le décalage à gauche d'ordre 2 pour k1 et le décalage à droite d'ordre 1 pour k2
k1.rol(2)
k2.ror(1)

# Définir le bloc N de 8 bits
N = BitArray('0b11001010')

# Appliquer la fonction de déchiffrement de Feistel à N avec k1 et k2
C = feistel_decrypt(N, k1, k2)

# Afficher le texte déchiffré C
print(f"Le texte déchiffré est: {C.bin}")
