import os
import pygame
from elevenlabs.client import ElevenLabs

API_KEY = "2972f725a0f62d90a99b727f17f6939ca4e775f52a7e2b592c723eb30d4b35cd"
VOICE_ID = "pNInz6obpgDQGcFmaJgB"  # Adam
MODEL_ID = "eleven_multilingual_v2"
FORMATO = "mp3_44100_128"

client = ElevenLabs(api_key=API_KEY)

def falar(texto, salvar=True, reproduzir=True):
    """
    Gera áudio com ElevenLabs e opcionalmente reproduz.
    
    Args:
        texto: Texto a ser falado
        salvar: Se True, salva em E:\IA\audio\falas\
        reproduzir: Se True, reproduz o áudio
    """
    texto_limpo = texto[:50].replace(" ", "_").replace("\n", "_")
    nome_arquivo = f"E:\\IA\\audio\\falas\\{texto_limpo}.mp3"
    
    print(f"Gerando áudio: {texto}")
    
    audio_stream = client.text_to_speech.convert(
        text=texto,
        voice_id=VOICE_ID,
        model_id=MODEL_ID,
        output_format=FORMATO
    )
    
    with open(nome_arquivo, "wb") as f:
        for chunk in audio_stream:
            if chunk:
                f.write(chunk)
    
    print(f"Áudio salvo: {nome_arquivo}")
    
    if reproduzir:
        pygame.mixer.init()
        pygame.mixer.music.load(nome_arquivo)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        pygame.mixer.quit()
    
    return nome_arquivo

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        texto = " ".join(sys.argv[1:])
        falar(texto)
    else:
        print("Uso: python template.py \"texto para falar\"")