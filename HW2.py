club1 = input("Klub A: ")
club2 = input("Klub B: ")

result = []
match = False
i = 1
while (not match):
    a, b = map(int,input(f"pertandingan ke-{i}: ").split())
    if a < 0 or b < 0:
        match = True
    else:
        if a > b:
            result.append(club1)
        elif a < b:
            result.append(club2)
        else:
            result.append("Draw")
        i += 1
for i in range(len(result)):
    print(f'Hasil {i+1} : {result[i]}')
print('Pertandingan selesai')