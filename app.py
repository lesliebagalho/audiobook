import os
from gtts import gTTS

def create_audiobook(text_file, output_file, lang):
    # Lê o conteúdo do arquivo de texto
    with open(text_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Gera o áudio com o idioma especificado
    tts = gTTS(text=text, lang=lang)
    
    # Salva o arquivo de áudio
    tts.save(output_file)
    print(f"Audiobook salvo em {output_file}")

# Arquivos de texto de entada
text_file_pt = "audiobook_pt.txt"
text_file_en = "audiobook_en.txt"

# Geração do audiobook nos idiomas
output_file = "audiobook_pt.mp3"
create_audiobook(text_file_pt, output_file, lang='pt')

output_file = "audiobook_en.mp3"
create_audiobook(text_file_en, output_file, lang='en')



# os.system(f"start {output_file}")

