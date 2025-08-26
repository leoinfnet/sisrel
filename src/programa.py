import random
from datetime import datetime, timedelta


class Venda:
    def __init__(self, produto, valor, data):
        self.produto = produto
        self.valor = valor
        self.data = data

    def __str__(self):
        return f"{self.produto} - R${self.valor:.2f} em {self.data.strftime('%d/%m/%Y')}"
def header():
    print("=" *40)
    print(" Seja bem vindo ao SISREL".center(50))
    print("="*40)

def gerar_vendas(qtd):
    produtos = ['Camiseta', 'Calça', 'Tênis', 'Boné']
    vendas = []
    for _ in range(qtd):
        produto = random.choice(produtos)
        valor = random.uniform(50, 500)
        dias_atras = random.randint(1, 30)
        data = datetime.now() - timedelta(days=dias_atras)
        vendas.append(Venda(produto, valor, data))
    return vendas

def calcular_media(vendas):
    total = sum(v.valor for v in vendas)
    return total / len(vendas)

def filtrar_por_produto(vendas, nome_produto):
    return [v for v in vendas if v.produto == nome_produto]

def relatorio(vendas):
    print("Relatório de Vendas diárias:\n")
    for v in vendas:
        print(v)
    print("\nMédia das vendas: R$", round(calcular_media(vendas), 2))

def main():
    header()
    vendas = gerar_vendas(10)
    vendas_tenis = filtrar_por_produto(vendas, 'Tênis')
    print("Vendas de Tênis:")
    for v in vendas_tenis:
        print(v)
    print("Análise geral:")
    print("aqui eh um bug escondido")  
    relatorio(vendas)
    print("-"*50)
    print("Programa finalizado")
    print("-"*50)
    print("Tenha um bom dia!")
    print()

if __name__ == '__main__':
    main()