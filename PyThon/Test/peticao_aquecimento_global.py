## ---------------------------------------------------------------------- "ADIÇÃO DE PLUGINS AO CÓDIGO" ------------------------------------------------------------------------------

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTableWidget, QVBoxLayout, QHBoxLayout, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from sys import argv

## ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Janela(QWidget):
    def __init__(self):
        self.linha = 0
        super().__init__()
        self.setWindowTitle("PETIÇÃO PARA O AQUECIMENTO GLOBAL")  #  "TITULO DA JANELA"
        self.setGeometry(150,50,1600,900)  #  "SETAR TAMALHO DA JANELA"
        self.setStyleSheet("background-color:#800000")  #  "COR DA JANELA"
        self.setWindowIcon(QIcon(""))  #  "ICONE DA JANELA"

## ------------------------------------------------------------------------------------------ "LAYOUT HORIZONTAL E VERTICAL"

        self.layout_horizontal = QHBoxLayout()  
        self.layout_horizontal.setSpacing(0)  #  "SETAR ESPAÇAMENTO DE LAYOUTS"
        self.layout_vertical = QVBoxLayout()

## ------------------------------------------------------------------------------------------- "COLUNA DIREITA"

        self.label_col_dir = QLabel()
        self.label_col_dir.setFixedWidth(800)
        
        self.label_logo_dir = QLabel()                                  #"LOGO"#
        self.label_logo_dir.setPixmap(QPixmap("aquecimento.jpg"))  #  "IMAGEM APLICADA"
        self.label_logo_dir.setScaledContents(True)  #  "REISCALONAR A IMAGEM "
        
## ------------------------------------------------------------------------------------------- "COLUNA ESQUERDA"
                                        # "TITULO"
        self.label_col_esq = QLabel()                                         #"COLUNA"#
        self.label_col_esq.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")
        self.label_col_esq.setLayout(self.layout_vertical)
        
        self.label_col_esq_T = QLabel("nos ajude a melhorar o planeta.")
        self.label_col_esq_T.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")

                                        # "NOME"
        self.nome_label_esq = QLabel("por favor, digite seu nome:")                                    #"ENTRADA DE DADOS"#
        self.nome_label_esq.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")
        self.nome_entrada_esq = QLineEdit()
        self.nome_entrada_esq.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.nome_entrada_esq.setFixedHeight(50)

#--------------------------------------------------------------------------------------------------------------------------
                                        # "SOBRENOME"
        self.sobrenome_label_esq = QLabel("Sobrenome")
        self.sobrenome_label_esq.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")
        self.sobrenome_entrada_esq = QLineEdit()
        self.sobrenome_entrada_esq.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.sobrenome_entrada_esq.setFixedHeight(50)

#----------------------------------------------------------------------------------------------------------------------
                                        # "E-mail"                                       
        self.email_label_esq = QLabel("E-mail:")
        self.email_label_esq.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")
        self.email_entrada_esq = QLineEdit()
        self.email_entrada_esq.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.email_entrada_esq.setFixedHeight(50)

#-----------------------------------------------------------------------------------------------------------------------
                                        # "IDADE"
        self.idade_label_esq = QLabel("Idade:")
        self.idade_label_esq.setStyleSheet("QLabel{font-weight:bold; font-size:25pt; color:#000000}")
        self.idade_entrada_esq = QLineEdit()
        self.idade_entrada_esq.setStyleSheet("QLineEdit{font-size:15pt; color:#000000; background-color:#ffffff}")
        self.idade_entrada_esq.setFixedHeight(50)
##  --------------------------------------------------------------------------------------  "BOTÕES DE CADASTRO"

        self.play_push = QPushButton("CADASTRAR")
        self.play_push.setStyleSheet("QPushButton {background-color:#000000; color:#ffffff} QPushButton:hover {background-color:#ffffff; color:#000000}") 
        self.play_push.setFixedHeight(50)
        
        self.google_play = QPushButton("GOOGLE")
        self.google_play.setStyleSheet("QPushButton {background-color:#8B0000; color:#ffffff} QPushButton:hover {background-color:#ffffff; color:#8B0000}") 
        self.google_play.setFixedHeight(50)
        
        self.facebook_play = QPushButton("FACEBOOK")
        self.facebook_play.setStyleSheet("QPushButton {background-color:#00008B; color:#ffffff} QPushButton:hover {background-color:#ffffff; color:#00008B}") 
        self.facebook_play.setFixedHeight(50)

## ------------------------------------------------------------------------------------------------------------  "ADICIONAR OS ELEMENTOS"

        self.layout_vertical.addWidget(self.label_col_esq_T)
        self.layout_vertical.addWidget(self.nome_label_esq)
        self.layout_vertical.addWidget(self.nome_entrada_esq)

        self.layout_vertical.addWidget(self.sobrenome_label_esq)
        self.layout_vertical.addWidget(self.sobrenome_entrada_esq)

        self.layout_vertical.addWidget(self.email_label_esq)
        self.layout_vertical.addWidget(self.email_entrada_esq)
        
        self.layout_vertical.addWidget(self.idade_label_esq)
        self.layout_vertical.addWidget(self.idade_entrada_esq)
        
        self.layout_vertical.addWidget(self.play_push)
        self.layout_vertical.addWidget(self.google_play)
        self.layout_vertical.addWidget(self.facebook_play)

        self.layout_vertical.addWidget(self.label_col_dir)
        #self.layout_vertical.addLayout(self.label_col_dir)
        #self.setLayout(self.label_logo_dir)

## ------------------------------------------------------------------------------------------------------------

        self.layout_horizontal.addWidget(self.label_col_esq)
        self.layout_horizontal.addWidget(self.label_col_dir)
        
        self.setLayout(self.layout_horizontal)

## ------------------------------------------------------------------------------------------------------------ "FIM DO CÓDIGO"

app = QApplication(argv)
Janela = Janela()
Janela.show()
app.exec()

## -------------------------------------------------------------------------------------------