from tkinter import *
from tkinter import messagebox
import mysql.connector as sql
from datetime import date
from tkinter import ttk
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle 
from reportlab.lib import colors 
from reportlab.lib.pagesizes import A4 
from reportlab.lib.styles import getSampleStyleSheet 
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas#pdf
banco = sql.connect(    
    host="localhost",
    user="root",
    passwd="",
    database="pdv_tkinter"
)


# calcula salario,imprimi serviços,lerite e contas
def lerite():
    nome = nomee11ntry.get()
    contas1 = str("contas")
    
    cursor = banco.cursor()
    comando_sql = f'SELECT nome  FROM funcionarios  WHERE nome ="{nome}";'
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    banco.commit()
    
    if len(resultado) != 0 :
        cursor = banco.cursor()
        comando = f'SELECT profisão FROM funcionarios WHERE nome = "{nome}"'#profisão
        cursor.execute(comando)
        cargo = cursor.fetchall()
        data = date.today()

        cursor = banco.cursor()
        comando1 = f'SELECT SUM(valor) FROM {nome} ;'
        cursor.execute(comando1)
        saldo = cursor.fetchall() [0] [0]
        valor = (float(saldo))

        comando2 = f'SELECT SUM(valor) FROM {nome}{contas1};'
        cursor.execute(comando2)
        debito = cursor.fetchall() [0][0]
        conta = float(debito)

        comando3 = f' SELECT porcentagem FROM funcionarios WHERE nome = "{nome}" ;'
        cursor.execute(comando3)
        porcentagem = cursor.fetchall()[0][0]
        p = float(porcentagem)

        total = (valor * p - conta)
        total1 = str(total)

        data1 = str(data)
        cargo1 = str(cargo)
        total1 = str(total)
        salario1 = str(valor)
        dividas1 = str(conta)
      
      
        recibo1 = [ #recibo1
        ["DUFF HAUS","CNPJ:46.277.635/0001-31"],
        [ "DATA" , "NOME", "CARGO", "VALORES"], 
        [data1,nome,cargo1,""], 
        [data1,"Salario","","R$ "+salario1], 
        [data1,"Divida","","R$ "+dividas1], 
        ["Total","","","R$ "+total1],
        ["","","",""],
        ["ass. funcionario: ____________________","carimbo : ________________________"]
        ] 
        pdf = SimpleDocTemplate( f'Recibo {nome}.pdf' , pagesize = A4 ) 
        styles = getSampleStyleSheet() 
        title_style = styles[ "Heading1" ] 
        title_style.alignment = 1
        title = Paragraph( "Comprovante de Pagamento" , title_style ) 
        
        style = TableStyle( 
            [ 
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
        ] 
        ) 

        recibo2 = [ #recibo1
        ["DUFF HAUS","CNPJ:46.277.635/0001-31"],
        [ "DATA" , "NOME", "CARGO", "VALORES"], 
        [data1,nome,cargo1,""], 
        [data1,"Salario","","R$ "+salario1], 
        [data1,"Divida","","R$ "+dividas1], 
        ["Total","","","R$ "+total1],
        ["","","",""],
        ["ass. funcionario: ____________________","carimbo : ________________________"]
        ] 
        pdf = SimpleDocTemplate( f'Recibo {nome}.pdf' , pagesize = A4 ) 
        styles = getSampleStyleSheet() 
        title_style = styles[ "Heading1" ] 
        title_style.alignment = 1
        title = Paragraph( "Comprovante de Pagamento" , title_style ) 
        
        style1 = TableStyle( 
            [ 
            ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ), 
            ( "GRID" , ( 0, 0 ), ( 4 , 4 ), 1 , colors.black ), 
            ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ), 
            ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ), 
            ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ), 
            ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ), 
        ] 
        ) 
        table = Table( recibo1,style = style  )
        table2 = Table(recibo2,style = style1)  
        pdf.build([ title , table,table2 ]) 
        messagebox.showinfo('Sucess',f'lerite do funcionario(a) {nome} gerado com sucesso!')
    else:
        messagebox.showinfo('Fail','Erro ao encontrar o funcionario(a)!')
