


from datetime import datetime

def total_days(data_nascimento, data_atual):
    # converte a string da data atual para um objeto data
    data_atual = datetime.strptime(data_atual, "%d/%m/%Y").date()

    # Converter a string de data de nascimento para um objeto data
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y").date()

    # Calcular a diferença em dias entre a data atual e a data de nascimento
    age_in_days = (data_atual - data_nascimento).days

    return age_in_days
if __name__ == '__main__':

    data_atual = input("Digite a data atual (no formato DD/MM/AAAA): ")
    data_nascimento = input("Digite a data de nascimento (no formato DD/MM/AAAA): ")
    age_in_days = total_days(data_nascimento, data_atual)

    print(f"A pessoa viveu aproximadamente {age_in_days} dias.")
