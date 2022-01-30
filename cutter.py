import os
from pydub import AudioSegment
from tokenize import String

AudioSegment.converter = r'C:\\ffmpeg-5.0-full_build\\bin\\ffmpeg.exe'
AudioSegment.ffmpeg = r'C:\\ffmpeg-5.0-full_build\\bin\\ffmpeg.exe'
AudioSegment.ffprobe = r'C:\\ffmpeg-5.0-full_build\\bin\\ffprobe.exe'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
    

pasta = input("Cole o diretorio das musicas aqui : ")
tamanho = input("Digite o tamanho desejado das musicas em segundos: ")
inicio = input("Digite o tempo inicial das musicas (Digite 0 para começar do inicio): ")
new_folder = f"{pasta}\\Musicas_{tamanho}s"
createFolder(new_folder)
arq = ""
for arquivo in os.listdir(pasta):
    if os.path.isfile(os.path.join(pasta, arquivo)):
        arq = pasta + "\\" + arquivo
        if arq.endswith(".mp3") or arq.endswith(".MP3"):
            print(f"Convertendo {arquivo}, Aguarde...")
            sound_file = AudioSegment.from_mp3(arq)
            new_file = sound_file[int(inicio)*1000:(int(inicio) + int(tamanho))*1000]
            new_file.export(new_folder+"\\"+arquivo[:-4]+" ("+tamanho+"s)"+".mp3", format="mp3")
        else:
            print(f"{arquivo} nao é uma musica!")
print(f"Todas as musicas foram convertidas em: {new_folder}")
print("Finalizado!")