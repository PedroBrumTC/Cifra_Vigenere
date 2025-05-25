# Projeto: Criptografia e Ataque à Cifra de Vigenère

**autores:**
- Pedro Brum Tristão de Castro; 
- Mateus Oliveira Santos


Este projeto implementa a criptografia e descriptografia de arquivos utilizando a Cifra de Vigenère, além de um ataque baseado na análise de frequência de letras.

---

## Estrutura do Projeto

- **Cifra_Vigenere.py**: Implementa a classe `Vigenere` com os métodos de criptografia (`cypher`) e descriptografia (`decypher`),
  alem de realizar a ciptografia e descriptografia ao ser executado.

- **Ataque.py**: Implementa varias funções necessárias para realizar o ataque, alem de realizar o proprio ao ser executado.

- **textos/**: Pasta contendo arquivos de texto para realizar testes

- **cypher.ipynb**: Explicação e funcionamento da cifra de Vigenère, usando jupter notebook.

- **break.ipynb**: Explicação e funcionamento do ataque, usando jupter notebook.

- **README.txt**: Este manual de instruções.

- **Relatorio_cifra_vigenere.pdf**: Relatório do projeto

---

## Como Executar

### 1. Criptografar e/ou Descriptografar

- Colocar os arquivos no mesmo diretório que Cifra_vigenere.py
- Executar Cifra_vigenere.py
- passar as informaçoes de acordo com o que for pedido

**saida:**
- gera os arquivos criptografado (.bin) e/ou descriptografado (.txt)

---

### 2. Ataque

- Colocar os arquivos no mesmo diretório que Ataque.py
- Executar Ataque.py
- passar as informaçoes de acordo com o que for pedido

**saida:**
- um print com a chave com maior possibilidade de ser a utilizada naquele arquivo
