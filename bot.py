#!/usr/bin/python3

from telegram.ext import CommandHandler, Updater
import psycopg2
import locale
from datetime import datetime

conn = psycopg2.connect(host="localhost", port=5432, database="nossosonho", user="postgres", password="postgres")
conn.autocommit = True
cur = conn.cursor()
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def guardarRendimentos(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /guardarRendimento'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /guardarRendimento'.format(dateNow,id,user), file=open("bot.log","a"))

    insert = False
    executeFunc = False

    try:
        if (len(context.args[0])>0):
            value_receiv = float(context.args[0])
            executeFunc=True
        else:
            executeFunc=False
    except:
        executeFunc=False


    if (executeFunc==True):
        query = "insert into investiments (code,name_code,valor,data_invest) values (nextval('investiments_code_seq'),3,%.2f,now())"%(value_receiv)
        cur.execute(query)
        insert = True
    else:
        mensagem = "Não foi possivel inserir o valor desejado!"
        insert = False
    
    if (insert==False):
        update.message.reply_text(mensagem)
    else:
        value_receiv = locale.currency(value_receiv, grouping=True, symbol=None)
        update.message.reply_text("Valor de R$"+value_receiv+" foi inserido para Rendimentos!")

def guardarBrenda(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /guardarBrenda'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /guardarBrenda'.format(dateNow,id,user), file=open("bot.log","a"))

    insert = False
    executeFunc = False    

    try:
        if (len(context.args[0])>0):
            value_receiv = float(context.args[0])
            executeFunc=True
        else:
            executeFunc=False
    except:
        executeFunc=False


    if (executeFunc==True):
        query = "insert into investiments (code,name_code,valor,data_invest) values (nextval('investiments_code_seq'),2,%.2f,now())"%(value_receiv)
        cur.execute(query)
        insert = True
    else:
        mensagem = "Não foi possivel inserir o valor desejado!"
        insert = False
    
    if (insert==False):
        update.message.reply_text(mensagem)
    else:
        value_receiv = locale.currency(value_receiv, grouping=True, symbol=None)
        update.message.reply_text("Valor de R$"+value_receiv+" foi inserido para a Brenda!")

def guardarFernando(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /guardarFernando'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /guardarFernando'.format(dateNow,id,user), file=open("bot.log","a"))

    insert = False
    executeFunc = False

    try:
        if (len(context.args[0])>0):
            value_receiv = float(context.args[0])
            executeFunc=True
        else:
            executeFunc=False
    except:
        executeFunc=False

    if (executeFunc==True):
        query = "insert into investiments (code,name_code,valor,data_invest) values (nextval('investiments_code_seq'),1,%.2f,now())"%(value_receiv)
        cur.execute(query)
        insert = True
    else:
        mensagem = "Não foi possivel inserir o valor desejado!"
        insert = False
    
    if (insert==False):
        update.message.reply_text(mensagem)
    else:
        value_receiv = locale.currency(value_receiv, grouping=True, symbol=None)
        update.message.reply_text("Valor de R$"+value_receiv+" foi inserido para o Fernando!")

    

def valorTotal(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /valorTotal'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /valorTotal'.format(dateNow,id,user), file=open("bot.log","a"))

    cur.execute("select sum(acc.valor),nom.name from investiments acc join nomes nom on (acc.name_code=nom.code) group by nom.name,nom.code order by nom.code")
    query_results = cur.fetchall()
    valorTotal = 0
    array_mensagem = []    

    if (len(query_results)==0):
        update.message.reply_text("Não há registros!")
    else:
        for row in query_results:
            valor = locale.currency(row[0], grouping=True, symbol=None)
            valorTotal = valorTotal + row[0]
            mensagem = "\n\n{nome} \nR$ {quantia}".format(nome=row[1],quantia=valor)
            array_mensagem.append(str(mensagem))

        valorTotal = locale.currency(valorTotal, grouping=True, symbol=None)
        array_mensagem.append("\n\nValor total\nR$ "+valorTotal)
        update.message.reply_text(''.join(array_mensagem))

def relacaoFernando(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /relacaoFernando'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /relacaoFernando'.format(dateNow,id,user), file=open("bot.log","a"))

    cur.execute("select acc.valor,nom.name,acc.data_invest from investiments acc join nomes nom on (acc.name_code=nom.code) where nom.code=1")
    query_results = cur.fetchall()
    valorTotal = 0
    array_mensagem = []
    array_mensagem.append("Resumo de Fernando")

    if (len(query_results)==0):
        update.message.reply_text("Não há registros!")
    else:
        for row in query_results:
            valor = locale.currency(row[0], grouping=True, symbol=None)
            valorTotal = valorTotal + row[0]
            mensagem = "\n\n{data}\nR$ {quantia}".format(data=row[2].strftime("%d/%m/%Y %H:%M"),quantia=valor)
            array_mensagem.append(str(mensagem))

        valorTotal = locale.currency(valorTotal, grouping=True, symbol=None)
        array_mensagem.append("\n\nValor total\nR$ "+valorTotal)
        update.message.reply_text(''.join(array_mensagem))

