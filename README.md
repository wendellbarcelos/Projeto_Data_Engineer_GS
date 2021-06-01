## Projeto Data Engineer - GS :snake: :computer:



odo ano o Stack Overflow faz uma pesquisa com sua comunidade de desenvolvedores sobre vários temas, que vão desde as suas preferências tecnológicas até questões profissionais. Seu desafio é nos ajudar a responder algumas perguntas usando os resultados de uma destas pesquisas.



1. **Popular um banco de dados a partir dos dados crus da pesquisa:**

   Você deve usar Python para ler esse arquivo, processá-lo de acordo com as regras de negócio descritas abaixo e depois inserir esses dados em um banco de dados PostgreSQL.

   **Regras de negócio:**

   1. Salário vazio ou com valor "NA" deve ser convertido para zero (0.0).
   2. Salário deve ser sempre calculado em reais e mensal. Para esse cálculo você usará a coluna ConvertedSalary, que contém o salário anual. Considere que 1 dólar equivale a R$5,6. 
   3. O nome dos respondentes deve seguir a regra respondente_[número] . (ex: respondente_1, respondente_2, respondente_3). O critério de geração desse número é todo seu.
   4. Cada linha da tabela linguagem_programacao deve conter uma única linguagem de programação.
   5. Cada linha da tabela ferramenta_comunic deve conter apenas uma ferramenta de comunicação.
   6. É importante notar que em alguns campos de respostas existem múltiplos resultados, como por exemplo na coluna LanguageWorkedWith, que contém várias linguagens de programação em uma linha. Nestes casos, você deve quebrar a string nos pontos que existem ponto-e-vírgula (";").

   **Como resultado desta etapa deve ser entregue um arquivo chamado “carga.py”.**

2. **Realizar consultas no banco de dados para responder as perguntas**:

   1. Qual a quantidade de respondentes de cada país?
   2. Quantos usuários que moram em "United States" gostam de Windows?
   3. Qual a média de salário dos usuários que moram em Israel e gostam de Linux?
   4. Qual a média e o desvio padrão do salário dos usuários que usam Slack para cada tamanho de empresa disponível?

   **Como resultado desta etapa deve ser entregue um Jupyter Notebook com as respostas.**