def imp_sim():
    nome = nomee11ntry.get()
    contas1 = str("contas")

    cursor = banco.cursor()
    comando_sql = f'SELECT nome  FROM funcionarios  WHERE nome ="{nome}";'
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    banco.commit()
    
    if len(resultado) != 0 :
        cursor4 = banco.cursor() 
        cursor4.execute(f'SELECT SUM(valor) FROM {nome}{contas1}')#divida
        valor1 = cursor4.fetchall()[0][0]
        dividas = str(valor1)
        cursor4.execute(f'SELECT * FROM {nome} ORDER BY id')#pdf
        dados_lidos1=cursor4.fetchall()
        banco.commit()
        # dados lidos = soma de jeff

        pdf = canvas.Canvas(f'Serviços {nome}.pdf')
        y = 0
        pdf.drawString(200,800, "Serviços Feito:")#PARTE SERVIÇOS
        pdf.setFillColor(HexColor('#807c00'))
        pdf.setFillColor(HexColor('#ff291f'))
        pdf.drawString(350,765, "Dividas Total =  "+ dividas)
        pdf.setFillColor(HexColor('#000000'))
        
        pdf.drawString(75,750, "ID |")
        pdf.drawString(110,750, "|SERVIÇOS")
        pdf.drawString(180,750, "|VALORES")
        pdf.drawString(250,750, "|PAGAMENTOS")
        pdf.drawString(350,750, "|PARCELAS")
        pdf.drawString(430,750, "|DATAS")

        

        for i in range(0, len(dados_lidos1)):#0 = de onde começa a desenha o banco
            y = y + 13
            pdf.setFillColor(HexColor('#363636'))

            #363636
            pdf.drawString(75,750 - y,str(dados_lidos1[i][0]))#ids
            pdf.drawString(110,750 - y,str(dados_lidos1[i][1]))#serviços
            pdf.drawString(180,750 - y,str(dados_lidos1[i][2]))#valores
            pdf.drawString(250,750 - y,str(dados_lidos1[i][3]))#pagamentos
            pdf.drawString(350,750 - y,str(dados_lidos1[i][4]))#parcelas
            pdf.drawString(430,750 - y,str(dados_lidos1[i][5]))#datas
            if i  == 56:
                pdf.showPage()
                for i in range(57, len(dados_lidos1)):
                    y = y + 13
                    pdf.drawString(75,1550 - y,str(dados_lidos1[i][0]))#ids
                    pdf.drawString(110,1550 - y,str(dados_lidos1[i][1]))#clientes
                    pdf.drawString(180,1550 - y,str(dados_lidos1[i][2]))#serviços
                    pdf.drawString(250,1550 - y,str(dados_lidos1[i][3]))#valores
                    pdf.drawString(350,1550 - y,str(dados_lidos1[i][4]))#datas
                    pdf.drawString(430,750 - y,str(dados_lidos1[i][5]))#datas

        pdf.save()

        cursor5 = banco.cursor() 
        cursor5.execute(f'SELECT SUM(valor) FROM {nome}{contas1}')#divida
        valor2 = cursor5.fetchall()[0][0]
        dividas1 = str(valor2)
        cursor5.execute(f'SELECT * FROM {nome}{contas1} ORDER BY id')#pdf
        dados_lidos2=cursor5.fetchall()
        banco.commit()
        # dados lidos = soma de jeff

        pdf = canvas.Canvas(f'Dividas {nome}.pdf')
        y = 0
        pdf.drawString(200,800, "Serviços Feito:")#PARTE SERVIÇOS
        pdf.setFillColor(HexColor('#807c00'))
        pdf.setFillColor(HexColor('#ff291f'))
        pdf.drawString(350,765, "Dividas Total =  "+ dividas1)
        pdf.setFillColor(HexColor('#000000'))
        
        pdf.drawString(75,750, "ID|")
        pdf.drawString(110,750, "|PRODUTOS ")
        pdf.drawString(200,750, "|VALORES")
        pdf.drawString(350,750, "|QUANTIDADE ")
        pdf.drawString(450,750, "|DATAS ")

        

        for i in range(0, len(dados_lidos2)):#0 = de onde começa a desenha o banco
            y = y + 13
            pdf.setFillColor(HexColor('#363636'))

            #363636
            pdf.drawString(75,750 - y,str(dados_lidos2[i][0]))#ids
            pdf.drawString(110,750 - y,str(dados_lidos2[i][1]))#clientes
            pdf.drawString(200,750 - y,str(dados_lidos2[i][2]))#serviços
            pdf.drawString(350,750 - y,str(dados_lidos2[i][3]))#valores
            pdf.drawString(450,750 - y,str(dados_lidos2[i][4]))#valores

            if i  == 56:
                pdf.showPage()
                for i in range(57, len(dados_lidos1)):
                    y = y + 13
                    pdf.drawString(75,1550 - y,str(dados_lidos2[i][0]))#ids
                    pdf.drawString(110,1550 - y,str(dados_lidos2[i][1]))#clientes
                    pdf.drawString(200,1550 - y,str(dados_lidos2[i][2]))#serviços
                    pdf.drawString(350,1550 - y,str(dados_lidos2[i][3]))#valores
                    pdf.drawString(450,1550 - y,str(dados_lidos2[i][4]))#valores

        pdf.save()
        messagebox.showinfo('Sucess',f'Pdfs do(a) funcionario(a) {nome} gerados com sucesso!')
    else:
        messagebox.showinfo('Fail','Funcionario(a) não encontrado!')
