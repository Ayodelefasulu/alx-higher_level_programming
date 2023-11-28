#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j or j == i:
            continue
        print(f"{i}{j}, ", end="")
