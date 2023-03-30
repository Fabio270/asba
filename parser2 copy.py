import spacy
import csv

nlp = spacy.load('pt_core_news_lg')

arquivo = open('processado.txt', encoding='utf-8').readlines()
dicionario = {} #sem asterisco
radicais = {127:[], 126:[]}  #tem asterisco

def abredic():
    with open('lexico.txt', encoding='utf-8') as lexico:
        lexico = lexico.read()
        lexico = lexico.replace("\t","  ").splitlines()

        linha = 0
        while linha < len(lexico):

            if '127' in lexico[linha] and '126' in lexico[linha]: #tem ambas as anotações
                lexico[linha] = lexico[linha].split(' ', 1)
                dicionario[lexico[linha][0]] = 2

            elif '127' in lexico[linha]: #negativas
                if '*' not in lexico[linha]:
                    lexico[linha] = lexico[linha].split(' ', 1)
                    dicionario[lexico[linha][0]] = -1
                else:#ter asterisco
                    lexico[linha] = lexico[linha].split(' ', 1)
                    radicais[127].append(lexico[linha][0].replace('*',''))


            elif '126' in lexico[linha]: #positivas
                if '*' not in lexico[linha]:
                    lexico[linha]= lexico[linha].split(' ', 1)
                    dicionario[lexico[linha][0]] = 1
                else: #se tiver asterisco vai para o dicionário de radicais
                    lexico[linha] = lexico[linha].split(' ', 1)
                    radicais[126].append(lexico[linha][0].replace('*', ''))


            """ else: #não tem anotação de sentimento
                lexico[linha] = lexico[linha].split(' ', 1) 
                dicionario[lexico[linha][0]] = 0 """

            linha+=1
abredic()

with open('resultado.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['line 0'] + ['token ' + str(i) for i in range(100)] + ['Sentiment']) # altere 100 para o número máximo de tokens que deseja imprimir
    for i, line in enumerate(arquivo):
        doc = nlp(line)
        for token in doc:
            row = ['line ' + str(i+1)]
            for t in doc:
                row.append(t.text)
            if token.text in dicionario.keys():
                row.append(dicionario[token.text])
            elif any(radical in token.text for radical in radicais[127]):
                row.append(127)
            elif any(radical in token.text for radical in radicais[126]):
                row.append(126)
            else:
                row.append(-2)
            writer.writerow(row)

print("PROGRAMA ENCERRADO")
