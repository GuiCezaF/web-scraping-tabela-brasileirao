import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()

def ObtemTabela(serie: str) -> list:
  try:
    url= f"https://www.gazetaesportiva.com/campeonatos/brasileiro-serie-{serie}"
    req = session.get(url)

    elemento_nome_times: list = req.html.find("td.table__team")
    elemento_status: list = req.html.find("td.table__stats")
    
    nome_times = [elemento.text for elemento in elemento_nome_times]
    status = [elemento.text for elemento in elemento_status]
    pontos_times = status[::9]

    return nome_times, pontos_times
  except Exception:
    print(f"Erro ao obter a tabela\n {Exception}")
    
def MontarTabela(serie: str):
  times, pontos = ObtemTabela(serie)
  
  df = pd.DataFrame({
    'Time': times,
    'Pontuação': pontos
  })
  df['Posição'] = range(1, len(df) + 1)
  df = df[['Posição', 'Time', 'Pontuação']]
  
  col_widths = {
        'Posição': 8,
        'Time': 50,
        'Pontuação': 10
    }
  
  header = '|'.join([f"{col:^{col_widths[col]}}" for col in df.columns])
  separator = '+' + '+'.join(['-' * col_widths[col] for col in df.columns]) + '+'
  
  print(separator)
  print(f"|{header}|")
  print(separator)

  for _, row in df.iterrows():
      row_str = '|'.join([f"{str(row[col]):^{col_widths[col]}}" for col in df.columns])
      print(f"|{row_str}|")
      print(separator)

def Main() -> None:
    print('''
          
          \033[31mAluno: Guilherme Cezarino Felipe | RA:195249 \033[0;0m
          
          Bem vindo a Tabela do brasileirão!!
          Insira a baixo a divisão que gostaria de ver a tabela,
          temos as seguintes opções:
          Digite A (para a serie A) 
          Digite B (para a serie B) 
          ''')
    serie = input("Qual divisão gostaria de ver a tabela? ").lower()
    
    if serie != 'a' and serie != 'b':
      return print("Utilize uma opção valida")
    
    MontarTabela(serie)

Main()