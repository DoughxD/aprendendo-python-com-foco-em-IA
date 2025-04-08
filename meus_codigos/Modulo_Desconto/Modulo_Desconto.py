"""
📦 Projeto: Módulo de Descontos Reutilizáveis

🔹 Descrição:
Este módulo implementa um conjunto de funções reutilizáveis para cálculo de descontos em um sistema de vendas.
Foi desenvolvido como parte de um treinamento técnico voltado para boas práticas, modularização e clareza de código.

🔧 Funcionalidades:
1. calcular_desconto(valor: float, percentual: float) -> float
   - Aplica um desconto percentual sobre um valor e retorna o resultado final.

2. avaliar_faixa_desconto(valor: float) -> float
   - Retorna o percentual de desconto adequado de acordo com a faixa de valor:
     • Até R$99,99 → 0%
     • De R$100 até R$499,99 → 5%
     • A partir de R$500 → 10%

3. preco_final(valor: float) -> float
   - Função final que integra as duas anteriores, retornando o valor com o desconto aplicado automaticamente.

🎯 Objetivo:
Permitir que o código seja utilizado em sistemas maiores, com clareza, reaproveitamento e fácil manutenção.

🧠 Autor: Douglas Sampaio  
📅 Data: 04/04/2025  
🛡️ Nível: Intermediário – Nível 3 (Progresso de Formação)
"""



def Avaliar_faixa_desconto(valor):
   if valor > 99.99 and valor < 500:
      return 0.05
   
   elif valor > 500:
      return  0.10
   
   else:
       return 0
   
def calcular_desconto(valor, percentual):
      
      return valor - valor * percentual


def preco_final(valor):
    desconto = Avaliar_faixa_desconto(valor)
    preco = calcular_desconto(valor, desconto)
    return preco

print(preco_final(354))

#def preco_final(valor):


