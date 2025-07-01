
## Visão Geral

Este sistema automatiza o processo de cadastro de produtos em um sistema web, utilizando Python com as bibliotecas `pyautogui`, `time` e `pandas`. O script realiza o login no site da empresa, lê uma base de dados de produtos e preenche automaticamente os campos do formulário de cadastro para cada produto listado.

## Requisitos

- Python 3.x
- Bibliotecas: `pyautogui`, `pandas`
- Navegador Google Chrome instalado
- Arquivo `produtos.csv` com os dados dos produtos

## Passos Realizados

1. **Abertura do Navegador e Acesso ao Site**
   - O script abre o navegador Chrome e acessa a URL de login do sistema da empresa.

2. **Login Automático**
   - Preenche automaticamente os campos de e-mail e senha e realiza o login.

3. **Leitura da Base de Dados**
   - Lê o arquivo `produtos.csv` contendo os dados dos produtos a serem cadastrados.

4. **Cadastro Automático dos Produtos**
   - Para cada produto na base, o script:
     - Clica no botão "Novo"
     - Preenche os campos do formulário (código, marca, tipo, categoria, preço unitário, custo, observações)
     - Envia o formulário

5. **Repetição**
   - O processo é repetido para todos os produtos listados no arquivo CSV.

## Estrutura do Arquivo CSV

O arquivo `produtos.csv` deve conter as seguintes colunas:

- `codigo`
- `marca`
- `tipo`
- `categoria`
- `preco_unitario`
- `custo`
- `obs` (opcional)

## Observações

- As coordenadas dos cliques (`x`, `y`) podem variar de acordo com a resolução da tela e o layout do site. Ajuste conforme necessário.
- O script utiliza delays (`time.sleep`) para garantir que os elementos estejam carregados antes das interações.
- O uso de `pyautogui` desabilita o fail-safe, então utilize com cautela.



