#CREATOR
#GitHub - > TonnyThe2nd
#Instagram - > @web_4ntonio
#E-mail - > antoniomarcos3577@gmail.com
#Linkedn - > www.linkedin.com/in/antonio-marcos-sousa-de-oliveira-25b902272


from tkinter import *
import math

#configuração da interface 
root = Tk()
root.geometry("570x447")
root.maxsize(570,447)
root.configure(background='#dfdfdf')
root.title('Calculadora')
#FRAME DA TELA DE VALORES SELECIONADOS E RESULTADO
win = Frame(root, width=570, height=150, bg='#dfdfdf')
win.grid(row=0, column=0)

calc = Entry(win,width=21, font=('Ivy 18', 30) , borderwidth=4, relief=FLAT, justify=RIGHT, bg='#dfdfdf')
calc.place(x=0, y=20)
#FRAME DE BOTÕES
win_2 = Frame(root, width=750, height=300, bg='#dfdfdf')
win_2.grid(row=1, column=0)
val = ' '
x = 1
#VERIFICADORES DE OPERAÇÃO
ponto_ver = False
somar = False
raiz_conta = False
log_conta = False
subtrair = False
dividir = False
multiplicar = False
fatorial = False
porcentagems = False
elevar_a_dois = False
dois_elevados = False
senos = False
cossenos= False
tangentes = False
seno_menos = False
cosseno_menos = False
tangente_menos = False
in_contas = False
inv_contas = False
exp_contas = False
um_sob_x = False
ans_contas = False
e_contas = False
pi_val = 0
numb_um = ''
numb_dois = ''
num_2_check = True

def valor(valor):
    global num_2_check
    global numb_um
    calc.insert(END, valor) 
#FUNÇÃO DE SOMA
def soma():
    global val
    global num_2_check
    global numb_um
    global somar 
    somar = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
#FUNÇÃO DE SUBTRAÇÃO
def sub():
    global val
    global subtrair
    global num_2_check
    global numb_um
    subtrair = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
#FUNÇÃO DE DIVISÃO
def div():
    global val
    global dividir
    global num_2_check
    global numb_um
    dividir = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)  
#FUNÇÃO DE MULTIPLICAÇÃO
def mult():
    global val
    global multiplicar
    global num_2_check
    global numb_um
    multiplicar = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END) 
#FUNÇÃO DE RAIZ 
def raiz():
    global val
    global numb_um
    global ponto_ver
    val = calc.get()
    numb_um = val
    if ponto_ver == True:
        numb_um = float(numb_um)
        calc.delete(0,END)
        calc.insert(END, (f'{math.sqrt(numb_um):.2f}'))
    else:
        numb_um = int(numb_um)
        calc.delete(0,END)
        calc.insert(END, (f'{math.sqrt(numb_um):.2f}'))
#FUNÇÃO DE 1 DIVIDIDO POR NÚMERO ESCOLHIDO
def um_sob():
    global val
    global um_sob_x
    global num_2_check
    global numb_um
    um_sob_x = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    if ponto_ver == True:
        numb_um = float(numb_um)
        calc.insert(END, f'{1/numb_um:.2f}')
    else:
        numb_um = int(numb_um)
        calc.insert(END, f'{1/numb_um:.2f}')
#FUNÇÃO DE POTENCIA
def elevar():
    global val
    global elevar_a_dois
    global num_2_check
    global numb_um
    global ponto_ver
    elevar_a_dois = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    if ponto_ver == True:
        numb_um = float(numb_um)
        calc.insert(END, numb_um**2)
    else:
        numb_um = int(numb_um)
        calc.insert(END, numb_um**2)
#FUNÇÃO DE PORCENTAGEM
def porcentagem():
    global val
    global porcentagems
    global num_2_check
    global numb_um
    porcentagems = True
    val = calc.get()
    numb_um = val
    calc.insert(END, '%')
#FUNÇÃO DE LOG
def in_conta():
    global val
    global in_contas
    global num_2_check
    global numb_um
    in_contas = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    if ponto_ver == True:
        numb_um = float(numb_um)
        calc.insert(END, f'{math.log(numb_um):.2f}')
    else:
        numb_um = int(numb_um)
        calc.insert(END, f'{math.log(numb_um):.2f}')
#FUNÇÃO DE SENO
def seno():
    global val
    global senos
    global num_2_check
    global numb_um
    senos = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.sin(numb_um):.2f}'))
#FUNÇÃO DE COSSENO
def cosseno():
    global val
    global cossenos
    global num_2_check
    global numb_um
    cossenos = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.cos(numb_um):.2f}'))
#FUNÇÃO DE TANGENTE
def tangente():
    global val
    global tangentes
    global num_2_check
    global numb_um
    tangentes = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.tan(numb_um):.2f}'))

def inv_conta():
    global val
    global inv_contas
    global num_2_check
    global numb_um
    inv_contas = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
