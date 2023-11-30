# Tabela de Produtos

# Apresentação

print('\n\t\t\t\t ----- Sistema de Cadastro Simples ------\n')


# Entrada c/ Processamento

# Dicionario = P

p = {'Produto': '', 'Preço': 0.0, 'Quantidade': 0, 'Disponivel' : False}

# P = Produto
p['Produto'] = str(input('Digite o nome do Produto: '))
p['Preço'] = float(input('Qual o preço do Produto R$:  '))
p['Quantidade'] = int(input('Quantidade de Produto: '))
p['Disponivel'] = True

if p['Quantidade'] >= 1:
    print('Produto Disponivel!')
else:
    print('Produto indisponivel')

print('\n\t\t\t --- Informações do Produto abaixo: ---\n')

# Saída

print(f'Produto: {p["Produto"]}')
print(f'Preço: {p['Preço']}')
print(f'Quantidade: {p["Quantidade"]}')
print(f'Disponivel: {p["Disponivel"]}')

print(f'Preço Total: {p['Preço'] * p['Quantidade']}')