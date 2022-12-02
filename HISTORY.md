### Introdução

    Olá! Esse History é para descrever o desenvolvimento deste pipeline. O objetivo deste desenvolvimento é criar um pipeline de operações que gere um csv no final. O passo a passo do pipeline:

    - unificar os datasets rouanet.csv e censo_estado.csv atraves das colunas estado_ibge e código, respectivamente;
    - criar uma Natural Key para esse dado, usando as colunas estado_ibge e valor_em_reais;
    - remover as linhas duplicadas de acordo com a surrogate key;
    - remover linhas com valor_em_reais = 0 ou quantidade = 0;
    - trocar os dados da coluna estado para a sigla da UF correspondente, ex.: Rio de Janeiro vira RJ.

    Antes de começar a desenvolver o projeto tive dúvida em qual abordagem trazer ao meu código, se seria algo mais "manual" ou se deveria utilizar uma biblioteca para automatizar mais os processos. Optei por usar uma biblioteca para que os processos não fossem longos e confusos com vários laços e condições, assim como para facilitar o entendimento e manutenção se necessário. Portanto, para criação deste pipeline foi utilizado o python 3.11 junto a biblioteca Pandas, levando como inspiração a manipulação de dados em Banco. O código foi desenvolvido com Pandas levando em consideração a facilidade  de possíveis manutenções, alterações na fonte de dados e possibilidade de expansão do pipeline. Para "chamar" o script, foi utilizado o Flask. 

### Ferramentas utilizadas

    Python 3.11 - linguagem de programação mais popular quando se trata de ciência de dados;
    Flask - Framework para criação de endpoint;
    Pandas - biblioteca para manipulação dos dados. Como o passo a passo deste pipeline assemelha-se a manipulação de dados em Banco, quis trazer essa biblioteca pela simplicidade, facilidade de possíveis manutenções por alteração na fonte de dados e expansão do mesmo.
    Dockerfile - build imagem. 

    Durante a contrução usei o Conda como ambiente, mas uma virtual env também é uma opção.

### Estrutura da aplicação

    Os diretorios foram dividos da seguinte forma:
    - pasta > datasets = os arquivos .csv usados como input;
    - pasta > services > utils > util.py = Classe Util e funções/métodos:
                                            - drop_values(df) = recebe o dataframe e remove linhas dos campos especificados caso sejam iguais a 0.
                                            - surrogate(df) = cria a coluna "sk_order" como a surrogate key do dataframe.
                                            - drop_duplicates_report(df) = remove linhas duplicadas/iguais.
                                            - dict_uf(df) = dicionário para transformar as linhas do campo "estado" para suas respectivas siglas.
    - pasta > services > censoService.py = recebe os métodos do arquivo util para tratamento dos dataframes criados ao coletar os arquivos csv e retorna um único arquivo .csv. Por ser uma chave "viva", a surrogate key foi adicionada nos últimos passos do pipeline.
    - Dockerfile = criado para o setup do ambiente em outras máquinas.
    - main.py = recebe o serviço criado e cria um endpoint para dar vazão ao mesmo. 
    - requirements.txt = lista de bibliotecas que precisam ser instaladas para funcionamento da stack.
    - .env = armazena algumas variáveis de acesso. Como é recomendável estar em gitignore, foi feita uma cópia renomeada para ser commitada.
    
    Foi incluido um .gitignore para ignorar os arquivos usados nos testes.

### Testes realizados
    Durante todo o desenvolvimento, o passo serviço foi testado dentro de arquivos.py para aferir o retorno dos mesmos. Para garantir que funcionaria em outra máquina, o dockerfile da stack logo foi criado para executar os testes. 