def pesquisa_total():
    
    nome = nomee11ntry.get()
    contas1 = str("contas")
    
    cursor = banco.cursor()
    comando_sql = f'SELECT nome  FROM funcionarios  WHERE nome ="{nome}" ;'
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    banco.commit()
    
    if len(resultado) != 0 :
        cursor = banco.cursor()
        comando1 = f'SELECT SUM(valor) FROM {nome}'
        cursor.execute(comando1)

        saldo = cursor.fetchall() [0] [0]
        valor = (float(saldo))
        comando2 = f'SELECT SUM(valor) FROM {nome}{contas1}'
        cursor.execute(comando2)
        debito = cursor.fetchall() [0][0]
        conta = float(debito)
        comando3 = f' SELECT porcentagem FROM funcionarios WHERE nome = "{nome}" '
        cursor.execute(comando3)
        porcentagem = cursor.fetchall()[0][0]

        p = float(porcentagem)
        total = (valor * p - conta)
        total1 = str(total)
        
        totalLabel = Label(window14,text=total1,font="Georgia 30 bold",bg='yellow')
        totalLabel.place(x=600,y=400)
        
        textsaldo = Label(window14,text='Saldo',font="Georgia 15",bg='turquoise')
        textsaldo.place(x=200,y=300)
        saldoLabel = Label(window14,text=saldo,font="Georgia 30 bold",bg='Green')
        saldoLabel.place(x=200,y=400)
                
        textdebito = Label(window14,text='| Divida',font="Georgia 15",bg='turquoise')
        textdebito.place(x=350,y=300)
                
        debitoLabel = Label(window14,text=debito,font="Georgia 30 bold",bg='Red')
        debitoLabel.place(x=350,y=400)
                
        textporc = Label(window14,text='| %',font="Georgia 15",bg='turquoise')
        textporc.place(x=480,y=300)

        porcentagemLabel = Label(window14,text=porcentagem,font="Georgia 30 bold",bg='orange')
        porcentagemLabel.place(x=480,y=400)

                
        texttotal = Label(window14,text='| Total',font="Georgia 15",bg='turquoise')
        texttotal.place(x=580,y=300)
    else:
        messagebox.showinfo('Fail','Funcionario(a) não encontrado!')
def volta_total():
    home()
    window14.destroy()
