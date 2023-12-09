def obter_idade():
    entrada_idade = input("Digite a idade no formato 'anos, meses, dias': ")

    try:
        anos, meses, dias = map(int, entrada_idade.split(','))

        # Verifica se os valores são positivos
        if anos >= 0 and meses >= 0 and dias >= 0:
            idade = (anos, meses, dias)
            return idade
        else:
            print("Por favor, digite valores positivos para anos, meses e dias.")
    except ValueError:
        print("Por favor, digite valores numéricos válidos para anos, meses e dias.")



if __name__ == '__main__':

    age_pessoa = obter_idade()
    print(f"Idade: {age_pessoa[0]} anos, {age_pessoa[1]} meses, {age_pessoa[2]} dias")

    age_in_days = age_pessoa[0]*365 + age_pessoa[1]*30 + age_pessoa[2]

    print(f"Sua idade em dias é {age_in_days}")