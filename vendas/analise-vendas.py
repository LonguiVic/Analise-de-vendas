# coloque o diretório de onde você irá deixar o arquivo .txt
with open(r"C:\Users\Victo\Documents\vendas\vendas.txt", "r") as arquivo:
    texto = arquivo.read()
lista_texto = texto.split('\n')

faturamento = 0
# excluir a primeira linha
# para cada linha do meu arquivo
# somar o valor que vem depois do ;

faturamento = 0
lista_texto = lista_texto[1:]
for linha in lista_texto:
    if linha:
        pos_pv = linha.find(';')
        if pos_pv != -1:
            valor = float(linha[pos_pv+1:])
            faturamento += valor

print(faturamento)