def total():
    global window14,nomee11ntry
    window14 = Tk()
    window14.geometry("1350x800")
    window14.title("Sistema de Vendas - HTec")
    window14.configure(background="turquoise")
    
    nomelab1el = Label(window14,text="Nome do Funcionario :",font="Georgia 10 bold",background="turquoise")
    nomelab1el.place(x=5,y=100)
    
    func = StringVar() 
    nomee11ntry = ttk.Combobox(window14, width = 27, textvariable = func) 
    nomee11ntry['values'] = ('Marllon','Jefferson','Walterlenia') 
    nomee11ntry.current()     
    nomee11ntry.place(x=200, y=100) 
     
    pesquisar1 = Button(window14,text="Pesquisar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=pesquisa_total)
    pesquisar1.place(x=400,y=90)
    
    voltar = Button(window14,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_total)
    voltar.place(x=1100,y=300)
    
    imp = Button(window14,text="Imprimir",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=imp_sim)
    imp.place(x=1100,y=350)

    lerite1 = Button(window14,text="Lerite",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=lerite)
    lerite1.place(x=1100,y=400)
    window7.destroy()
#mostra um resumo financeiro mensal do funcionario em forma de grafico, tem a opção de salvar imagem
def mostra_valores():
    #definindo valores 
    nome = nomee11ntry.get()
    contas1 = str("contas")

    
    #faz a plotagem
    if nome != 0:

        import matplotlib.pyplot as plt
        import numpy as np
        cursor = banco.cursor()
        comando = f'SELECT SUM(valor) FROM {nome}'
        cursor.execute(comando)
        positivo = float(cursor.fetchall() [0] [0])

        comando1 = f'SELECT SUM(valor) FROM {nome}{contas1}'
        cursor.execute(comando1) 
        negativo = float(cursor.fetchall()[0] [0])


        votos = np.array([negativo, positivo])
        candi = ['Divida', 'Saldo']
        cores=['red', 'green']
        explode = (0.1, 0)
        plt.title(f'Rendimento do Funcionario {nome}')
        plt.pie(votos, explode=explode, labels=votos, colors=cores, autopct='%1.2f%%', shadow=True, startangle=90)
        plt.legend(candi, bbox_to_anchor=(1.3, 1.3),loc='upper right')
        plt.axis('equal')
        plt.show()
    
    else:
        messagebox.showinfo('Fail','funcionario não encontrado!')
def volta_resumo():
    home()
    window13.destroy()
def resumo_financeiro():
    global window13,nomee11ntry
    window13 = Tk()
    window13.geometry("1350x800")
    window13.title("Sistema de Vendas - HTec")
    window13.configure(background="turquoise")
    
    nomelab1el = Label(window13,text="Nome do Funcionario :",font="Georgia 10 bold",background="turquoise")
    nomelab1el.place(x=5,y=100)
    func = StringVar() 
    nomee11ntry = ttk.Combobox(window13, width = 27, textvariable = func) 
    nomee11ntry['values'] = ('Marllon','Jefferson','Walterlenia') 
    nomee11ntry.current() 
    nomee11ntry.place(x=200,y=100)
     
    pesquisar1 = Button(window13,text="Pesquisar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=mostra_valores)
    pesquisar1.place(x=400,y=90)
    
    voltar = Button(window13,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_resumo)
    voltar.place(x=1100,y=300)
    window7.destroy()
#
def pesquisar():
    global func1,contas2
    func1 = nomee1ntry.get()
    contas2 = str("contas")
    cf.delete(*cf.get_children())
    cursor = banco.cursor()
    cursor.execute(f'SELECT * FROM {func1}{contas2} ORDER BY id ;')
    linhas = cursor.fetchall()
    for i in linhas:
        cf.insert("","end",values = i)
def deletar_conta_func():
    vid=-1
    itemselecionado = cf.selection()[0]
    valores = cf.item(itemselecionado,"values")
    vid = valores[0]
    try:
        cursor = banco.cursor()
        cursor.execute(f'DELETE FROM {func1}{contas2} WHERE id ='+ vid)
        messagebox.showinfo("Sucess","Item deletado com sucesso")
    except:
        messagebox.showinfo("ERRO","Item não foi deletado!")
        return
    cf.delete(itemselecionado)
def volta_conta_func():
    home()
    window12.destroy()
def contas_funcionarios():
    global window12,nomee1ntry
    window12 = Tk()
    window12.geometry("1350x800")
    window12.title("Sistema de Vendas - HTec")
    window12.configure(background="turquoise")
    
    nomelab1el = Label(window12,text="Nome do Funcionario :",font="Georgia 10 bold",background="turquoise")
    nomelab1el.place(x=5,y=100)
    func = StringVar() 
    nomee1ntry = ttk.Combobox(window12, width = 27, textvariable = func) 
    nomee1ntry['values'] = ('Marllon','Jefferson','Walterlenia') 
    nomee1ntry.current()     
    nomee1ntry.place(x=200, y=100) 
     
    pesquisar1 = Button(window12,text="Pesquisar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=pesquisar)
    pesquisar1.place(x=400,y=90)

    deletar1 = Button(window12,text="Deletar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=deletar_conta_func)
    deletar1.place(x=620,y=90)
    
    voltar = Button(window12,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_conta_func)
    voltar.place(x=1100,y=300)
    
    grid = LabelFrame(window12,text="Historico de Contas",width=500)
    grid.place(x=250,y=250)

    global cf

    cf = ttk.Treeview(grid,columns=('id','produlto','valor','quantidade','data'),show='headings')
    cf.column('id',minwidth=0,width=50)
    cf.column('produlto',minwidth=0,width=150)
    cf.column('valor',minwidth=0,width=150)
    cf.column('quantidade',minwidth=0,width=150)
    cf.column('data',minwidth=0,width=150)


    cf.heading('id',text='Id')
    cf.heading('produlto',text='Produlto')
    cf.heading('valor',text='Valor')
    cf.heading('quantidade',text='Quantidade')
    cf.heading('data',text='Data')
    cf.pack(padx=70,pady=50)
    window7.destroy()
# cria as tables de contas e salarios de cada funcionario tambem as apagas
def salva_func():
    func = nomeentry.get()
    sobrefunc = sobrenomeentry.get()
    prof = profisaoentry.get()
    porcentagem = pagamentoentry.get()
    contas1 = str("contas")
    if func and sobrefunc and prof and porcentagem != 0:
        cursor = banco.cursor()
        comandosal = f'Create table {func}(id int not null auto_increment,serviço varchar(255) not null,valor varchar(255) not null,pagamento varchar(255) not null,parcela varchar(255) not null,data varchar(255) not null,primary key(id));'
        cursor.execute(comandosal)
        comandocon = f'Create table {func}{contas1}(id int not null auto_increment,produlto varchar(255) not null,valor varchar(255) not null,quantidade varchar(255) not null,data varchar(255) not null,primary key(id));'
        cursor.execute(comandocon)
        comandofunc = "insert into funcionarios(nome,sobrenome,profisão,porcentagem) values(%s,%s,%s,%s);"
        dados = (func,sobrefunc,prof,porcentagem)
        cursor.execute(comandofunc,dados)
        banco.commit()
        messagebox.showinfo('Sucess',f'Funcionario {func}  {sobrefunc} salvo com sucesso!')
    else:
        messagebox.showinfo('Fail','Erro ao salvar o funcionario')
def volta_func():
    home()
    window11.destroy()
def mostra_func():
        f.delete(*f.get_children())
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM funcionarios ORDER BY id ;")
        linhas = cursor.fetchall()
        for i in linhas:
            f.insert("","end",values = i)
def apaga_func():
    cnt = 'contas'
    vid=-1
    itemselecionado = f.selection()[0]
    valores = f.item(itemselecionado,"values")
    vid = valores[0]
    nome = valores[1]
    try:
        cursor = banco.cursor()
        cursor.execute(f'Drop table {nome},{nome+cnt};')
        cursor.execute(f'DELETE FROM funcionarios WHERE id ='+ vid)
        messagebox.showinfo("Sucess","Item deletado com sucesso")
    except:
        messagebox.showinfo("ERRO","Item não foi deletado!")
        return
    
    f.delete(itemselecionado)
def add_funcionarios():

    global window11,nomeentry,sobrenomeentry,profisaoentry,pagamentoentry
    window11 = Tk()
    window11.geometry("1350x800")
    window11.title("Sistema de Vendas - HTec")
    window11.configure(background="turquoise")

    #labels e opções de func e serviços
    nomelabel = Label(window11,text="Nome :",font="Georgia 10 bold",background="turquoise")
    nomelabel.place(x=5,y=100)
    nomeentry = Entry(window11,font="Georgia 10",background="LightBlue")
    nomeentry.place(x=100, y=100)

    sobrenomelabel = Label(window11,text="Sobrenome :",font="Georgia 10 bold",background="turquoise")
    sobrenomelabel.place(x=320,y=100)
    sobrenomeentry = Entry(window11,font="Georgia 10",bg="lightblue")
    sobrenomeentry.place(x=421,y=100)

    prof = StringVar() 
    profisaoentry = ttk.Combobox(window11, width = 27, textvariable = prof) 
    profisaoentry['values'] = ('Cabelereiro','Massoterapeuta','Manicure', 'Nail Designer' ,'Maquiador' ,'Depilador') 
    profisaoentry.current()
    profisaoentry.place(x=650, y=100)

    pag = StringVar() 
    pagamentoentry = ttk.Combobox(window11, width = 27, textvariable = pag) 
    pagamentoentry['values'] = ('0.15','0.20','0.25','0.30','0.35','0.40','0.45','0.50','0.55','0.60','0.65','0.70','0.75') 
    pagamentoentry.current()
    pagamentoentry.place(x=850, y=100)

    addcfunc = Button(window11,text="Salvar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=salva_func)
    addcfunc.place(x=1000,y=300)

    voltacr = Button(window11,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_func)
    voltacr.place(x=1000,y=350)
    
    exclui = Button(window11,text="Deletar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=apaga_func)
    exclui.place(x=1000,y=400)

    quadrogrid = LabelFrame(window11,text="Funcionarios",width=500)
    quadrogrid.place(x=100,y=250)

    global f

    f = ttk.Treeview(quadrogrid,columns=('id','nome','sobrenome','profisao','porcentagem'),show='headings')
    f.column('id',minwidth=0,width=100)
    f.column('nome',minwidth=0,width=150)
    f.column('sobrenome',minwidth=0,width=150)
    f.column('profisao',minwidth=0,width=150)
    f.column('porcentagem',minwidth=0,width=150)


    f.heading('id',text='ID')
    f.heading('nome',text='Nome')
    f.heading('sobrenome',text='Sobrenome')
    f.heading('profisao',text='Profisão')
    f.heading('porcentagem',text='Porcentagem')
    f.pack(padx=70,pady=50)
    mostra_func()
    
    window7.destroy()
# salva as contas dos funcionarios
def salva_contas():
    funcionario = contasfunc.get()
    produlto = contasprod.get()
    valor = contasvalor.get()
    quantidade = prod.get()
    data = date.today()
    if funcionario and produlto and valor != 0:
        cursor = banco.cursor()
        comando5 = f'INSERT INTO {funcionario+"contas"}(produlto,valor,quantidade,data) VALUES (%s,%s,%s,%s) '
        dados = (produlto,valor,quantidade,data)
        cursor.execute(comando5,dados)
        messagebox.showinfo('Sucess','Conta salva com sucesso!')
    else:
        messagebox.showinfo('Fail','Conta não salva!')
def volta_menu1():
    window10.destroy()
    home()
def refresh1():
    window10.destroy()
    contas()
def contas():
    global window10,contasvalor,contasfunc,contasprod,prod
    window10 = Tk()
    window10.geometry("1350x800")
    window10.title("Sistema de Vendas - HTec")
    window10.configure(background="turquoise")

    #labels e opções de func e serviços
    c = StringVar() 
    contasvalor = ttk.Combobox(window10, width = 27, textvariable = c) 
    contasvalor['values'] = ('10,00','20,00','30,00', '40,00' ,'50,00' ,'60,00' ,'70,00', '80,00' ,'90,00' ,'100,00','110,00') 
    contasvalor.current()
    contasvalor.place(x=50, y=100)

    f = StringVar() 
    contasfunc = ttk.Combobox(window10, width = 27, textvariable = f) 
    contasfunc['values'] = ('Jefferson','Walterlenia','Marllon') 
    contasfunc.current()
    contasfunc.place(x=250,y=100)
    

    p = StringVar() 
    contasprod = ttk.Combobox(window10, width = 27, textvariable = p) 
    contasprod['values'] = ('Tinta','Esmalte') 
    contasprod.current()    
    contasprod.place(x=450,y=100)

    q = StringVar() 
    prod = ttk.Combobox(window10, width = 27, textvariable = q) 
    prod['values'] = ('1','2','3','4','5','6','7','8','9','10') 
    prod.current()    
    prod.place(x=650,y=100)


    

    addcfunc = Button(window10,text="Salvar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=salva_contas)
    addcfunc.place(x=1000,y=300)

    voltacr = Button(window10,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_menu1)
    voltacr.place(x=1000,y=350)
    window7.destroy()
#salva e cadastra novo usuario para o loguin
def funções_newusers():
    
    new = nomeentry.get()
    senha1 = senhaentry2.get()
    senha2 = confirmentry.get()
    if senha1 == senha2:
        cursor = banco.cursor()
        comando_sql = "INSERT INTO login (nome,senha) VALUES (%s,%s);"
        dados = (new,senha1)
        cursor.execute(comando_sql,dados)
        banco.commit()
        messagebox.showinfo('New user','Usuario salvo com sucesso!')
    else:
        messagebox.showinfo('As senhas não são iguais','Usuario não foi salvo!')
def volta_n():
    window2.destroy()
    inicio()
def newuser():
    global window2
    window2 = Tk()
    window2.geometry("1350x800")
    window2.title("Novo Usuario")
    window2.configure(background="turquoise")
    global nomeentry,senhaentry2,confirmentry 
    nomeentry = StringVar()#new user
    senhaentry2 = StringVar()#new User
    confirmentry = StringVar()#new user
    #y=linha x=coluna
    label = Label(window2,text="Novo Usuario",font="Georgia 20 bold",bg="turquoise")
    label.place(x=300,y=250)
    nomelabel = Label(window2,text="Nome :",font="Georgia 20",bg="turquoise")
    nomelabel.place(x=200,y=300)
    nomeentry = Entry(window2,font="Georgia 20 ",bg="LightBlue")
    nomeentry.place(x=300,y=300)
    senhalabel2 = Label(window2,font="Georgia 20",bg="turquoise",text="Senha:")
    senhalabel2.place(x=200, y=400)
    senhaentry2 = Entry(window2,font="Georgia 20",bg="LightBlue")
    senhaentry2.place(x=300,y=400)
    confirmlabel= Label(window2,font="Georgia 20",bg="turquoise",text="Confirme:")
    confirmlabel.place(x=150,y=500)
    confirmentry = Entry(window2,font="Georgia 20",show="*",bg="LightBlue")
    confirmentry.place(x=300,y=500)
    botaosalvar=Button(window2,text="Salvar",width=42,height=2,font="Georgia 10",bg="PowderBlue",command=funções_newusers)
    botaosalvar.place(x=50,y=600)
    botaovoltar=Button(window2,text="Voltar",width=42,height=2,font="Georgia 10",bg="PowderBlue",command=volta_n)
    botaovoltar.place(x=450,y=600)
    window.destroy()
#realiza vendas, guarda dados, fazer sangria abertura e fecha de caixa
def verifica_cx():
    gerencia = adm.get()
    valor_ex = entrycx.get()
    cursor = banco.cursor()
    comando = "Select sum(valor) from dinheiro"
    cursor.execute(comando)
    valor = cursor.fetchall() [0] [0]
    
    if valor != valor_ex and gerencia != '26' :
        messagebox.showinfo('Fail','Valor de caixa errado')

    else:
            messagebox.showinfo('Sucess','caixa aberto')
            caix.destroy()
def abrir_caixa():
    global caix
    caix = Tk()
    caix.geometry('400x400')
    caix.configure(background="white")
    global entrycx,adm
    label = Label(caix,text='Valor existente :',font="Georgia 20",bg="white")
    label.place(x=50,y=50)
    entrycx = Entry(caix,font="Georgia 10 ",bg="LightBlue")
    entrycx.place(x=50,y=100)
    label1= Label(caix,text='Senha Gerencial :',font="Georgia 20",bg="white")
    label1.place(x=50,y=150)
    adm = Entry(caix,font="Georgia 10 ",bg="LightBlue",show='*')
    adm.place(x=50,y=200)
    abrir = Button(caix,text='Abrir',bg='Green',command=verifica_cx)
    abrir.place(x=50,y=250)
def verifica_fch_cx():
    resultado = entrycx1.get()
    senha = adm1.get()
    cursor = banco.cursor()
    comando = 'select sum(valor) from dinheiro;'
    cursor.execute(comando)
    valor = cursor.fetchall()[0][0]
    if valor != resultado and senha != '26':
        messagebox.showinfo('Faill','Valores Errados')
    else:
        messagebox.showinfo('Sucess','Valores Corretos')
def sangria():
    valor = str(entrysang.get())
    adm = str(entrysangadm.get())
    if adm == "26":
        cursor = banco.cursor()
        comando = 'drop table dinheiro;'
        cursor.execute(comando)
        comando2 = 'create table dinheiro(id int not null auto_increment,valor varchar(255) not null,primary key(id));'
        cursor.execute(comando2)
        comando3 =f'INSERT INTO dinheiro(valor) VALUES("{valor}");'
        cursor.execute(comando3)
        messagebox.showinfo('Sucess',f'Sangria realizada com sucesso, valor {valor}')
    else:
        messagebox.showinfo('Fail','Senha errada')
def tela_sangria():
    global entrysangadm,entrysang
    sang = Tk()
    sang.geometry('400x400')
    sang.configure(background='turquoise')

    label = Label(sang,text='Valor Existente :')
    label.place(x=10,y=10)

    entrysang = Entry(sang)
    entrysang.place(x=100,y=10)

    labeladm = Label(sang,text='Senha Gerencial :')
    labeladm.place(x=10,y=30)

    entrysangadm = Entry(sang,show='*')
    entrysangadm.place(x=100,y=30)

    button = Button(sang,text='Salvar',command=sangria)
    button.place(x=300,y=10)
def fechar_caixa():
    global caix1,entrycx1,adm1
    caix1 = Tk()
    caix1.geometry('400x400')
    caix1.configure(background="white")
    global entrycx1,adm1
    label1 = Label(caix1,text='Valor existente :',font="Georgia 20",bg="white")
    label1.place(x=50,y=50)
    entrycx1 = Entry(caix1,font="Georgia 10 ",bg="LightBlue")
    entrycx1.place(x=50,y=100)
    label1= Label(caix1,text='Senha Gerencial :',font="Georgia 20",bg="white")
    label1.place(x=50,y=150)
    adm1 = Entry(caix1,font="Georgia 10 ",bg="LightBlue",show='*')
    adm1.place(x=50,y=200)
    abrir1 = Button(caix1,text='Fechar',bg='red',command=verifica_fch_cx)
    abrir1.place(x=50,y=250)
def dinheiro():
    valor = str(total1.get())
    pagamento = typemoney.get()
    if pagamento == 'Dinheiro':
        cursor = banco.cursor()
        comando =f'INSERT INTO dinheiro(valor) VALUES("{valor}");'
        cursor.execute(comando)
        banco.commit()
def salva_vendas():
    funcionario = str(typefunc.get())
    serviços = str(typeservice.get())
    valor = str(total1.get())
    data = str(date.today())
    pagamento = str(typemoney.get())
    parcelas = str(typeparc.get())

    if funcionario and valor and serviços and parcelas != 0:
        cursor = banco.cursor()
        comando_sql = f'INSERT INTO {funcionario}(serviço,valor,pagamento,parcela,data) VALUES (%s,%s,%s,%s,%s);'
        dados = (serviços,valor,pagamento,parcelas,data)
        cursor.execute(comando_sql,dados)
        comando_sql1 = "INSERT INTO caixa(funcionario,serviço,valor,pagamento,parcela,data) VALUES (%s,%s,%s,%s,%s,%s);"
        dados = (funcionario,serviços,valor,pagamento,parcelas,data)
        cursor.execute(comando_sql1,dados)
        dinheiro()
        messagebox.showinfo('Sucess',f'Salvo\n func = {funcionario},\nvalor = {valor},\nservice = {serviços},\ndata = {data} !')        
    
    else:
        messagebox.showinfo('Fail','erro ao salvar os dados')
def popular():
    tv.delete(*tv.get_children())
    cursor = banco.cursor()
    cursor.execute("SELECT * FROM caixa ORDER BY id ;")
    linhas = cursor.fetchall()
    for i in linhas:
        tv.insert("","end",values = i)
def volta_menu():
    window1.destroy()
    home()
def vendas():
    global window1,total1,typefunc,typeservice,typemoney,typeparc
    window1 = Tk()
    window1.geometry("1350x800")
    window1.title("Sistema de Vendas - HTec")
    window1.configure(background="turquoise")

    #labels e opções de func e serviços
    t = StringVar() 
    total1 = ttk.Combobox(window1, width = 27, textvariable = t) 
    total1['values'] = ('10,00','20,00','30,00', '40,00' ,'50,00' ,'60,00' ,'70,00', '80,00' ,'90,00' ,'100,00','110,00') 
    total1.current()
    total1.place(x=50, y=100)

    f = StringVar() 
    typefunc = ttk.Combobox(window1, width = 27, textvariable = f) 
    typefunc['values'] = ('Jefferson','Walterlenia','Marllon') 
    typefunc.place(x=250,y=100)
    typefunc.current()

    s = StringVar() 
    typeservice = ttk.Combobox(window1, width = 27, textvariable = s) 
    typeservice['values'] = ('hidratação',
'escova',
'cauterização',
'corte fem',
'coloração',
'mechas',
'blindagem',
'Botox',
'progressiva',
'penteados',
'recons/ elástico',
'esm/Gel',
'banho de Gel',
'blindagem',
'manicure',
'pedicure',
'manutenção',
'maquiagem cilios',
'maquiagem',
'sobrancelha',
'limpeza pele',
'extensao cilios',
'relaxante',
'bambuterapia',
'modeladora',
'spa',
'plastica d/pes',
'ventosaterapia',
'axila',
'buço',
'meia perna',
'virilha',
'perna compl.',
'glúteos',
'perianal',
'corpo inteiro',
'peito/barriga'

) 
    typeservice.place(x=450,y=100) 
    typeservice.current() 

    n = StringVar() 
    typemoney = ttk.Combobox(window1, width = 27, textvariable = n) 
    typemoney['values'] = ('Debito','Credito','Dinheiro','Pix') 
    typemoney.place(x=650,y=100) 
    typemoney.current()

    parcela = StringVar() 
    typeparc = ttk.Combobox(window1, width = 27, textvariable = parcela) 
    typeparc['values'] = ('1x','2x','3x') 
    typeparc.place(x=850,y=100) 
    typeparc.current() 

    caixa = Button(window1,text='Abrir Caixa',bg="Green",width=26,height=2,font="Georgia 10",command=abrir_caixa)
    caixa.place(x=1050,y=100)

    fchcaixa = Button(window1,text='Fechar Caixa',bg="Red",width=26,height=2,font="Georgia 10",command=fechar_caixa)
    fchcaixa.place(x=1050,y=150)
    
    sangria = Button(window1,text='Sangria',bg="orange",width=26,height=2,font="Georgia 10",command=tela_sangria)
    sangria.place(x=1050,y=200)

    addfunc = Button(window1,text="Salvar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=salva_vendas)
    addfunc.place(x=800,y=600)

    voltar = Button(window1,text="Voltar",bg="PowderBlue",width=26,height=2,font="Georgia 10",command=volta_menu)
    voltar.place(x=1030,y=600)
    
    quadrogrid = LabelFrame(window1,text="Historico",width=500)
    quadrogrid.place(x=100,y=250)

    global tv

    tv = ttk.Treeview(quadrogrid,columns=('id','funcionario','serviço','valor','pagamento','parcela','data'),show='headings')
    tv.column('id',minwidth=0,width=100)
    tv.column('funcionario',minwidth=0,width=150)
    tv.column('serviço',minwidth=0,width=150)
    tv.column('valor',minwidth=0,width=150)
    tv.column('pagamento',minwidth=0,width=150)
    tv.column('parcela',minwidth=0,width=150)
    tv.column('data',minwidth=0,width=150)



    tv.heading('id',text='Id')
    tv.heading('funcionario',text='Funcionario')
    tv.heading('serviço',text='Serviço')
    tv.heading('valor',text='Valor')
    tv.heading('pagamento',text='Pagamento')
    tv.heading('parcela',text='Parcela')
    tv.heading('data',text='Data')
    tv.pack(padx=70,pady=50)
    popular()
    window7.destroy()
# casa home/ mapa de funções
def home():
    global window7
    window7 = Tk()
    window7.geometry("1350x800")
    window7.title("Novo Usuario")
    window7.configure(background="turquoise")

    botaoreceber=Button(window7,text="Receber",font="Georgia 20 bold",bg="dark green", command=vendas)
    botaoreceber.place(x=750,y=50,width=500,height=200)
    botaopagar=Button(window7,text="Pagar",font="Georgia 20 bold",bg="red",command=contas)
    botaopagar.place(x=100,y=50,width=500,height=200)
    botaoclientes=Button(window7,text="Funcionarios",font="Georgia 20 bold" , bg="blue",command=add_funcionarios)
    botaoclientes.place(x=100,y=252,width=500,height=200)
    
    botaofinanças=Button(window7,text="Resumo Financeiro",font="Georgia 20 bold" , bg="orange",command=resumo_financeiro)
    botaofinanças.place(x=750,y=252,width=500,height=200)

    botaocontas=Button(window7,text="Contas Funcionario",font="Georgia 20 bold" , bg="yellow",command= contas_funcionarios)
    botaocontas.place(x=100,y=455,width=500,height=200)

    botaofinanças=Button(window7,text="Total",font="Georgia 20 bold" , bg="Gray",command= total)
    botaofinanças.place(x=750,y=455,width=500,height=200)
# verifica senha e usuario
def login():
    user = loguinentry.get()
    password = senhaentry.get()
    print(user,password)

    cursor = banco.cursor()
    comando_sql = "SELECT nome and senha FROM login  WHERE nome ='{}' and senha = '{}';".format(user,password)
    cursor.execute(comando_sql)
    resultado = cursor.fetchall()
    banco.commit()
    
    if len(resultado) != 0 :
        home()
        window.destroy()
    else:
       messagebox.showinfo('ERRO','usuario ou senha errada')
def inicio():
    global window,loguinentry,senhaentry
    window = Tk()
    window.geometry("1350x800")
    window.title("Sistema de Vendas - HTec")
    window.configure(background="turquoise")
    loguinentry = StringVar()
    senhaentry = StringVar()
    bg = PhotoImage(file = "htec.png") 
    label1 = Label( window, image = bg) 
    label1.place(x = 800, y = 0)
    loguinlabel = Label(window,text = "Login:",font="Georgia 20 bold",background="turquoise")
    loguinlabel.place(x=200,y=200)
    loguinentry = Entry(window,font="Georgia 20",background="LightBlue")
    loguinentry.place(x=400,y=200)
    senhalabel = Label(window,text = "Password:",font="Georgia 20 bold",background="turquoise")
    senhalabel.place(x=200,y=300)
    senhaentry = Entry(window,show="*",font="Georgia 20",bg="LightBlue")
    senhaentry.place(x=400,y=300)
    loguinbutton = Button(window,text="Entrar",width=42,height=2,font="Georgia 10",command=login,bg="PowderBlue")
    loguinbutton.place(x= 100,y=500)
    Nuser = Button(window,text="Novo Usuario",width=42,height=2,font="Georgia 10",bg="PowderBlue",command=newuser)
    Nuser.place(x=450,y=500)
    window.mainloop()
inicio()

