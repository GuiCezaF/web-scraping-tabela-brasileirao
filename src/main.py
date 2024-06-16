from services.montar_tabela import  MontarTabelaExcel, MontarTabelaTerminal

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
    
    tipo_retorno = input("Deseja ver no termianal ou exportar para excel? (EXCEL ou TERMINAL)").lower()
    if tipo_retorno != "excel" and tipo_retorno != "terminal":
      return print("Utilize uma opção valida")
    if tipo_retorno == "excel":
      MontarTabelaExcel(serie)
    

Main()