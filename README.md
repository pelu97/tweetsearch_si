
# Tweet Search SI
Buscador de Tweets para Previsão de Crises de Saúde - Sistemas de Informação


## Explicacao de uso:

A aplicação possui dois módulos, o buscador e a interface:

### -- INTERFACE:
Para abrir a interface, deve-se abrir um terminal na pasta raiz/tweetsearch_site e executar o comando:   
		
		python3 manage.py runserver IP:PORTA  
OU  
		
		python3 manage.py runserver  
	
(caso os campos sejam deixados em branco, como o comando acima, a interface ficará na página *127.0.0.1:8000*)
onde IP pode ser deixado em branco (acessar apenas como local *127.0.0.1*) ou *0.0.0.0* (acessar como o ip da máquina na rede lan) 
	
	python3 manage.py runserver PORTA 
OU  
	
	python3 manage.py runserver 0PORTA

onde PORTA deve ser substituído por um número não utilizado no momento, como *7000* por exemplo:  
	   
	   python3 manage.py runserver 7000
OU

	   python3 manage.py runserver 0.0.0.0:7000
	
A interface estará no ip local *127.0.0.1:PORTA* OU *IP DA MÁQUINA:PORTA*
	Para acessar deve ser inserido o link *IP:PORTA/map*
	(Para facilidade, vamos resumir que "/alguma_pagina" significa que esse /alguma_pagina deve ser colocado ao lado do endereço)
	É dentro do /map que a interface reside.
	-Para visualizar uma busca:
	  Deve-se acessar /map e digitar os parâmetros:
	 	-Data início do filtro
	 	-Data final do filtro
	 	-Estado ou município (funcionalidade não existente no momento)
	 	-Palavra chave da busca a ser visualizada
	 
**ATENÇÃO!**

**- Se a palavra chave não tiver sido pesquisada, ocorrerá um erro! Deve existir uma busca por essa palavra chave para conseguir mostrar a mesma**

**- Se a busca escolhida nao tiver dados para a data escolhida , ocorrerá um erro. deve-se apenas alterar a data para um que contenha dados na busca da palavra chave**

-Para configurar a busca:
	  Deve-se acessar /map/key e digitar o parâmetro:
	  	-Palavra chave da busca
		(Uma palavra chave que o buscador irá procurar)
	  Após configurar, a busca deve ser rodada (Veja o passo do buscador)

### -- BUSCADOR:
A busca deverá ser executada manualmente. Para isso, abra um terminal na pasta raiz/tweetsearch_site/map e digite o seguinte comando:
		
		python3 busca.py
		
A busca será executada pela palavra chave que foi configurada na interface (Veja o passo de configurar a palavra chave na interface)