def relacaoBrenda(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /relacaoBrenda'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /relacaoBrenda'.format(dateNow,id,user), file=open("bot.log","a"))
    
    cur.execute("select acc.valor,nom.name,acc.data_invest from investiments acc join nomes nom on (acc.name_code=nom.code) where nom.code=2")
    query_results = cur.fetchall()
    valorTotal = 0
    array_mensagem = []
    array_mensagem.append("Resumo de Brenda")
    if(len(query_results)==0):
        update.message.reply_text("Não há registros!")
    else:
        for row in query_results:
            valor = locale.currency(row[0], grouping=True, symbol=None)
            valorTotal = valorTotal + row[0]
            mensagem = "\n\n{data}\nR$ {quantia}".format(data=row[2].strftime("%d/%m/%Y %H:%M"),quantia=valor)
            array_mensagem.append(str(mensagem))

        valorTotal = locale.currency(valorTotal, grouping=True, symbol=None)
        array_mensagem.append("\n\nValor total\nR$ "+valorTotal)
        update.message.reply_text(''.join(array_mensagem))


def relacaoMensal(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /relacaoMensal'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /relacaoMensal'.format(dateNow,id,user), file=open("bot.log","a"))
    
    cur.execute("select date_trunc('month',data_invest) as data_invest, sum(valor),name from investiments acc join nomes nom on (acc.name_code=nom.code) group by date_trunc('month',data_invest),name,name_code order by data_invest,acc.name_code;")
    query_results = cur.fetchall()
    cur.execute("select date_trunc('month',data_invest) as data_invest from investiments group by date_trunc('month',data_invest) order by data_invest;")
    query_date = cur.fetchall()
    valorTotal = 0
    array_mensagem = []
    array_mensagem.append("Resumo Mensal")
    if(len(query_results)==0):
        update.message.reply_text("Não há registros!")
    else:
        for row1 in query_date:
            array_mensagem.append("\n\n"+row1[0].strftime("%m/%Y"))
            for row in query_results:
                if (row1[0]==row[0]):
                    valor = locale.currency(row[1], grouping=True, symbol=None)
                    valorTotal = valorTotal + row[1]
                    mensagem = "\n{nome} - R$ {quantia}".format(nome=row[2],quantia=valor)
                    array_mensagem.append(str(mensagem))

        valorTotal = locale.currency(valorTotal, grouping=True, symbol=None)
        array_mensagem.append("\n\nValor total\nR$ "+valorTotal)
        update.message.reply_text(''.join(array_mensagem))

def retirarSonho(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /retirarSonho'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /retirarSonho'.format(dateNow,id,user), file=open("bot.log","a"))

    insert = False
    executeFunc = False

    try:
        if (len(context.args[0])>0):
            value_receiv = float(context.args[0])
            executeFunc=True
        else:
            executeFunc=False
    except:
        executeFunc=False

    if (executeFunc==True):
        query = "insert into investiments (code,name_code,valor,data_invest) values (nextval('investiments_code_seq'),4,%.2f,now())"%(value_receiv)
        cur.execute(query)
        insert = True
    else:
        mensagem = "Não foi possivel inserir o valor desejado!"
        insert = False
    
    if (insert==False):
        update.message.reply_text(mensagem)
    else:
        value_receiv = locale.currency(value_receiv, grouping=True, symbol=None)
        update.message.reply_text("Valor de R$"+value_receiv+" foi retirado para realização sonho!")

def relacaoRetirada(update,context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /relacaoRetirada'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /relacaoRetirada'.format(dateNow,id,user), file=open("bot.log","a"))
    
    cur.execute("select acc.valor,nom.name,acc.data_invest from investiments acc join nomes nom on (acc.name_code=nom.code) where nom.code=4")
    query_results = cur.fetchall()
    valorTotal = 0
    array_mensagem = []
    array_mensagem.append("Resumo de retiradas")
    if(len(query_results)==0):
        update.message.reply_text("Não há registros!")
    else:
        for row in query_results:
            valor = locale.currency(row[0], grouping=True, symbol=None)
            valorTotal = valorTotal + row[0]
            mensagem = "\n\n{data}\nR$ {quantia}".format(data=row[2].strftime("%d/%m/%Y %H:%M"),quantia=valor)
            array_mensagem.append(str(mensagem))

        valorTotal = locale.currency(valorTotal, grouping=True, symbol=None)
        array_mensagem.append("\n\nValor total\nR$ "+valorTotal)
        update.message.reply_text(''.join(array_mensagem))

    
    
def help(update, context):
    user = update.message.from_user.first_name
    id = update.message.from_user.id
    dateNow = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print ('{} - {} - {} digitou comando /help'.format(dateNow,id,user))
    print ('{} - {} - {} digitou comando /help'.format(dateNow,id,user), file=open("bot.log","a"))

    update.message.reply_text("Lista de Comandos\n\n/guardarFernando\n/relacaoFernando\n/guardarBrenda\n/relacaoBrenda\n/valorTotal\n/relacaoMensal\n/guardarRendimento\n/retirarSonho\n/relacaoRetirada")

def main():
    updater = Updater("TOKEN HERE", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("valorTotal",valorTotal))
    dispatcher.add_handler(CommandHandler("guardarFernando",guardarFernando))
    dispatcher.add_handler(CommandHandler("relacaoFernando",relacaoFernando))
    dispatcher.add_handler(CommandHandler("guardarBrenda",guardarBrenda))
    dispatcher.add_handler(CommandHandler("relacaoBrenda",relacaoBrenda))
    dispatcher.add_handler(CommandHandler("relacaoMensal",relacaoMensal))
    dispatcher.add_handler(CommandHandler("guardarRendimento",guardarRendimentos))
    dispatcher.add_handler(CommandHandler("retirarSonho",retirarSonho))
    dispatcher.add_handler(CommandHandler("relacaoRetirada",relacaoRetirada))
    dispatcher.add_handler(CommandHandler("help",help))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    print("press CTRL + C to cancel.")
    main()
