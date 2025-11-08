meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "BLING":"una referencia a joyas",
            "SHEESH": "ligera desaprobación",
            "CREEPY": "aterrador, siniestro",
            "ROFL": "una respuesta a una broma"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict.keys():
    print("aqui tienes la palabra",meme_dict[word])
else:
    print("la palabra esta en progreso")
