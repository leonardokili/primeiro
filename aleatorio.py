import random
nometimes = ['Palmeiras', "Internacional", "Fluminense", "Corinthians", "Flamengo",
         "Athletico", "Atlético-MG", "Fortaleza", "São Paulo", "América-MG",
         "Botafogo", "Santos", "Goiás", "RB Bragantino", "Coritiba",
         "Cuiabá", "Ceará", "Atlético-GO", "Avaí", "Juventude"]
random.shuffle(nometimes)
print(nometimes)
totalvit = []
totalder = []
totalemp = []

def pontuacao():
    der1=random.randint(5, 18)
    emp1=random.randint(6,18)
    de = der1 + emp1
    vit1 = 38 - emp1 - der1
    point = 3 * vit1 + emp1
    tabela.append(point)
    #print(3 * vit1 + emp1)
    totalvit.append(vit1)
    totalemp.append(emp1)
    totalder.append(der1)
x = 0
tabela = []
while x < 20:
    pontuacao()
    x += 1
tabela.sort()
tabela.reverse()
tab = zip(tabela, nometimes)
for team in tab:
    print(team)


pontuacao()