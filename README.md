# analytics-rouanet-censo-jus
Desafio de Pipeline de Operações.
Os objetivos do pipeline são:

    - unificar os datasets rouanet.csv e censo_estado.csv atraves das colunas estado_ibge e código, respectivamente;
    - criar uma Natural Key para esse dado, usando as colunas estado_ibge e valor_em_reais;
    - remover as linhas duplicadas de acordo com a surrogate key;
    - remover linhas com valor_em_reais = 0 ou quantidade = 0;
    - trocar os dados da coluna estado para a sigla da UF correspondente, ex.: Rio de Janeiro vira RJ.

Para criação deste pipeline utilizamos o python 3.11 junto a biblioteca Pandas, levando como inspiração a manipulação de dados em Banco. O código foi desenvolvido com Pandas levando em consideração a facilidade  de possíveis manutenções, alterações na fonte de dados e possibilidade de expansão do pipeline. Além do Pandas, o microframework Flask foi utilizado para a criação de um endpoint para chamar sua execução.

### Como Executar o Projeto

O projeto foi desenvolvido em python e a biblioteca Pandas, muito usada para a manipulação e análise de dados. O pipeline foi desenvolvido em ambiente Conda, mas uma virtual env também é uma opção. Escolha um destes ambientes e siga os passos abaixo:
 
 1 - Primeiro, instale os módulos necessários (Para evitar conflitos entre módulos, é preferível que tais comandos sejam executando em um ambiente virtual, como venv ou conda):

        --pip install -r requirements.txt--

 2 - renomeie o arquivo ".env copy" para .env.
 
 3 - Após instalação, acesse o diretório onde está a aplicação Web com o comando:
        
        python main.py

 4 - Feito! Agora navegue até a página respondida pela aplicação.

### Navegação

A url __ é o index da aplicação, para acessar o endpoint, utiliza-se o endpoint abaixo:

    http://127.0.0.1:5000/generate_report

### Docker

Também é possível rodar a aplicação com o Docker, executando no terminal:

    docker build -t relatorio-censo-rouanet .

Para confirmar se a sua imagem foi criada:
    docker image ls

Após a criação da imagem, é possível rodar e seguir os pasos de navegação.
