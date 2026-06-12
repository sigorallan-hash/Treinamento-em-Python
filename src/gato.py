class Cat:
    def __init__(self,raca,cor,tipo_de_pelo,idade,nome):
         
     '''
     Dogstring for __init__
         
     :para self: o comando que faz os atributos e métodos olhares para classe
     :param raca: a raça do gato
     :type raca: str
     :param cor: a cor do gato
     :type cor: str
     :param tipo_de_pelo: o tipo de pelo do gato
     :type tipo_de_pelo: str
     :param idade: a idade do gato
     :type idade: int
     :param nome: o nome do gato
     :type nome: str
     '''
         
     self.raca=raca
     self.cor=cor
     self.tipo_de_pelo=tipo_de_pelo
     self.idade=idade
     self.nome=nome
         
    def miar(self):
      print(f'{self.nome} miou.')
    def aranha(self):
        print(f'O {self.nome} aranhou.')
        
my_cat = Cat(f'rua','laranja','curto',20,'felix')
