#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:39:18 2024

@author: adesintia
"""

def sum_recursive(numbers, n):
    if n == 0:
        return 0
    return numbers[n - 1] + sum_recursive(numbers, n - 1)

jumlah = int(input("Masukkan Jumlah: "))
numbers = []

for i in range(jumlah):
    angka = int(input(f"Masukkan angka ke-{i + 1}: "))
    numbers.append(angka)

result = sum_recursive(numbers, jumlah)
print(f"Hasil dari penjumlahan adalah: {result}")

