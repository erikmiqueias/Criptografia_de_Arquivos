import os
from cryptography.fernet import Fernet

PATH = "/home/erik_miqueias/Criptografia_de_Arquivos/texts"
arquivos = []
chave = Fernet.generate_key()

with open("chave.key", "rb") as arquivo:
    chave = arquivo.read()

for arquivo in os.listdir(PATH):
    arquivos.append(os.path.join(PATH, arquivo))

for arq in arquivos:
    with open(arq, "rb") as arquivo:
        conteudo = arquivo.read()
        
    conteudo_descriptografado = Fernet(chave).decrypt(conteudo)
    
    with open(arq, "wb") as arquivo:
        arquivo.write(conteudo_descriptografado) 
    
        
