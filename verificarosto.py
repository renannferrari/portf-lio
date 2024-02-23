import face_recognition

def carregar_codificar_imagem(file):
    imagem = face_recognition.load_image_file(file)
    encoding = face_recognition.face_encodings(imagem)[0]
    return encoding

imagem1 = carregar_codificar_imagem("C:/Users/user/Desktop/estudos/python/imagem1.jpeg")
imagem2 = carregar_codificar_imagem("C:/Users/user/Desktop/estudos/python/imagem2.jpeg")

imagens_conhecidas = [imagem1, imagem2]
rotulos_conhecidos = ["Você", "Você"]  

def verificar_imagem(imagem_desconhecida):
    
    encoding_desconhecido = carregar_codificar_imagem(imagem_desconhecida)
    
    
    for imagem_conhecida, rotulo in zip(imagens_conhecidas, rotulos_conhecidos):
        resultado = face_recognition.compare_faces([imagem_conhecida], encoding_desconhecido)
        if resultado[0]:
            print(f"A imagem fornecida corresponde a {rotulo}.")
            return
    print("A imagem fornecida não corresponde a nenhuma imagem conhecida.")

# imagem que vai ser comparada
verificar_imagem("C:/Users/user/Desktop/estudos/python/imagem3.jpeg")
