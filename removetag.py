texto = open('SentiCorpus-PT_01.txt', encoding='utf-8').read()
print(texto)


novotexto = ""
valida = 1
for i in texto.replace('</F>', '|'):
  if i == "<":
    valida = 0
  if valida == 1:
    novotexto += i
  if i == ">":
    valida = 1

novotexto = novotexto.replace('\n', '').replace('... ', '.').replace(' . ', '.').replace('. ', '.').replace(' .', '.').replace('  ', '').replace(' ! ', '!').replace(' , ', ', ').replace('| ', '|').rstrip('\n').strip()
novotexto = novotexto.split('|')

novoarquivo = open('processado.txt', 'w+', encoding='utf-8')
for linha in novotexto:
    novoarquivo.write(linha)
    novoarquivo.write("\n")
novoarquivo.close()
    