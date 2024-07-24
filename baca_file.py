file_pantun = open("file-oi/puisi.txt", "r")

# print(file_pantun.readlines())

pantun = file_pantun.readlines()

# print(pantun[0])

# print(pantun[2])


for teks in pantun:

   print(teks)


file_pantun.close()