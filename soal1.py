arrBerat = []
bMin = 0
bMax = 0

def hitungMinMax(arrBerat):
    global bMin, bMax
    # Definisikan Proses Mencari Berat Maximum Dan Minimum
    bMax = max(arrBerat)
    bMin = min(arrBerat)
    print("Berat balita maksimum: {:.2f} kg".format(bMax))
    print("Berat balita minimum: {:.2f} kg".format(bMin))

def rerata(arrBerat):
    total = 0

    # Definisikan Proses Mencari Rerata Dari Total Berat
    rata = sum(arrBerat)/n
    print("Rerata berat balita: {:.2f} kg".format(rata))

    # Return Hasil Rerata
    return rata

print('Masukkan Banyak Data Berat Balita :', end=" ")
n = int(input())

for i in range(n):
    print(f'Masukkan Berat Balita Ke-{i+1} :', end=' ')
    # Inisialisasi Input Data Berat
    x = float(input())

    # Masukkan Data Berat Ke Array (arrBerat)
    x = arrBerat.append(x)

# Panggil procedur hitungMinMax(arrBerat)
hitungMinMax(arrBerat)

# Print Data Minimum, Maximum, dan Rerata Berat
rerata(arrBerat)