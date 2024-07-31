def membaca():
    with open('tugas-operasi-file/file.txt', "r") as file_txt:
        file_content = file_txt.read()
        print(file_content)

def menulis():
    
    membaca()

    nama_anime = input("Nama Anime: ")
    text = "\n {}".format(nama_anime)


    with open("tugas-operasi-file/file.txt", "a") as file_anime:
        file_anime.write(text)

menulis()
