import pyautogui
import time
import pandas;
#pyton2024
pyautogui.PAUSE = 3; #Tempo para cada comando em Segundos


pyautogui.press("win");
pyautogui.write("chrome");
pyautogui.press("enter");
pyautogui.click(x=950, y=292);

time.sleep(3);

pyautogui.click(x=603, y=61);
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login";
pyautogui.write(link);
pyautogui.press('enter');
time.sleep(3);


pyautogui.click(x=555, y=408);

pyautogui.press("tab");


pyautogui.press("tab");
pyautogui.press('enter');

pyautogui.click(x=952, y=680);
time.sleep(0.1);

""""import pandas;

tabela = pandas.read_csv("produtos.csv");
print(tabela);

for linha in tabela.index:

    pyautogui.click(x=709, y=319);

    pyautogui.write(tabela.loc[linha, 'codigo']);
    pyautogui.press('tab');

    pyautogui.write(tabela.loc[linha, 'marca']);
    pyautogui.press('tab');

    pyautogui.write(tabela.loc[linha, 'produto']);
    pyautogui.press('tab');
    
    pyautogui.write(str(tabela.loc[linha, 'categoria']));
    pyautogui.press('tab');

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']));
    pyautogui.press('tab');

    pyautogui.write(str(tabela.loc[linha, 'custo']));
    pyautogui.press('tab');

    obs=(tabela.loc[linha, 'obs'])
    if not pandas.isna(obs):
        pyautogui.write(obs);

    pyautogui.write(str(tabela.loc[linha, 'obs']));
    pyautogui.press('tab');

    pyautogui.press("enter")
    pyautogui.scroll(max)



"""

