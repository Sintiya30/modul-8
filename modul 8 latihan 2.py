#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:33:31 2024

@author: adesintia
"""

def power_recursive(base, power):
    # Base case: pangkat 0 hasilnya adalah 1
    if power == 0:
        return 1
    # Recursive case: base * pangkat (power - 1)
    return base * power_recursive(base, power - 1)

# Input dari user
base = int(input("Masukkan angka awal (base): "))
power = int(input("Masukkan pangkat (power): "))

# Kalkulasi perpangkatan
result = power_recursive(base, power)

# Output hasil
print(f"Hasil dari {base}^{power} adalah {result}")
