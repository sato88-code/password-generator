#importo le librerie che mi serviranno
import string 
import random
import time
import os

# creo il mio insieme da cui andremo a "pescare" i caratteri che formeranno la nostra password e la password finale vuota
caratteri = string.ascii_letters + string.digits 
password_finale = ""
#do il benvenuto all'utente spiegandogli cosa fa lo script e la lunghezza della sua password
print("Benvenuto, sono password-generator!")
time.sleep(0.30)
print("so che hai bisogno di una nuova password totalmente sicura, sei nel posto giusto")
lunghezza = input("quanti caratteri vuoi che sia lunga la tua password?\n")
lunghezza = int(lunghezza)

# chiediamo all'utente se vuole inserire nella sua password anche dei caratteri speciali
time.sleep(0.30)
print("perfetto!\n vuoi che nella tua password ci siano anche dei caratteri speciali?")

# in base alla risposta ci muoviamo in modo diverso
time.sleep(0.30)
# se l'utente vuole caratteri speciali nella sua password
while True:
    risposta = input("si/no \n").strip().lower()
    if risposta == "si":
        caratteri = caratteri + string.punctuation
        print("perfetto aggiungo i caratteri speciali")
        break
# se l'utente NON vuole caratteri speciali nella sua password
    elif risposta == "no":
        print("ok,ti genero una password senza caratteri speciali")
        break
# se l'utente ha dato una risposta diversa dal si o dal no 
    else:
        print("ERRORE:puoi rispondere con si o con no. riprova!")
    

print("perfetto inizio subito a creare la tua password!")
while len(password_finale)<lunghezza:
    password_finale = password_finale + random.choice(caratteri)
for i in range(3):
    time.sleep(0.30)
    print(".",end='',flush=True)
time.sleep(1)
print("\n perfetto ecco la tua password: \n",password_finale)

# Creiamo un nome per il file
nome_file = "le_mie_password.txt"


# 1. Trova la cartella dell'utente (es: C:\Users\TuoNome)
user_folder = os.path.expanduser("~") 

# 2. Unisce i pezzi in modo sicuro (funziona su Windows, Mac e Linux)
path_file = os.path.join(user_folder, "Desktop", "le_mie_password.txt")

# --- SALVATAGGIO ---
# Ora uso 'path_file' invece del solo nome
with open(path_file, "a") as f:
    f.write(f"Password: {password_finale}\n")


time.sleep(1)
print(f"💾 Salvato con successo sul Desktop: {path_file}")