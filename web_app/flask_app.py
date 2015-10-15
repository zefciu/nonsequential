from flask import Flask
import psycopg2.pool


app = Flask(__name__)


pool = psycopg2.pool.ThreadedConnectionPool(
    0, 1000,
    host='127.0.0.1',
    user='zefciu',
    password='zelgad00',
    database='sample_data',
)


@app.route('/')
def hello_world():
    result = []
    connection = pool.getconn()
    cur = connection.cursor()
    cur.execute('select first_name, last_name from people limit 100;')
    for first_name, last_name in cur.fetchall():
        result.append('{} {}<br>'.format(first_name, last_name))
    pool.putconn(connection)
    return '<html><head></head><body>{}</body></html>'.format(
        '\n'.join(result)
    )


if __name__ == '__main__':
    app.run(debug=True, port=8000)
