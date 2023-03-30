import spacy
nlp = spacy.load('pt_core_news_lg')


arquivo = open('processado.txt', encoding='utf-8').readlines()
processado = open('palavrarelevante.txt','w+',encoding='utf-8')

for item in arquivo:
    documento = nlp(item)
    processado.write('---------------------\n')
    for token in documento:
        if token.pos_ == 'PROPN':
            processado.write(item + " " + token.text + "\n")