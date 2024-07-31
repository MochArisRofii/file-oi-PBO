def membaca(nama_file):
    with open(nama_file, "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis(nama_file):
    
    membaca("file.txt")

    nama_anime = input("Nama Anime: ")
    text = "\n {}".format(nama_anime)


    with open(nama_file, "a") as file_anime:
        file_anime.write(text)

menulis("file.txt")
