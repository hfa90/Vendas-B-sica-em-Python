class Cliente:
    def __init__(self, nome):
        self.nome = nome

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Sistema:
    def __init__(self):
        self.clientes = []
        self.produtos = []
        self.vendas = []

    def cadastrar_cliente(self, nome_cliente):
        cliente = Cliente(nome_cliente)
        self.clientes.append(cliente)

    def cadastrar_produto(self, nome_produto, preco):
        produto = Produto(nome_produto, preco)
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\n=== LISTA DE PRODUTOS ===")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. Produto: {produto.nome} - Preço: R${produto.preco:.2f}")

    def listar_clientes(self):
        print("\n=== LISTA DE CLIENTES ===")
        for i, cliente in enumerate(self.clientes, 1):
            print(f"{i}. Nome do Cliente: {cliente.nome}")

    def realizar_venda(self, cliente_index, produto_index):
        cliente = self.clientes[cliente_index - 1]
        produto = self.produtos[produto_index - 1]
        self.vendas.append((cliente, produto))
        print("Venda Realizada com sucesso!")

    def relatorio_ultima_venda(self):
        if self.vendas:
            cliente, produto = self.vendas[-1]
            print("\n=== ÚLTIMA VENDA ===")
            print(f"Cliente: {cliente.nome}")
            print(f"Produto: {produto.nome} - Preço: R${produto.preco:.2f}")
        else:
            print("Nenhuma venda realizada ainda.")


# Função principal para interação com o usuário
def main():
    sistema = Sistema()

    while True:
        print("\n=== MENU ===")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Produto")
        print("3. Listar Produtos")
        print("4. Listar Clientes")
        print("5. Realizar Venda")
        print("6. Relatório Última Venda")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome_cliente = input("Digite o nome do cliente: ")
            sistema.cadastrar_cliente(nome_cliente)
            print("Cliente cadastrado com sucesso!")
        elif opcao == '2':
            nome_produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o preço do produto: "))
            sistema.cadastrar_produto(nome_produto, preco)
            print("Produto cadastrado com sucesso!")
        elif opcao == '3':
            sistema.listar_produtos()
        elif opcao == '4':
            sistema.listar_clientes()
        elif opcao == '5':
            sistema.listar_clientes()
            cliente_index = int(input("Selecione o cliente (digite o número correspondente): "))
            sistema.listar_produtos()
            produto_index = int(input("Selecione o produto (digite o número correspondente): "))
            sistema.realizar_venda(cliente_index, produto_index)
        elif opcao == '6':
            sistema.relatorio_ultima_venda()
        elif opcao == '7':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
