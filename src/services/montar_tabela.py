import pandas as pd
from services.obter_tabela import ObtemTabela


def MontarTabelaTerminal(serie: str) -> None:
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
      
      
def MontarTabelaExcel(serie: str) -> None:
  try:
    times, pontos = ObtemTabela(serie)
    
    df = pd.DataFrame({
      'Time': times,
      'Pontuação': pontos
    })
    df['Posição'] = range(1, len(df) + 1)
    df = df[['Posição', 'Time', 'Pontuação']]
    
    df.to_excel('tabela.xlsx', index=False)
    print('Arquivo tabela.xlsx foi criado!')
  except Exception:
    print(f"Erro ao montar a tabela\n {Exception}")
