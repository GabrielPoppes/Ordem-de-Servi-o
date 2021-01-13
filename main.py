"""
ATUALIZAÇÃO:
1. SE A PESSOA NÃO CHECAR A CAIXA LEMBRAR DADOS, QUANDO CLICAR NO BOTÃO
SAIR NÃO VAI SALVAR OS DADOS DE LOGIN
2. ARRUMADO BOTÃO DE SAIR (VISUAL)
3. ADICIONADO LOGOTIPO NA TELA DE LOGIN E RECUPERAR SENHA
"""

"""
PENDÊNCIA:
1. MODO DE TELA EM TODAS AS TELAS DO PROGRAMA.
2. NA RECUPERAÇÃO DE SENHA, CHECAR SE TEM @ NO E-MAIL PARA VALIDAR.
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from layout import *



class Cores(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.lista = list()

        # ESCOLHER TEMA DO PROGRAMA
        self.botao_normal.clicked.connect(self.appnormal)
        self.botao_noturno.clicked.connect(self.appnorturno)

        # CORES DO PROGRAMA PADRÃO
        self.setStyleSheet('background: #E2E2E2;')
        self.label.setStyleSheet('color: black;')
        self.listWidget.setStyleSheet('background: white;')
        self.lineEdit.setStyleSheet('background: white;')
        self.atividades.setStyleSheet('background: white;')
        self.botao2.setStyleSheet('background: white;')

        self.fundo_top.setStyleSheet('background: #1351cd')
        self.fundo_footer.setStyleSheet('background: #1208ab')
        self.label.setStyleSheet('background: #1208ab; color: white;')
        self.botao_normal.setStyleSheet('background: #1208ab; color: white;')
        self.botao_noturno.setStyleSheet('background: #1208ab; color: white;')
        self.label_contato.setStyleSheet('color: white')
        self.btn_sair.setStyleSheet('QPushButton{'
                                    'background-color: #1208AB; '
                                    'border-radius: 5px;'
                                    'color: white;}'                
                                    'QPushButton:hover{'
                                    'color: #F0F0F0;}')

        # BOTÃO ENVIAR E REMOVER
        self.pushButton.clicked.connect(self.add_lista)
        self.pushButton_2.clicked.connect(self.remove_lista)
        self.btn_excluiros.clicked.connect(self.somente_remover_lista)

        # BOTÃO FECHAR NOTIFICAÇÃO ERRO (X)
        self.botao_x.clicked.connect(self.frame_error.hide)

        # TELA DE NOTIFICAÇÃO INICIAR FECHADA
        self.frame_error.hide()

        # BOTÃO LIMPAR O.S
        self.btnlimparatividadesok.clicked.connect(self.limpar_os)

        # BOTÃO ENTRAR (LOGIN)
        self.btn_entrarlog.clicked.connect(self.btn_entrar)

        # ERROR NA TELA DE LOGIN INICIAR OCULTO
        self.frame_error_login.hide()

        # BOTÃO FECHAR NOTIFICAÇÃO ERRO (TELA LOGIN)
        self.btn_x_login.clicked.connect(self.btn_error_login)

        # TELA ESQUECI MINHA SENHA INICIAR FECHADA
        self.frame_esquecisenha.hide()

        # FUNÇÃO QUANDO CLICA NO BOTÃO ESQUECI MINHA SENHA
        self.btn_esquecisenha.clicked.connect(self.esquecisenha)

        # FUNÇÃO BOTÃO "VOLTAR A TELA INICIAL" DA TELA ESQUECI MINHA SENHA
        self.btn_recuperarsenha_2.clicked.connect(self.voltar_tela_inicial)

        # ESCONDER FRAME ERROR TELA ESQUECI MINHA SENHA
        self.frame_error_password.hide()

        # BOTÃO RECUPERAR SENHA DA TELA
        self.btn_recuperarsenha.clicked.connect(self.recuperar_senha)

        # BOTÃO X (FECHAR TELA) DA TELA DE RECUPERAÇÃO DE SENHA
        self.btn_x_login_2.clicked.connect(self.botao_x_recuperarsenha)

        # BOTÃO SAIR DA TELA LOGADA
        self.btn_sair.clicked.connect(self.botaosair)

        # CONTADOR DOS NUMEROS DAS ATIVIDADES FINALIZADAS
        self.j = 1
        self.i = 0
        self.contadorn = int(1)

        # Bordas do programa
        self.listWidget.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.atividades.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.totalpendencia.setStyleSheet('background: rgb(255, 255, 255); '
                                          'border-radius: 5px; '
                                          'border: 1px solid black;')

        self.lineEdit.setStyleSheet('background: rgb(255, 255, 255); '
                                    'border-radius: 5px; '
                                    'border: 1px solid black;')

        self.btn_excluiros_n.setStyleSheet('background: rgb(255, 255, 255); '
                                           'border-radius: 5px; '
                                           'border: 1px solid black;')

        self.botao2.setStyleSheet('background: rgb(255, 255, 255); '
                                  'border-radius: 5px; '
                                  'border: 1px solid black;')

        self.n_ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                    'border-radius: 5px; '
                                    'border: 1px solid black;')

        self.totalfinalizadas.setStyleSheet('background: rgb(255, 255, 255); '
                                            'border-radius: 5px; '
                                            'border: 1px solid black;')

    # FUNÇÃO DO BOTÃO SAIR (QUANDO USER JÁ TÁ LOGADO)
    def botaosair(self):
        # Esconder frame de erros caso esteja aparecendo!
        self.frame_error.hide()

        # Mostrar frame de logout com sucesso na tela inicial!
        self.frame_login.show()
        self.frame_error_login.setStyleSheet('background-color: #52AE09;')
        self.frame_error_login.show()
        self.label_error_2.setText('Você foi desconectado com sucesso!')

    # FUNÇÃO DO X DA TELA DE RECUPERAÇÃO DE SENHA
    def botao_x_recuperarsenha(self):
        self.frame_error_password.hide()

    # FUNÇÃO DO BOTÃO RECUPERAR SENHA
    def recuperar_senha(self):
        if self.entrada_email.text() == '':
            self.frame_error_password.setStyleSheet('background-color: #FF0000;')
            self.frame_error_password.show()
            self.label_error_password.setText('Por favor, digite seu'
                                              ' endereço de e-mail!')

        else:
            self.frame_error_password.setStyleSheet('background-color: #52AE09;')
            self.frame_error_password.show()
            self.label_error_password.setText('Foi enviado um link de recuperação no seu'
                                              ' endereço de e-mail!')

    # FUNÇÃO BOTÃO VOLTAR TELA INICIAL
    def voltar_tela_inicial(self):
        self.frame_esquecisenha.hide()
        self.frame_error_password.hide()

    # BOTÃO ESQUECI MINHA SENHA, PARA ABRIR A FRAME DE RECUPERAÇÃO
    def esquecisenha(self):
        self.frame_esquecisenha.show()
        self.frame_error_login.hide()

    def btn_error_login(self):
        self.frame_error_login.hide()

    # FUNÇÕES DA FRAME DE ERROR DA TELA DE LOGIN! E TAMBÉM PRA SUMIR A TELA DO LOGIN APÓS
    # O ACESSO SER LIBERADO
    def btn_entrar(self):
        if self.entrada_login.text() == '' and self.entrada_senha.text() == '':
            self.frame_error_login.setStyleSheet('background-color: #FF0000;')
            self.frame_error_login.show()
            self.label_error_2.setText('Por favor, digite o nome do usuário e a senha para'
                                       ' acessar sua conta!')

        elif self.entrada_login.text() == '':
            self.frame_error_login.setStyleSheet('background-color: #FF0000;')
            self.frame_error_login.show()
            self.label_error_2.setText('Por favor, digite o nome do usuário!')

        elif self.entrada_senha.text() == '':
            self.frame_error_login.setStyleSheet('background-color: #FF0000;')
            self.frame_error_login.show()
            self.label_error_2.setText('Por favor, digite a senha do cadastro!')

        else:
            self.frame_login.hide()
            self.label_welcome.setText(f'Seja bem-vindo(a) {self.entrada_login.text()}!')

            # SE MARCAR O CAMPO DE SALVAR DADOS, NÃO APAGAR LOGIN E SENHA
            if self.checkBox_salvardados.isChecked():
                pass

            # SE NÃO MARCAR O CAMPO DE SALVAR DADOS, LIMPAR LOGIN E SENHA
            else:
                self.entrada_login.clear()
                self.entrada_senha.clear()

    def add_lista(self):
        # ITENS
        self.entradaitens = self.lineEdit.text()
        if self.entradaitens == '':
            self.frame_error.show()
            self.label_error.setText('Por favor, descreva a O.S!')

        else:
            self.atividades.addItem(self.entradaitens)
            self.lineEdit.clear()

            # NUMERACAO
            i = str(len(self.listWidget))
            self.listWidget.addItem(i)

            # Adicionando descrição da OS na lista de OS
            self.lista.append(self.entradaitens)

            # Esconder frame de erro caso esteja aparecendo
            self.frame_error.hide()

            # Adicionando + 1 no Total de Pendências
            self.totalpendencia.clear()
            self.tpendencia = str(len(self.listWidget))
            self.totalpendencia.addItem(self.tpendencia)

    def somente_remover_lista(self):
        # Removendo elemento da lista de OS Finalizadas
        num_remove = self.btn_excluiros_n.text()

        if num_remove == '':
            self.frame_error.show()
            self.label_error.setText('Por favor, digite o número da O.S!')

        elif num_remove >= str(len(self.listWidget)):
            self.frame_error.show()
            self.label_error.setText('Esta O.S não existe! Digite uma O.S'
                                     ' válida!')
            self.btn_excluiros_n.clear()

        else:
            num_remove_oficial = int(num_remove)
            self.atividades.takeItem(num_remove_oficial)
            self.listWidget.takeItem(len(self.atividades))
            self.lista.pop(num_remove_oficial)
            self.btn_excluiros_n.clear()

            # Removendo -1 no Total de Pendências
            self.totalpendencia.clear()
            self.tpendencia = str(len(self.listWidget))
            self.totalpendencia.addItem(self.tpendencia)

            # Esconder frame de erro caso esteja aparecendo
            self.frame_error.hide()

    def remove_lista(self):
        # ATIVIDADES
        nremove = self.botao2.text()
        if nremove == '':
            self.frame_error.show()
            self.label_error.setText('Por favor, digite o número da O.S!')

        elif nremove >= str(len(self.listWidget)):
            self.frame_error.show()
            self.label_error.setText('Esta O.S não existe! Digite uma O.S'
                                     ' válida!')
            self.botao2.clear()

        else:
            nremove_int = int(nremove)

            # Adicionando OS em campo do app "Finalizada"
            self.ospronta.addItem(self.lista[nremove_int])
            # Removendo elemento da lista de OS Finalizadas
            self.lista.pop(nremove_int)

            # Removendo OS das Pendentes
            self.atividades.takeItem(nremove_int)

            # NUMEROS
            self.listWidget.takeItem(len(self.atividades))
            self.botao2.clear()

            # Esconder frame de erro caso esteja aparecendo
            self.frame_error.hide()

            # Removendo -1 no Total de Pendências
            self.totalpendencia.clear()
            self.tpendencia = str(len(self.listWidget))
            self.totalpendencia.addItem(self.tpendencia)

            # Adicionando +1 no Total de Finalizadas
            self.totalfinalizadas.clear()
            self.tfinalizadas = str(len(self.ospronta))
            self.totalfinalizadas.addItem(self.tfinalizadas)

            # LISTA UTILIZADA COMO CONTADOR NOS NÚMEROS DAS O.S FINALIZADAS
            self.listateste = str(list())
            self.listateste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                               15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                               28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
                               41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53,
                               54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66,
                               67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79,
                               80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
                               93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104]

            # LÓGICA DOS NÚMEROS DA O.S FINALIZADA (PRA CONSEGUIR EXIBIR O PRIMEIRO NÚMERO
            # ZERO
            if self.j == 1:
                self.numos = str(0)
                self.n_ospronta.addItem(str(self.listateste[0]))
                self.j += 1

            # LÓGICA DOS NÚMEROS DA O.S FINALIZADA (PARA DAR SEQUÊNCIA NOS NÚMEROS DEPOIS DO
            # ZERO
            else:
                self.n_ospronta.addItem(str(self.listateste[self.i]))
            self.i += 1

    def limpar_os(self):
        # LÓGICA PARA QUE APAREÇA O ERRO CASO A LISTA ESTEJA VAZIA NA HORA DE LIMPAR
        if str(len(self.ospronta)) == '0':
            self.frame_error.show()
            self.label_error.setText('Sua lista de ordens finalizadas está vazia! ')

        else:
            self.ospronta.clear()
            self.n_ospronta.clear()
            self.j = 1
            self.i = 0
            # Esconder frame de erro caso esteja aparecendo
            self.frame_error.hide()

        # Zerar o total de finalizados
        self.totalfinalizadas.clear()
        self.tfinalizadas = str(len(self.ospronta))
        self.totalfinalizadas.addItem(self.tfinalizadas)

    def appnormal(self):
        self.setStyleSheet('background: #E2E2E2;')
        self.label.setStyleSheet('color: black;')
        self.listWidget.setStyleSheet('background: white;')
        self.lineEdit.setStyleSheet('background: white;')
        self.atividades.setStyleSheet('background: white;')
        self.ospronta.setStyleSheet('background: white;')
        self.botao2.setStyleSheet('background: white;')
        self.n_ospronta.setStyleSheet('background: white;')
        self.btn_excluiros_n.setStyleSheet('background: white;')
        self.totalpendencia.setStyleSheet('background: white;')
        self.totalfinalizadas.setStyleSheet('background: white;')

        self.fundo_top.setStyleSheet('background: #1351cd')
        self.fundo_footer.setStyleSheet('background: #1208ab')
        self.label.setStyleSheet('background: #1208ab; color: white;')
        self.botao_normal.setStyleSheet('background: #1208ab; color: white;')
        self.botao_noturno.setStyleSheet('background: #1208ab; color: white;')
        self.label_contato.setStyleSheet('color: white')
        self.label_welcome.setStyleSheet('color: black;')

        # Bordas do programa
        self.listWidget.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.atividades.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.totalpendencia.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.lineEdit.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.btn_excluiros_n.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.botao2.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.n_ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;')

        self.totalfinalizadas.setStyleSheet('background: rgb(255, 255, 255); '
                                    'border-radius: 5px; '
                                    'border: 1px solid black;')



    def appnorturno(self):
        self.setStyleSheet('background: #a7a7a7;')
        self.label.setStyleSheet('color: black;')
        self.listWidget.setStyleSheet('background: #dad1d1;')
        self.lineEdit.setStyleSheet('background: #dad1d1;')
        self.atividades.setStyleSheet('background: #dad1d1;')
        self.botao2.setStyleSheet('background: #dad1d1;')
        self.ospronta.setStyleSheet('background: #dad1d1;')
        self.n_ospronta.setStyleSheet('background: #dad1d1;')
        self.btn_excluiros_n.setStyleSheet('background: #dad1d1;')
        self.totalpendencia.setStyleSheet('background: #dad1d1;')
        self.totalfinalizadas.setStyleSheet('background: #dad1d1;')

        self.fundo_top.setStyleSheet('background: #070442')
        self.fundo_footer.setStyleSheet('background: #02001b')
        self.label.setStyleSheet('background: #02001b; color: white;')
        self.botao_normal.setStyleSheet('background: #02001b; color: white;')
        self.botao_noturno.setStyleSheet('background: #02001b; color: white;')
        self.label_contato.setStyleSheet('color: white;')
        self.label_welcome.setStyleSheet('color: white;')

        # Bordas do programa
        self.totalfinalizadas.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;'
                                      'background: #dad1d1;')

        self.listWidget.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;'
                                      'background: #dad1d1;')

        self.atividades.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;'
                                      'background: #dad1d1;')

        self.totalpendencia.setStyleSheet('background: rgb(255, 255, 255); '
                                          'border-radius: 5px; '
                                          'border: 1px solid black;'
                                          'background: #dad1d1;')

        self.lineEdit.setStyleSheet('background: rgb(255, 255, 255); '
                                    'border-radius: 5px; '
                                    'border: 1px solid black;'
                                    'background: #dad1d1;')

        self.btn_excluiros_n.setStyleSheet('background: rgb(255, 255, 255); '
                                           'border-radius: 5px; '
                                           'border: 1px solid black;'
                                           'background: #dad1d1;')

        self.botao2.setStyleSheet('background: rgb(255, 255, 255); '
                                  'border-radius: 5px; '
                                  'border: 1px solid black;'
                                  'background: #dad1d1;')

        self.n_ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                      'border-radius: 5px; '
                                      'border: 1px solid black;'
                                      'background: #dad1d1;')

        self.ospronta.setStyleSheet('background: rgb(255, 255, 255); '
                                    'border-radius: 5px; '
                                    'border: 1px solid black;'
                                    'background: #dad1d1;')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cores = Cores()
    cores.show()
    qt.exec_()