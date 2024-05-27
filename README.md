## Análise de Dados do IBGE 

Este repositório contém um conjunto de scripts Python para automatizar a coleta, tratamento e análise de dados sobre acesso à internet e posse de celular no Brasil, publicados pelo IBGE.

### Pré-requisitos

* **Python 3.x**
* **Bibliotecas Python:** 
Instale as dependências necessárias usando o comando:
   ```bash
   pip install -r requirements.txt
   ```
   Os pacotes principais são:
    * **selenium:** Para automatizar a navegação no site do IBGE e baixar os arquivos.
    * **pandas:** Para manipular e analisar os dados em DataFrames.
    * **webdriver_manager:** Para gerenciar os drivers do navegador Chrome.
    * **openpyxl:** Para ler e escrever arquivos Excel.

### Como executar

1. **Baixe o repositório:** Faça o download do repositório Git ou clone-o usando:
   ```bash
   git clone https://github.com/seu-usuario/analise-dados-ibge.git
   ```

2. **Ajuste os caminhos dos arquivos:** No arquivo `main.py`, edite os seguintes caminhos:
   * `diretorio_entrada`: Caminho para a pasta onde os arquivos XLSX serão baixados.
   * `diretorio_saida`: Caminho para a pasta onde os arquivos CSV serão salvos.
   # Troque também as funções: 
   * `diretorio_entrada`: Edite no arquivo `extracao_dados.py ` é equivalente ao `diretorio_entrada`
   * `diretorio`: Edite no arquivo `tratamento_dados.py ` é equivalente ao `diretorio_entrada`
   * `input_dir`: Edite no arquivo `converter_arquivos.py ` é equivalente ao `diretorio_entrada`
   * `output_dir`: Edite no arquivo `converter_arquivos.py ` é equivalente ao `diretorio_saida`
   * `diretorio_dados`: Edite no arquivo `visualizar_dados.py ` é equivalente ao `diretorio_saida`


3. **Execute o script principal:**
   ```bash
   python main.py
   ```

   O script irá:
   * **Extrair os dados:** Acessar o site do IBGE, baixar os arquivos XLSX e salvá-los na pasta `diretorio_entrada`.
   ## IMPORTANTE ##: 
   * **Tratar os dados:** Limpar os arquivos XLSX, removendo linhas e colunas desnecessárias, corrigindo erros de formatação e salvando as versões limpas.
   * **Converter para CSV:** Converter os arquivos XLSX limpos para CSV e salvá-los na pasta `diretorio_saida`.
   * **Analisar os dados:** Realizar uma análise exploratória dos dados CSV e gerar um arquivo Excel (`analise_exploratoria.xlsx`) com os resultados.

### Funcionalidades

* **Automatizar o download de dados:** O script automatiza a navegação no site do IBGE e o download dos arquivos XLSX desejados.
* **Limpar e tratar os dados:** O script realiza a limpeza e tratamento dos dados, incluindo:
    * Remover linhas e colunas irrelevantes.
    * Corrigir erros de formatação.
    * Substituir caracteres especiais e normalizar o encoding.
* **Converter para CSV:** Converter os arquivos XLSX limpos para CSV para facilitar o processamento.
* **Análise exploratória:** Realizar uma análise exploratória dos dados, incluindo:
    * Mostrar as tabelas com os dados de acesso à internet por região.
    * Mostrar as tabelas com os dados de posse de celular por região.
    * Mostrar as tabelas com os dados de acesso à internet por celular ou tablet.

### Informações adicionais

* O script está configurado para baixar os dados da pesquisa "Acesso à internet e posse de celular" de 2015.
* inicialmente era pra ele fazer scroll down automaticamente até achar os botões em que precisa clicar, mas nao foi possivel até o momento configurar por completo essa função por isso **É NECESSÁRIO QUANDO INICIAR O CHROME** `fazer scrolldown manualmente até os botões aparecerem na pagina do IBGE`

* Você pode modificar o script para baixar dados de outras pesquisas, ajustando os XPaths dos elementos do site do IBGE.
* Para realizar análises mais avançadas, você pode utilizar as bibliotecas de visualização de dados como Matplotlib e Seaborn.
* Havia configurado um arquivo config.py apenas importar e rodar os **diretorio_saida** e **diretorio_entrada**, porem o codigo nao interpretou isso muito bem e removi para as configurações que estavam antes por falta de tempo habil para poder unificar tudo nesse momento

### CASO O MAIN NÃO FUNCIONE DE PRIMEIRA:
   * RODAR POR PRIMEIRO ARQUIVO SECUNDÁRIO planoB.py seguir as mesmas instruções que para o arquivo extracao_dados.py
   * CLICAR PARA RODAR O **MAIN** NOVAMENTE

### Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema, tiver sugestões de melhoria ou quiser adicionar novas funcionalidades, abra um pull request.

---