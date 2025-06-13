import math

def hitung_rangkaian(R, L, C, f=50, V=200):
    pi = math.pi
    omega = 2 * pi * f
    X_L = omega * L
    X_C = 1 / (omega * C)
    Z = math.sqrt(R**2 + (X_L - X_C)**2)
    I = V / Z
    cos_phi = R / Z
    phi_rad = math.acos(cos_phi)
    phi_deg = math.degrees(phi_rad)
    sin_phi = math.sin(phi_rad)
    P = V * I * cos_phi
    Q = V * I * sin_phi
    S = math.sqrt(P**2 + Q**2)

    if X_L > X_C:
        sifat = "Lagging (Induktif)"
    elif X_C > X_L:
        sifat = "Leading (Kapasitif)"
    else:
        sifat = "Netral (Resonansi)"

    return {
        "omega": omega,
        "X_L": X_L,
        "X_C": X_C,
        "Z": Z,
        "I": I,
        "cos_phi": cos_phi,
        "phi_deg": phi_deg,
        "P": P,
        "Q": Q,
        "S": S,
        "sifat": sifat
    }
