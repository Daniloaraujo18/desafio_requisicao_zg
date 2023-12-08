from urllib.parse import urlparse
from typing import Any, Dict
import requests
def validar_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def make_request(url: str, params: Dict) -> Any:
    response = requests.post(url=url, params=params)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"A requisição falhou com o código de status {response.status_code}")


if __name__ == '__main__':
    url = input("Digite a URL de destino: ")

    # Verificar se a URL é válida
    if validar_url(url):
        name = input("Digite seu nome sem espaços: ")
        email = input("Digite seu email: ")
        cpf = input("Digite seu cpf: ")

        params = {
            'nome': name,
            'email': email,
            'cpf': cpf
        }

        make_request(url, params)
    else:
        print("A URL fornecida é inválida. Certifique-se de fornecer uma URL válida.")