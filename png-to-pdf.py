import os
from PIL import Image

# Caminho da pasta contendo os arquivos PNG
pasta_imagens = 'C:'
# Nome do arquivo PDF de saída (salvo na mesma pasta das imagens)
pdf_saida = os.path.join(pasta_imagens, 'saida.pdf')

# Lista para armazenar as imagens abertas
imagens = []

# Percorre todos os arquivos na pasta
for arquivo in os.listdir(pasta_imagens):
    if arquivo.endswith('.png'):
        caminho_imagem = os.path.join(pasta_imagens, arquivo)
        img = Image.open(caminho_imagem).convert('RGB')  # Converte para RGB
        imagens.append(img)

# Verifica se há imagens para combinar
if imagens:
    # Salva o primeiro arquivo como PDF e adiciona os outros
    imagens[0].save(pdf_saida, save_all=True, append_images=imagens[1:])
    print(f'{pdf_saida} criado com sucesso!')
else:
    print('Nenhum arquivo PNG encontrado.')