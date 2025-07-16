
import math

# Constants
m = 0.510998928  # MeV
K = 0.307075     # MeV·mol⁻¹·cm²
re = 2.8179403267  # fm
kr = 2 * math.pi * (re * 1e-13)**2 * m * 1e6  # cm²·eV
alpha = 1 / 137.036 # fine structure constant
z = 1 # particle charge

# Input
material = "argon"
state = "liquid"

# Initialize
Ion = Z = A = Temp = pressure = Den = Omega_p = Ecritem = Ecritep = Ecritmu = None

if material == "argon" and state == "liquid":
    Ion = 188.0  # eV doe argon
    Z = 18
    A = 39.948
    Temp = 87
    pressure = 1.0  # bar
    Den = -0.00615 * Temp + 1.928 # density for liquid Ar in gm/cc
    Omega_p = math.sqrt((Den * Z)/ A) * 28.816
    Ecritem = 32.84 # MeV for electron critical energy
    Ecritep = 31.91 # MeV for positron critical energy
    Ecritmu = 485000 # MeV for muon critical energy

if material == "argon" and state == "gas" :
    Ion = 188.0  # eV for argon
    Z = 18
    A = 39.948
    Temp = 300 # for room temp
    pressure = 1.0 # bar
    Den = 1.662e-3 * pressure * (300 / Temp) # density for gas Ar in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816
    Ecritem = 38.03 # MeV for electron critical energy
    Ecritep = 37.06 # MeV for positron critical energy
    Ecritmu = 572000 # MeV for muon critical energy

if material == "krypton" and state == "liquid" :
    Ion = 352.0 # eV for argon
    Z = 36
    A = 83.798 
    Temp = 119.9 #  for krypton
    pressure = 1.0 # bar
    Den = 2.42 # density for liquid Kr in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816 # plasma eV
    Ecritem = 17.03 # MeV for electron critical energy
    Ecritep = 16.51 # MeV for positron critical energy
    Ecritmu = 277000.0 # MeV for muon critical energy

if material == "krypton" and state == "gas" : 
    Ion = 352.0 # eV for krypton
    Z = 36
    A = 83.798 
    Temp = 300 # for room temp
    pressure = 1.0 # bar
    Den = 1.662e-3 * pressure * (300/Temp) # density for gas Kr in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816
    Ecritem = 18.61 # MeV for electron critical energy
    Ecritep = 18.06 # MeV for positron critical energy
    Ecritmu = 324000 # MeV for muon critical energy
    
if material == "silicon" : 
    Ion = 173.0 # eV for silicon
    Z = 14
    A = 28.0854
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 2.33 # density for silicon in gm/cc
    Omega_p = math.sqrt((Den* Z) / A) * 28.816
    Ecritem = 40.19 # MeV for electron critical energy
    Ecritep = 39.0 # MeV for positron critical energy
    Ecritmu = 324000 # MeV for muon critical energy
    
if material == "xenon" and state == "liquid" : 
    Ion = 482.0 # eV for xenon
    Z = 54
    A = Z / 0.41130
    Temp = 165.05 # for argon
    pressure = 1 # bar
    Den = -0.00746 * (Temp - 161.4) + 2.978 # density for liquid Xe in gm//cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816
    Ecritem = 11.66 # MeV for electron critical energy
    Ecritep = 11.28 # MeV for postiron crtical energy
    Ecritmu = 200000 # MeV for muon critical energy
    
if material == "xenon" and state == "gas" :
    Ion = 482.0 # eV for xenon
    Z = 54.0
    A = Z / 0.41130
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 5.894e-3 * pressure * (300/Temp) # density for gas Xe in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816    
    Ecritem = 12.3 # MeV for electron critcal energy
    Ecritep = 11.91 # MeV for positron critical energy
    Ecritmu = 232000 # MeV for muon critical energy
    
if material == "water" and state == "liquid" : 
    Ion = 75.0
    Z = (1 + 1 + 8) / 3 # average Z
    A = (1.008 + 1.008 + 15.999) / 3 # average A
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 1 # density for liquid in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816
    Ecritem = 78.33 # MeV for electron critical energy
    Ecritep = 76.24 # MeV for positron critical energy
    Ecritmu = 1029000 # MeV for muon critical energy
    
if material == "scintillator" and state == "liquid" :
    # assume it is polyethelene C2H4
    Ion = 62.5 # ev for scintillator
    Z = (8 + 7 * 6) / 15 # average Z
    A = (8 * 1.008 + 7 * 12.0107) / 6 # average A
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 0.8669 # density for liquid in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816 
    Ecritem = 95.06 # Mev for electron critical energy
    Ecritep = 92.57 # MeV for postiron critical energy
    Ecritmu = 1204000 # MeV for muon critical energy

if material == "scintillator" and state == "solid" :
    Ion = 57.4 
    Z = (4 + 2 * 6) / 6 # average Z
    A = (2) / 6 # average A
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 1.023 # density for solid in gm/cc 
    Omega_p = math.sqrt((Den * Z) / A) * 28.816
    Ecritem = 101.79 # MeV for electron critical energy
    Ecritep = 99.13 # MeV for positron critical energy
    Ecritmu = 1282000 # MeV for muon critical energy
    
if material == "cf4" and state == "gas" :
    Ion = 107.127 # ev for cf4 from 1505.00701
    # Z = 42; A = Z/0.41130
    Z = (6 + 4 * 9) / 5 # average Z
    A = (12.0107 + 4 * 18.998403) / 5 # average A
    Temp = 300 # for room temp
    pressure = 2 # bar
    Den = 3.26e-3 * pressure * (300/Temp) # density for gas in gm/cc
    Omega_p = math.sqrt((Den * Z) / A) * 28.816 
    Ecritem = 83.0 # MeV using 800 / (Z + 1.2)
    Ecritep = 81.0 # MeV for positron critcial energy simply assuming 83-2
    Ecritmu = 1214000 # MeV for muon critcial energy simply assuming 14000 * Ecritem
    
if material == "iron" :
    Ion = 286.0 # ev for cf4
    Z = 26 
    A = 55.845 # average A
    Temp = 300 # for room temp
    pressure = 1 # bar
    Den = 7.874 # density for solid in gm/cc
    Omega_p = 55.17 #using Sqrt[Den*Z/A]*28.816
    Ecritem = 32.84 # MeV using 31.91 for e^+
    Ecritep = 31.91 # MeV positron critical energy
    Ecritmu = 485000 # MeV for muon critical energy
    
# Output
print(f"Ionization Energy: {Ion} eV")
print(f"Z = {Z}, A = {A}, Temp = {Temp} K, Pressure = {pressure} bar")
print(f"Density = {Den:.5f} g/cm³")
print(f"Plasma energy (Ωp) = {Omega_p:.5f} eV")
print(f"Critical Energies:\n  Electron = {Ecritem} MeV\n  Positron = {Ecritep} MeV\n  Muon = {Ecritmu} MeV")
