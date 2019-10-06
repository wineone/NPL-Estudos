import pandas as pd
from matplotlib import pyplot as plt
import string


def removePonctu(text):
    # trans = string.maketrans("","",string.punctuation)
    return text.translate(None,string.punctuation)

data = pd.read_csv("vgsales.csv")

ps4 = data[data['Platform'] ==  'PS4'].shape[0]
wii = data[data['Platform'] ==  'Wii'].shape[0]
pc = data[data['Platform'] ==  'PC'].shape[0]
xone = data[data['Platform'] ==  'XOne'].shape[0]

largura = 4

plt.title("quantidade de jogos vendidos no ultimo ano")
plt.bar(10,ps4,largura,label="ps4")
plt.bar(15,wii,largura,label="wii")
plt.bar(20,pc,largura,label="pc")
plt.bar(25,xone,largura,label="xone")

plt.legend()

# plt.show()

data['Name'] = data['Name'].apply(removePonctu) 


print data.head(20)
