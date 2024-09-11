# Função para coletar informações sobre o pet
def coletar_informacoes_pet():
    print("Por favor, insira as informações sobre seu pet.")

    # Coleta do nome do pet
    nome = input("Nome do pet: ")

    # Coleta da idade do pet, garantindo que seja um número inteiro
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    # Coleta do peso do pet, garantindo que seja um número flutuante
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")
    
    # Exibindo as informações coletadas 
    # pela funcao mostrar_informacoes_pet
    petdata = [nome,idade,peso]
    mostrar_informacoes_pet(petdata)
    

    # Retornando as informacoes dos pets para serem armazenadas
    return [nome,idade,peso]


# Funcao para mostrar as informacoes do pet sem coleta-las
def mostrar_informacoes_pet(petdata):
    # Exibindo as informações do pet
    print("\nInformações do pet:")
    print(f"Nome: {petdata[0]}")
    print(f"Idade: {petdata[1]} anos")
    print(f"Peso: {petdata[2]} kg")
    




# Criando array para guardar informacoes dos pets 
Pets = []

# Chama a função para coletar e exibir as informações do pet
Pets.append(coletar_informacoes_pet())
