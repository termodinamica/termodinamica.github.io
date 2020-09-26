csv = open('NBS_Tables Library_with_ErratumValues.csv', 'r');
novo_csv = open('NBS_Tables Library_with_ErratumValues.js', 'w', encoding="utf-8")
linhas = csv.readlines();
novo_csv.write("var dados = [");
for linha in linhas:
    colunas = linha.strip().split(";")
    if len(colunas) > 10:
        if colunas[0].strip() != "" and colunas[4] != "" and colunas[4] in ['g', 'l', 's', 'aq']:
            novo_csv.write("['%s','%s','%s','%s','%s']," % (colunas[0].strip(), colunas[4].strip(), colunas[7].replace(".", ",").strip(), colunas[8].replace(".", ",").strip(), colunas[10].replace(".", ",").strip()))
novo_csv.write("];");