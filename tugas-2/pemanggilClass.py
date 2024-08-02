from FilClass import HandleFile

def Baca_Class():
    file_handler = HandleFile()
     
    file_handler.tulis_file('Output.txt', 'a') # Bisa Ganti Mode Sesuka Hati "tulis_file("nama_file", "mode")"

    # file_handler.baca_file('contoh.txt')

Baca_Class()