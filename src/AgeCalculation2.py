

if __name__ == '__main__':

    years = input("Digite quantos anos você tem: ")
    months = input("Digite quantos os meses: ")
    days = input("Digite quantos dias: ")

    age_in_days = int(years)*365 + int(months)*30 + int(days)



    print(f"Sua idade em dias é {age_in_days}")