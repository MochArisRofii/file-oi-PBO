from FilClass import HandleFile

def Baca_Class():
    file = HandleFile()
     
    file.baca_file('Output.txt')
    
    file.tulis_file('Output.txt', 'a') # Bisa Ganti Mode Sesuka Hati "tulis_file("nama_file", "mode")"

Baca_Class()