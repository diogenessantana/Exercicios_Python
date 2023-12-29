clientes = []
saldos = []
titulo = "RELAÇÃO DE CLIENTES - BANCO NACIONAL"

for contador in range(1, 6):
    nome = input("Digite o nome: ")
    clientes.append(nome)
    saldo = float(input("Digite o valor em R$: "))
    saldos.append(saldo)

print("\n{}".format(titulo))
print("=" * len(titulo))

for i in range(0, len(clientes)):
    print("{:>10} {:>20,.2f}".format(clientes[i], saldos[i]))