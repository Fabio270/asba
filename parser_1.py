import spacy
nlp = spacy.load('pt_core_news_lg')

arquivo = open('processado.txt', encoding='utf-8').readlines()

arquivodep = open('dependencia.txt', 'w+',encoding='utf-8')

for i in arquivo:
    doc = nlp(i)
    arquivodep.write('---------------------\n')
    for token in doc:
        arquivodep.write(token.text + '  ' + token.dep_ + '  \n')