#FUNÇÃO DE PI
def pi():
    global numb_um
    global ponto_ver
    ponto_ver = True
    numb_um = math.pi
    calc.insert(END, f'{numb_um:.2f}')
#FUNÇÃO DE SENO NEGATIVO
def seno_neg():
    global val
    global num_2_check
    global seno_menos
    global numb_um
    seno_menos = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.asin(numb_um):.2f}'))
#FUNÇÃO DE COSSENO NEGATIVO
def cosseno_neg():
    global val
    global cosseno_menos
    global num_2_check
    global numb_um
    cosseno_menos = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.acos(numb_um):.2f}'))
#FUNÇÃO DE TANGENTE NEGATIVA
def tangente_neg():
    global val
    global tangente_menos
    global num_2_check
    global numb_um
    tangente_menos = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = int(numb_um)
    calc.insert(END, (f'{math.atan(numb_um):.2f}'))

def e_conta():
    global val
    global e_contas
    global num_2_check
    global numb_um
    e_contas = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    numb_um = float(numb_um)
    calc.insert(END, f'{numb_um*2.71828:.2f}')
#FUNÇÃO DE POTENCIA DE DOIS
def dois_elevar():
    global val
    global num_2_check
    global numb_um
    global dois_elevados
    dois_elevados = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
#FUNÇÃO DE FATORIAL
def fat():
    global val
    global fatorial
    global x 
    global numb_um
    fatorial = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
    if fatorial == True:
        numb_um = int(numb_um)
        for i in range(1,numb_um+1):
            x*=i
        calc.insert(END, x)
#FUNÇÃO DE LOG DE 10
def logaritmo():
    global val
    global num_2_check
    global numb_um
    global log_conta
    global ponto_ver
    log_conta = True
    val = calc.get()
    numb_um = val
    calc.delete(0,END)
    if ponto_ver == True:
        numb_um = float(numb_um)
        calc.insert(END, f'{math.log10(numb_um):.2f}')
    else:
        numb_um = int(numb_um)
        calc.insert(END, f'{math.log10(numb_um):.2f}')
def exp_conta():
    global val
    global num_2_check
    global numb_um
    global exp_contas
    exp_contas = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
def ans_conta():
    global val
    global num_2_check
    global numb_um
    global ans_contas
    ans_contas = True
    val = calc.get()
    numb_um = val
    calc.delete(0, END)
def ponto():
    global ponto_ver
    ponto_ver = True
    calc.insert(END, '.')
def conta():
    global numb_dois
    global numb_um
    global ans_contas
    global exp_contas
    global log_conta
    global somar
    global subtrair
    global dividir
    global multiplicar
    global raiz_conta
    global fatorial
    global log_conta
    global senos
    global cossenos
    global tangentes
    global seno_menos
    global cosseno_menos
    global tangente_menos
    global e_contas
    global um_sob_x
    global elevar_a_dois
    global dois_elevados
    global inv_contas
    global in_contas
    global ponto_ver
    global x
    numb_dois = calc.get()
    if somar == True:
        if ponto_ver == True:
            numb_um = float(numb_um)
            numb_dois = float(numb_dois)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um+numb_dois):.2f}')
        else:
            numb_dois = int(numb_dois)
            numb_um = int(numb_um)
            calc.delete(0,END)
            calc.insert(END, numb_um+numb_dois)
    if subtrair == True:
        if ponto_ver == True:
            numb_um = float(numb_um)
            numb_dois = float(numb_dois)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um-numb_dois):.2f}')
        else:
            numb_dois = int(numb_dois)
            numb_um = int(numb_um)
            calc.delete(0,END)
            calc.insert(END, numb_um-numb_dois)
    if multiplicar == True:
        if ponto_ver == True:
            numb_um = float(numb_um)
            numb_dois = float(numb_dois)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um*numb_dois):.2f}')
        else:
            numb_dois = int(numb_dois)
            numb_um = int(numb_um)
            calc.delete(0,END)
            calc.insert(END, numb_um*numb_dois)
    if dividir == True:
        if ponto_ver == True:
            numb_um = float(numb_um)
            numb_dois = float(numb_dois)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um/numb_dois):.2f}')
        else:
            numb_dois = int(numb_dois)
            numb_um = int(numb_um)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um/numb_dois):.2f}')
    if dois_elevados == True:
        if ponto_ver == True:
            numb_um = float(numb_um)
            numb_dois = float(numb_dois)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um**numb_dois):.2f}')
        else:
            numb_dois = int(numb_dois)
            numb_um = int(numb_um)
            calc.delete(0,END)
            calc.insert(END, f'{(numb_um**numb_dois):.2f}')  
    if porcentagems == True:
        numb_um = float(numb_um)
        calc.delete(0,END)
        calc.insert(END, numb_um/100)
