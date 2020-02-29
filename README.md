### Descricao

Script desenvolvido para automatizar as batidas de ponto no RM Chronus utlizando a biblioteca selenium.
Foi implementada a funcionalidade de checar se o dia é final de semana ou feriado(em Portugal) e não fazer a batida. Para esses casos a batida terá que ser feita manual ou pode alterar o script conforme atender melhor a sua necessidade.

### Instrucoes de uso

##### Irá precisar instalar as dependencias `holidays` e `selenium`.
```
pip install holidays
pip install selenium
```
Também irá precisar baixar o geckodriver, o último release pode ser baixado [aqui](https://github.com/mozilla/geckodriver/releases)  
Decompactar o arquivo baixado e informar o caminho absoluto na variavel `geckodriver_driver_path` (default `C:\geockdriver\geckodriver.exe`).

##### Preencha as variaveis a seguir no começo do arquivo forms_filler_wafx.py conforme instruções

beg_work: entrada no trabalho  
out_lunch: saida para o almoco  
in_lunch: retorno do almoco  
out_work: saida do trabalho  
description: descricao da tarefa executada  
