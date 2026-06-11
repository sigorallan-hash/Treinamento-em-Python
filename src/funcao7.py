def acrescimo(preco: float, taxa: float ):
    '''
    A função acrecimo reaiza o cálculo de aumento
    do valor do preço do produto de acordo com a taxa.
    
     Args:
     
     preco(float): passe o preço do produto
     taxa(float): passe a taxa do acrecimo sem somente o número.
     
     return:
      
      Float: returna o preço do produto com o valor do acréscimo.
    '''
    return preco * (1+(taxa / 100))

rs = acrescimo(2500.90, 8.9)
    
print(f'O valor do acréscimo é: {rs}')