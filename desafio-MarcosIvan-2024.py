class Zoo: #definindo a classe Zoo como a estrutura de cada recinto do zoologico
    def __init__(self, num, bioma1, bioma2, tamanho, qtde, animal):
        self.num = num #num = numero do recinto
        self.bioma1 = bioma1 #bioma1 = bioma 1 do recinto
        self.bioma2 = bioma2 #bioma2 = bioma 2 do recinto
        self.tamanho = tamanho #tamanho = tamanho máximo do recinto
        self.qtde = qtde #qtde = capacidade atual
        self.animal = animal #animal = quais animais estão no recinto

class Animais: #definindo a classe Animais como a estrutura de cada animal que pode ser alocado ao zoologico
    def __init__(self, esp, tamanho, bioma1, bioma2):
        self.esp = esp #esp = especie do animal
        self.tamanho = tamanho #tamanho = tamanho que o animal ocupa
        self.bioma1 = bioma1 #bioma1 = bioma 1 em que vive
        self.bioma2 = bioma2 #bioma2 = bioma 1 em que vive   

def verifica(animal, quantidade, atual):
    viavel = 1
    recinto_viavel = []
    for i in range(len(atual)):
        viavel = 1
        for j in range(len(animais)):
            if animais[j].esp == animal:
                break
        if (atual[i].bioma1 != animais[j].bioma1 and atual[i].bioma1 != animais[j].bioma2 and atual[i].bioma2 != animais[j].bioma1 and atual[i].bioma2 != animais[j].bioma2) and atual[i].qtde != 0:
            #1) Um animal se sente confortável se está num bioma adequado
            viavel = 0
        if (atual[i].tamanho-atual[i].qtde < quantidade*animais[j].tamanho) and atual[i].qtde != 0:
            #1) Um animal se sente confortável se está com espaço suficiente para cada indivíduo
            viavel = 0
        if (animal != atual[i].animal and (animal in carnivoro or atual[i].animal in carnivoro)) and atual[i].qtde != 0:
            #2) Animais carnívoros devem habitar somente com a própria espécie e 3) Animais já presentes no recinto devem continuar confortáveis com a inclusão do(s) novo(s)
            viavel = 0
        if animal == 'hipopotamo' and (atual[i].bioma1 != "savana" or atual[i].bioma2 != "rio") and atual[i].qtde != 0:
            #4) Hipopótamo(s) só tolera(m) outras espécies estando num recinto com savana e rio
            viavel = 0
        if animal == 'macaco' and quantidade == 1 and atual[i].qtde != 0:
            #5) Um macaco não se sente confortável sem outro animal no recinto, seja da mesma ou outra espécie
            viavel = 0
        if viavel == 1:
            recinto_viavel.append([atual[i].num, atual[i].qtde + (quantidade * animais[j].tamanho), atual[i].tamanho])
    if len(recinto_viavel)==0:
        print("Não há recinto viável")
    else:
        for i in range(len(recinto_viavel)):
            print(f"Recinto {recinto_viavel[i][0]} (espaco livre: {recinto_viavel[i][1]} total: {recinto_viavel[i][2]})")




atual = [] #inicializando o estado atual do zoologico para cada um dos recintos
atual.append(Zoo(1, "savana", "", 10, 3, "macaco"))
atual.append(Zoo(2, "floresta", "", 5, 0, ""))
atual.append(Zoo(3, "savana", "rio", 7, 1, "gazela"))
atual.append(Zoo(4, "rio", "", 8, 0, ""))
atual.append(Zoo(5, "savana", "", 9, 1, "leao"))

animais = [] #inicializando os animais existentes com o tamanho que ocupa e os biomas em que vivem
animais.append(Animais("leao", 3, "savana", ""))
animais.append(Animais("leopardo", 2, "savana", ""))
animais.append(Animais("crocodilo", 3, "rio", ""))
animais.append(Animais("macaco", 1, "savana", "floresta"))
animais.append(Animais("gazela", 2, "savana", ""))
animais.append(Animais("hipopotamo", 4, "savana", "rio"))

carnivoro = ["leao", "leopardo", "crocodilo"] #animais que só podem habitar com a propria especie

animal = input("Digite o animal a ser inserido no zoologico: ")
quantidade = int(input("Digite a quantidade de animais: "))

aux_animais = []
for i in range(len(animais)):
    aux_animais.append(animais[i].esp)

if animal not in aux_animais:
    print(aux_animais)
elif quantidade <= 0:
    print("Quantidade invalida")
else:
    verifica(animal, quantidade, atual)