def del_all():
    global numb_dois
    global numb_um
    global ans_contas
    global exp_contas
    global log_conta
    global somar
    global subtrair
    global dividir
    global multiplicar
    global raiz_conta
    global fatorial
    global log_conta
    global senos
    global cossenos
    global tangentes
    global seno_menos
    global cosseno_menos
    global tangente_menos
    global e_contas
    global um_sob_x
    global elevar_a_dois
    global dois_elevados
    global inv_contas
    global in_contas
    global ponto_ver
    global x
    global val
    val = ' '
    x = 1
    ponto_ver = False
    somar = False
    raiz_conta = False
    log_conta = False
    subtrair = False
    dividir = False
    multiplicar = False
    fatorial = False
    porcentagems = False
    elevar_a_dois = False
    dois_elevados = False
    senos = False
    cossenos= False
    tangentes = False
    seno_menos = False
    cosseno_menos = False
    tangente_menos = False
    in_contas = False
    inv_contas = False
    exp_contas = False
    um_sob_x = False
    ans_contas = False
    e_contas = False
    global pi_val
    pi_val = 0
    numb_um = ''
    numb_dois = ''
    calc.delete(0,END)
    numb_um = ' '
    numb_dois = ' '

#BOTÕES

button_porc = Button(win_2,text='%',command=porcentagem,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_porc.place(x=2,y=0)
button_ce = Button(win_2,text='CE',font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_ce.place(x=82,y=0)
button_c = Button(win_2,text='C',command=del_all,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=11 )
button_c.place(x=162,y=0)

button_in = Button(win_2,text='In',command=in_conta,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_in.place(x=326,y=0)
button_sin = Button(win_2,text='Sin',command=seno,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_sin.place(x=406,y=0)
button_inv = Button(win_2,text='Inv',command=inv_conta,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_inv.place(x=486,y=0)

button_um_div = Button(win_2,text='1/x',command=um_sob,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_um_div.place(x=2,y=50)
button_pow = Button(win_2,text='x²',command=elevar,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_pow.place(x=82,y=50)
button_raiz = Button(win_2,text='RAIZ',command=raiz,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_raiz.place(x=162,y=50)
button_div = Button(win_2,text='/',command=div,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_div.place(x=243,y=50)

button_e = Button(win_2,text='E',command=e_conta,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_e.place(x=326,y=100)
button_tan = Button(win_2,text='Tan',command=tangente,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_tan.place(x=406,y=100)
button_yx = Button(win_2,text='y^x',command=dois_elevar,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_yx.place(x=486,y=100)

button_pi = Button(win_2,text='π',command=pi,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_pi.place(x=326,y=50)
button_cos = Button(win_2,text='Cos',command=cosseno,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_cos.place(x=406,y=50)
button_log = Button(win_2,text='Log',command=logaritmo,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_log.place(x=486,y=50)


button_7 = Button(win_2,text='7', command=lambda: valor('7') ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_7.place(x=2,y=100)
button_8 = Button(win_2,text='8', command=lambda: valor('8'), font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_8.place(x=82,y=100)
button_9 = Button(win_2,text='9',command=lambda: valor('9'), font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_9.place(x=162,y=100)
button_x = Button(win_2,text='*',command=mult,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_x.place(x=243,y=100)


button_6 = Button(win_2,text='6', command=lambda: valor('6'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_6.place(x=2,y=150)
button_5 = Button(win_2,text='5' , command=lambda: valor('5'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_5.place(x=82,y=150)
button_4 = Button(win_2,text='4' , command=lambda: valor('4'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_4.place(x=162,y=150)
button_min = Button(win_2,text='-',command=sub,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_min.place(x=243,y=150)

button_sin_1 = Button(win_2,text='sin-1',command=seno_neg,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_sin_1.place(x=326,y=150)
button_cos_1 = Button(win_2,text='cos-1',command=cosseno_neg ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_cos_1.place(x=406,y=150)
button_tan_1 = Button(win_2,text='tan-1',command=tangente_neg ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_tan_1.place(x=486,y=150)

button_3 = Button(win_2,text='3' , command= lambda: valor('3'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_3.place(x=2,y=200)
button_2 = Button(win_2,text='2' , command= lambda: valor('2'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_2.place(x=82,y=200)
button_1 = Button(win_2,text='1' , command= lambda: valor('1'),font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_1.place(x=162,y=200)
button_sum = Button(win_2,text='+',command=soma,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_sum.place(x=243,y=200)

button_exp = Button(win_2,text='EXP',command=exp_conta ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_exp.place(x=326,y=200)
button_fat = Button(win_2,text='X!',command=fat ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_fat.place(x=406,y=200)
button_ANS = Button(win_2,text='ANS',command=ans_conta ,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_ANS.place(x=486,y=200)

button_0 = Button(win_2,text='0',command=lambda: valor('0'), font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_0.place(x=2,y=250)
button_ponto = Button(win_2,text='.',command=ponto,font=('Ivy 18'), relief=GROOVE, overrelief=RIDGE, width=5 )
button_ponto.place(x=82,y=250)
button_igual = Button(win_2,text='=', command=conta,font=('Ivy 17',19), relief=GROOVE, overrelief=RIDGE, width=10)
button_igual.place(x=162,y=250)
root.mainloop()