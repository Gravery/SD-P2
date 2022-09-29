# SD-P2
Segundo trabalho prático Sistemas Distribuídos

---

*Alunos:*

Guilherme Calça - RA 790759

Pedro Lealdini do Prado Borges - RA 790894

---

Link da apresentação do projeto: 

---

O trabalho consiste na criação de uma rede de monitoramento onde estão presentes 20 lojas que possuem 210 variedades de produtos em cada uma, um centro de distibuição que fornece estoques dos produtos para todas as lojas e 70 fábricas que produzem 3 variedades produtos cada e mantém o estoque do CD.

A solução apresentada possui 3 arquivos nos quais são criados os objetos da loja, fábrica e CD e 3 arquivos main que realizam a criação dos objetos e iniciam a execução das tarefas. Ocorre a comunicação entre lojas e CD e entre CD e fábricas por meio do broker mqtt no qual todos estão conectados e as mensagens são enviadas e recebidas por método publish/subscribe. As lojas são publishers, cada qual com seu respectivo canal para requisitar reposição de um produto para o CD quando este produto possui nível vermelho de estoque, ou seja, possui menos de 25% de estoque. O CD é subscriber das 20 lojas para receber suas requisições e realizar o crédito nas mesmas e ao mesmo tempo é publisher para realizar as requisições das fábricas quando seu próprio estoque está abaixo de 25%. As fábricas são apenas subscribers do CD, cada uma com um canal próprio para receber mensagens do produto a ser reabastecido e fornecer crédito ao CD.

Para o sistema funcionar são realizadas operações de débito nas lojas a partir de um consumo aleatório de clientes de determinado produto, rodando todo o sistema acima do âmbito das lojas.

A execução da solução é simples: execute os 3 arquivos main simultaneamente e o sistema funcionará de forma automática, realizando toda comunicação entre os 3 programas por meio do broker e exibindo visualmente cada operação de débito, crédito e as requisições enviadas e recebidas para cada entidade.

