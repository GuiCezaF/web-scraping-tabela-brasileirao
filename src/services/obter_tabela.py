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