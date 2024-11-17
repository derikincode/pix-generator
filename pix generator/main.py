import os
from PIL import Image, ImageDraw, ImageFont

def adicionar_numeros_e_linhas_na_arte(limite):
    imagem_fundo = Image.open("./img/banner.png")
    
    x_inicial, y_inicial = 110, 700 
    espaco_x, espaco_y = 90, 100  
    largura = 10 

    numero_atual = 1

    while numero_atual <= limite:
        imagem_fundo_atual = imagem_fundo.copy()
        draw = ImageDraw.Draw(imagem_fundo_atual)
        
        x_atual, y_atual = x_inicial, y_inicial

        for i in range(50):
            if numero_atual > limite:
                break 
            
            if numero_atual < 1000:
                font = ImageFont.truetype("arial.ttf", 40)
                offset_x = 15
            else:
                font = ImageFont.truetype("arial.ttf", 35)
                offset_x = 5

            draw.rectangle([x_atual, y_atual, x_atual + espaco_x, y_atual + espaco_y], fill="white")
            
            draw.text((x_atual + offset_x, y_atual + 20), f"{numero_atual:02}", font=font, fill="black")
            
            if ((i + 1) % largura) != 0:
                draw.line([(x_atual + espaco_x, y_atual), (x_atual + espaco_x, y_atual + espaco_y)], fill="black", width=3)
            
            x_atual += espaco_x
            
            if ((i + 1) % largura) == 0:
                draw.line([(x_inicial, y_atual + espaco_y), (x_inicial + largura * espaco_x, y_atual + espaco_y)], fill="black", width=3)
                x_atual = x_inicial
                y_atual += espaco_y

            numero_atual += 1

        draw.line([(x_inicial, y_inicial), (x_inicial + largura * espaco_x, y_inicial)], fill="black", width=3)
        draw.line([(x_inicial, y_inicial), (x_inicial, y_inicial + 5 * espaco_y)], fill="black", width=3)
        draw.line([(x_inicial + largura * espaco_x, y_inicial), (x_inicial + largura * espaco_x, y_inicial + 5 * espaco_y)], fill="black", width=3)

        numero_imagem = 1
        while os.path.exists(f"pix_premiado_{numero_imagem}.png"):
            numero_imagem += 1

        nome_arquivo = f"pix_premiado_{numero_imagem}.png"

        imagem_fundo_atual.save(nome_arquivo)
        print(f"Imagem salva como {nome_arquivo}")

adicionar_numeros_e_linhas_na_arte(1000)