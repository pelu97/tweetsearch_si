# Tweet Search SI
Buscador de Tweets para Previsão de Crises de Saúde - Sistemas de Informação


#Explicacao de uso:

-Todo o programa funciona de acordo com o diretório raiz onde está a função main.py
-A função main.py não possui uso, possui apenas exemplos de como usar todas as bibliotecas do projeto.

para usar, favor faça as alterações necessárias nos paths de leitura do bib_backend.filtrador, para acessar os dados na pasta dados. 
Do buscador.buscador para acessar os dados de twts. Ex: 'seuPath/dados/twts.json'.

-Importando: (siga a ordem exata)
	-import seuPath.buscador 
	-from seuPath.bib_backend import analisadorSentimentos
	-from seuPath.bib_backend import filtrador

-Uso: 

	-Para receber o dataFrame com o sentimento e contagem de twts por estado, geolocalizados, faça:

		transformador.geraSentimentosEstados(df = data_frame_de_twts_filtrado_a_seu_gosto)
	
	-Para ativar o buscador com uma palavra chave sendo o nome de uma doença faça:

		buscaTwts.iniciaBusca(key = palavraChave, time = 10) #obs: time é um parâmetro fantasma, colocado na arquitetura para futuramente 
									gerenciar o tempo que o buscador vai funcionar. (logo pode ser qualquer coisa
									no momento).

obs: Até o momento não foi implementado tratamento de erros nas funções, portanto deve-se passar exatamente os parâmetros que elas esperam. Caso
contrário a aplicação irá retornar resultados imprevisíveis. 	
