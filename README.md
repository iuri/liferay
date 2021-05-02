# Liferay

## Evaluation source code Liferay selection process
# Coding Problem: Sales Taxes
Please include all source files, unit tests, readme, batch files, etc. with your solution and e-mail to the person conducting your technical interview and cc: your recruiter.
Basic sales tax is applicable at a rate of 10% on all goods, except books, food, and medical products that are exempt. Import duty is an additional sales tax applicable on all imported goods at a rate of 5%, with no exemptions.
When I purchase items, I receive a receipt which lists the name of all the items and their price (including tax), finishing with the total cost of the items, and the total amounts of sales taxes paid. The rounding rules for sales tax are that for a tax rate of n%, a shelf price of p contains (np/100 rounded up to the nearest 0.05) amount of sales tax.
Write an application that prints out the receipt details for these shopping baskets:

# INPUT
## Input 1:
1 book at 12.49
1 music CD at 14.99
1 chocolate bar at 0.85
## Input 2:
1 imported box of chocolates at 10.00 1 imported bottle of perfume at 47.50
## Input 3:
1 imported bottle of perfume at 27.99 1 bottle of perfume at 18.99
1 packet of headache pills at 9.75
1 imported box of chocolates at 11.25

# OUTPUT
## Output 1:
1 book: 12.49
1 music CD: 16.49
1 chocolate bar: 0.85 Sales Taxes: 1.50 Total: 29.83
## Output 2:
1 imported box of chocolates: 10.50 1 imported bottle of perfume: 54.65 Sales Taxes: 7.65
Total: 65.15
## Output 3:
1 imported bottle of perfume: 32.19 1 bottle of perfume: 20.89
1 packet of headache pills: 9.75
1 imported box of chocolates: 11.85 Sales Taxes: 6.70
Total: 74.68


========== 


Na verdade, como esse problema não é tão grande, existem apenas duas classes e poucas funções de primeira classe.

# Design
Como este problema é bastante simples, decidi escrever uma classe de item para armazenar seus atributos, e uma classe que representa o carrinho de compras para adicionar itens e calcular totais. Pelo menos, era bastante óbvio para mim.

Algumas funções de primeira classe são usadas em duas classes ao mesmo tempo, portanto, foram colocadas separadamente dessas classes.

O catálogo com itens foi armazenado em um arquivo separado (data / catalog.json) para torná-lo simples de modificar no futuro. O formato JSON foi usado porque é muito semelhante ao dicionário Python (em nosso caso).

# Uso
Este programa pode ser utilizado/executado diretamente online em: https://replit.com/@IuriSampaio2/liferay#
ou localmente, seguindo as instrucoes abaixo.

Apenas a biblioteca padrão foi usada, portanto, para executar esta solução, você precisa apenas do Python 3.

Vá para o diretório onde os arquivos sales_taxes.py e sales_taxes_tests.py estão armazenados.

Para executar testes, digite python3 sales_taxes_tests.py primeiro. Adicione o argumento -v se quiser verbosidade.

Para executar a solução, digite python3 sales_taxes.py [PATH TO ORER FILE], por exemplo:

Para testar a entrada 1: python3 sales_taxes.py data / order_1.txt

Para testar a entrada 2: python3 sales_taxes.py data / order_2.txt

Para testar a entrada 3: python3 sales_taxes.py data / order_3.txt

Além disso, o arquivo test_order.txt foi adicionado para demonstrar a análise do arquivo com espaços

Divirta-se! Have Fun!
