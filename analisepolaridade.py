import spacy
nlp = spacy.load('pt_core_news_lg')

#126 posemo e 127 negemo e 0 neutro
dicionario = {}
with open('lexico.txt') as lexico: 
    lexico = lexico.read()
    lexico = lexico.replace("\t","  ").splitlines()

    linha = 0
    while linha < len(lexico):
        if '126' in lexico[linha] and '127' not in lexico[linha]:
            lexico[linha]= lexico[linha].split(' ', 1)
            dicionario[lexico[linha][0]] = 1

        elif '127' in lexico[linha] and '126' not in lexico[linha]:
            lexico[linha] = lexico[linha].split(' ', 1)
            dicionario[lexico[linha][0]] = -1

        elif '127' in lexico[linha] and '126' in lexico[linha]: #tem ambas as anotações
            lexico[linha] = lexico[linha].split(' ', 1)
            dicionario[lexico[linha][0]] = 0

        else:
            lexico[linha] = lexico[linha].split(' ', 1)
            dicionario[lexico[linha][0]] = 0

        linha+=1
    
    #print(dicionario['movimentas'])

    with open('processado.txt', 'r', encoding='utf-8') as corpus:
        corpus = corpus.readlines()
        i = 0
        while i < len(corpus):
            print(corpus[i])
            corpus[i] = [palavra for palavra in corpus[i].split() if palavra in dicionario.keys()]#list comprehension
            

            j = 0
            while j < len(corpus[i]):
                corpus[i][j] = corpus[i][j] + ' ' +str(dicionario[corpus[i][j]])
                j+=1
            print( ' '.join(corpus[i]) + '\n-----------------------------------------------------')
            i+=1
            
        