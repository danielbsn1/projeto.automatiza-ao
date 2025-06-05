#passo 1 - entrar no sistema da empresa (no caso, entrar no site https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui  # Desabilita o fail-safe, use com cuidado!
import time
import pandas as pd

pyautogui.PAUSE = 0.5

#passo 2 - abrir o navegador  # Ajuste as coordenadas conforme necessári
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter') 
time.sleep(2)     
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')  # Substitua pela URL do site
pyautogui.press('enter')
time.sleep(5) 

# - clicar no campo de login
pyautogui.click(  x=496, y=375)# Pressiona tab para navegar até o campo de email
time.sleep(1)  # Aguarda um segundo para garantir que o campo esteja ativo
pyautogui.write('jb355835@gmail.com')  # Substitua 'seu_usuario' pelo seu usuário
pyautogui.press('tab')  # Clica no campo de senha
pyautogui.write('senha123456')  # Substitua 'sua_senha' pela sua senha
pyautogui.press('enter') # Clica no botão de login
time.sleep(5)  # Aguarde o login

#passo 3 - importar a base de dados (tabela)
tabela = pd.read_csv('produtos.csv')
print(tabela)

# passo 4 - preencher os campos vazios
# Defina as coordenadas do botão "Novo"
BOTAO_NOVO_X = 632
BOTAO_NOVO_Y = 508

for linha in tabela.index:
    # Clique no botão "Novo" antes de cada cadastro
    pyautogui.click(x=BOTAO_NOVO_X, y=BOTAO_NOVO_Y)
    time.sleep(1)

    # Clique no campo de código
    pyautogui.click(x=653, y=294)
    time.sleep(1)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']).replace(',', '.'))
    pyautogui.press('tab')
    time.sleep(0.5)
    pyautogui.press('tab')  # Pula para o campo de custo
    pyautogui.write(str(tabela.loc[linha, 'custo']).replace(',', '.'))
    pyautogui.press('tab')
    time.sleep(0.5)
    obs = tabela.loc[linha, 'obs']
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.scroll(5000)
    time.sleep(1)
#passo 5 - repetir o processo de cadastro até o fim