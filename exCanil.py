class Cachorro:
	def _init_(self):
		self.nome = ''
		self.peso = 0
		self.raça = ''
		self.idade = ''

def exibirMenu():
	print('\n ==== == MENU == ====')
	print('0 - SAIR')
	print('1 - CADASTRAR')
	print('2 - LISTAR')
	print('3 - ATUALIZAR')
	print('4 - MAIS VELHO')
	print('5 - EXCLUIR PITBULL')
	print('6 - VIRA-LATAS')
	print('7 - MAIS MAGRO')
	print('8- QUANTIDADE')
	print('9 - ESTOQUE')
	print('==== == ==== == ====')

def cadastrarCachorro(lista):
	novoCachorro = Cachorro()
	nomeCachorro = input('Digite o nome do cachorro: ')
	nomeValido = validarNome(listaCachorros, nomeCachorro)
	if nomeValido == True:
		novoCachorro.nome = nomeCachorro
		novoCachorro.peso = float(input('Digite o peso do cachorro: '))
		novoCachorro.raça = input('Digite a raça do cachorro: ')
		novoCachorro.idade = int(input('Digite a idade do cachorro: '))
		lista.append(novoCachorro)
	else:
		print('DADOS INSETIDOS ESTÃO INCORRETOS')

def validarNome(lista, nome):
	nomeValidado = True
	for i in lista:
		if i.nome == nome:
			nomeValidado = False
	return nomeValidado

def atualizarCachorro(lista):
	nomeAtualizar = input('Digite o nome do cachorro que deseja atualizar: ')
	for i in lista:
		if i.nome == nomeAtualizar:
			i.nome = input('Digite o nome do cachorro: ')
			i.peso = float(input('Digite o peso do cachorro: '))
			i.raça = input('Digite a raça do cachorro: ')
			i.idade = int(input('Digite a idade do cachorro: '))
		else:
			print('Cachorro não encontrado!')

def cachorroVelho(lista):
	velho = 0
	nomeVelho = ''
	for i in lista:
		if i.idade > velho:
			nomeVelho = i.nome
	print('O cachorro mais velho é: {}'.format(nomeVelho))

def excluirPitbull(lista):
	for i in lista:
		if i.raça == 'Pitbull':
			lista.remove(i)

def listar(lista):
	for i in lista:
		print('Nome do cachorro', i.nome)
		print('Peso do cachorro', i.peso)
		print('Raça do cachorro', i.raça)
		print('Idade do cachorro', i.idade)
		print('==== == ==== == ====')

def percentualViraLata(lista):
	qtdd = 0
	total = len(lista)
	for i in lista:
		if i.raça == 'Vira-lata':
			qtdd +=1
	percentual = (qtdd*100)/total
	print('O percentual de cachorros da raça vira-lata é de: {}%'.format(percentual))

def maisMagro(lista):
	magro = float('Inf')
	nomeMagro = ''
	for i in lista:
		if i.peso < magro:
			nomeMagro = i.nome
	print('O cachorro mais magro é', nomeMagro)

def addListaRacas(lista1, lista2):
	raçaValida = True
	for i in lista1:
		for b in lista2:
			if b == i.raça:
				raçaValida = False				
		if raçaValida == True:
			lista2.append(i.raça)

	raça = ''
	for i in lista2:
		cont = 0
		raça = i
		for b in lista1:
			if i == b.raça:
				cont += 1
		print('Existem {} cães da raça {}'.format(cont, raça))

def estoqueRacao(lista):
	quiloCachorro = 0
	for i in lista:
		quiloCachorro += i.peso
	estoque = (quiloCachorro*2)*12
	print('O estoque deve ser de {} quilos para os próximos 12 meses'.format(estoque))


listaRacas = []
listaCachorros = []
opc = -1
while opc != 0:
	exibirMenu()
	opc = int(input('Digite a opção: '))
	if opc == 1:
		cadastrarCachorro(listaCachorros)
	elif opc == 2:
		listar(listaCachorros)
	elif opc == 3:
		atualizarCachorro(listaCachorros)
	elif opc == 4:
		cachorroVelho(listaCachorros)
	elif opc == 5:
		excluirPitbull(listaCachorros)
	elif opc == 6:
		percentualViraLata(listaCachorros)
	elif opc == 7:
		maisMagro(listaCachorros)
	elif opc == 8:
		addListaRacas(listaCachorros, listaRacas)
	elif opc == 9:
		estoqueRacao(listaCachorros)
