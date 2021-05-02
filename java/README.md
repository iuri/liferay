# RECEBER DOCUMENTAÇÃO DO USUÁRIO
___
### RESUMO
+ **Visão geral técnica**
+ **Visão geral do desafio**
+ **Instruções de instalação e uso**
+ **Opções de teste**
+ **Premissas**
   1. _Entrada de arquivo_
   2. _Transcodificação_
   3. _Objetos e Classes_
   4. _Outro_
+ **Casos de Uso**
   1. _Como cliente / usuário_
   2. _Como desenvolvedor_
+ **Notas, pensamentos e feedback sobre o desafio**

### VISÃO GERAL TÉCNICA
  | 
--- | 
Linguagem: ***Java*** |
Unidade de teste: ***jUnit*** |
Versão: ***v1.1.2*** |
Arquivos de entrada: ***arquivos .txt de entrada*** |

### VISÃO GERAL DO DESAFIO
  |
--- |
Empresa Solicitante: ***Liferay*** |
Candidatura a Cargo: ***Programa de Consultor Associado - Brasil*** |
Desafio: ***2 Impostos sobre vendas (consulte o README para obter os requisitos do desafio)*** | 
Data: ***1 de maio de 2021*** | 
Tempo estimado de conclusão: ***06/05/21*** |

### INSTRUÇÕES DE INSTALAÇÃO E USO
**Instalação no IntelliJ**

  1. Importar projeto para o IntelliJ
  2. Execute a classe Recibo para ativar o programa.
  3. O console exibirá a saída calculada.
  4. Nomes de arquivos opcionais podem ser fornecidos acessando Executar> Configurações de arquivo e digitando: "PATH / TO / Filename.txt" nos argumentos do programa. Irá demorar mais do que uma string de nome de arquivo por vez.

**Pacote de teste disponível no diretório de teste**
  1.Execute a classe ReceiptTest para teste de desafio
 
### OPÇÕES DE TESTE 
Testes de projeto e testes básicos de sucesso de desafio foram fornecidos. Eles podem ser encontrados no diretório de teste.

### PREMISSAS
Abaixo estão notas e abordagens com base nas expectativas de desafio.

Entrada de arquivo |
---|
Uma série de nomes de arquivos pode ser importada no início do programa. |
Se nenhum nome de arquivo for fornecido, 3 arquivos .txt serão carregados. |
Os exemplos de desafio precisarão ser fornecidos como um arquivo .txt e executados, se nenhum nome de arquivo tiver sido fornecido. |
Será necessário um padrão de linha ou guia de sintaxe envolvido em todos os arquivos de entrada. Isso garantirá o tratamento adequado da transcodificação de dados. |
Um leitor de arquivos precisará ser implementado em algum momento. |

Transcodificação |
---|
Cada item de linha conterá 3 informações cruciais - Quantidade. Descrição. Preço. |
Os dados da string numérica precisarão ser convertidos em um número inteiro para os cálculos. |
Regex pode ser usado para separar as informações. |

Objetos e Classes |
---|
Recibo - classe de controlador
Calculadora de Receitas - Aula encarregada de calcular impostos sobre vendas e totais |
Scanner de recibos - cria compras e itens com base nos dados do leitor de arquivos chamado |
Compra - Aula para armazenar vários itens. Também poderia supervisionar os totais? |
Item - classe para lidar com as informações do item, como descrição, quantidade, tipo de faixa de imposto e preço. |
Console de recebimento - Classe de exibição encarregada de fornecer saída para o console. |
Validação de recibo - verifica se os dados do arquivo são válidos |

Outro |
---|
A saída de dados será por meio do console. |
O conjunto de testes precisará ser criado para o sucesso do desafio. |
O multiplicador de quantidade não foi discutido no desafio, mas a lógica para ele deve ser incluída. |

### CASOS DE USO

Como cliente / usuário ...  |
---|
... Desejo fornecer novos dados de compra por meio de nomes de arquivo .txt. |
... Quero ver o total do imposto sobre vendas. |
... Quero ver o total atualizado do item. |
... Quero ver o total da compra. |
... Quero os detalhes do item organizados corretamente para saída. |
... Quero que o valor da compra do item seja atualizado na saída. |
... Quero que a saída seja mostrada no console do terminal. |
... Quero que o imposto sobre vendas seja cobrado a uma taxa básica de 10%. |
... Quero uma categoria ISENTA de itens com 0% de imposto sobre vendas. |
... Quero um imposto sobre vendas IMPORT calculado em 5% adicional sobre todas as mercadorias. |
... Quero que o cálculo do imposto sobre vendas seja arredondado para o 0,05 mais próximo. |

Como desenvolvedor ...  |
---|
... Vou usar o controle de versão .git. |
... Fornecerei 3 carrinhos de amostra como arquivos .txt. |
... Permitirei que novos nomes de arquivo recebam informações do carrinho - especificadas nestas instruções. |
... Vou criar modelos de separação de funcionalidade para melhorias futuras, bem como para manter as práticas de OOD e RESTful. |
... Vou fornecer dois conjuntos de testes (teste de método e metas de desafio). |

### Notas, ideias e feedback sobre o desafio  
Este foi meu primeiro projeto Java desde 5 anos que nao programava em JAVA, então tive que me atualizar rapidamente com as bibliotecas e sintaxe Java, IntelliJ e jUnit. Ler, seguir tutoriais e rastrear erros foram uma grande parte desse desafio. Uma vez que comecei no aspecto de codificação - ele veio junto muito rápido.

A parte mais difícil deste desafio foi envolver minha cabeça em torno do IntelliJ. Depois de fazer alguns tutoriais de amostra sobre configurações de projeto, as filas de construção surgiram naturalmente. Não fiz muito nas formas de desenvolvimento orientado a teste neste projeto, o que não é normal para mim. Eu estava tentando entender o java em geral, então, em um esforço para economizar algum tempo, decidi fazer o teste depois. Lame - eu sei, eu sei.

Houve três momentos principais de pensamento crítico que tive que fazer para este projeto. Tive que descobrir como transcodificar cada item de linha corretamente. Tive que descobrir como determinar o preço do imposto sobre vendas. Para isso, acho que encontrei uma boa solução por enquanto, mas é baseada em palavras-chave como 'chocolate'. Em um mundo perfeito, você teria modelos de inventário para acessar os detalhes. Por último, tive que voltar ao meu código no final, porque percebi que não levei em conta os números de quantidade - que se você comprar digamos "2 CDs do Batman Forever" - então, seria calculado apenas o preço de um.


Quanto ao feedback do desafio, achei o desafio muito fácil. O texto do desafio era um pouco confuso no início, mas quando comecei a acertar as partes, entendi claramente - ficou claro. Eu gostaria que houvesse mais contexto em que isso seria usado (fictício ou não). Acho que isso ajuda no processo de construção e interrompe aqueles momentos "e se".

Usei tambem Team Treehouse, Lynda, Stack Overflow e o wiki java / junit como principais fontes de pesquisas. Eu adoraria um feedback se você tiver tempo ou quiser! Obrigado.
