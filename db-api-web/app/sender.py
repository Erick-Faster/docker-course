import psycopg2 #Para mexer no postgre
from bottle import route, run, request

DSN = 'dbname=email_sender user=postgres password=admin host=db'
SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'

def register_message(assunto, mensagem):
    conn = psycopg2.connect(DSN) #conexao
    cur = conn.cursor() #cursor
    cur.execute(SQL, (assunto, mensagem))
    conn.commit()
    cur.close()
    conn.close()

    print('Mensagem registrada !')

@route('/', method='POST')
def send():
    assunto = request.forms.get('assunto')
    mensagem = request.forms.get('mensagem')
    
    register_message(assunto, mensagem)
    return 'Mensagem enfileirada ! Assunto {} Mensagem: {}'.format(
        assunto, mensagem
    )

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)