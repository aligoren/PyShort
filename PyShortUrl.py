from bottle import route, run, template, request, static_file, url, abort
from hashids import Hashids
import sqlite3, os

conn = ''
if not os.path.isfile('test.db'):
    conn = sqlite3.connect('test.db')
    conn.execute('CREATE TABLE "shorted" ("ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "ShortID"  TEXT, "Url"  TEXT );')
else:
    conn = sqlite3.connect('test.db')



@route("/static/<filename>", name="static")
def static(filename):
    return static_file(filename, root="static")


@route("/")
def index():
    return template("index", url=url)


@route("/short", method='POST')
def short():
    link_id = ''
    
    site = request.forms.get("txtSearch")
    ip = request.environ.get('REMOTE_ADDR')
    generated_id = Hashids(salt=site, min_length=8)
    link_id = generated_id.encrypt(len(site)+int(str.replace(ip, '.', '')))
    addUrl = conn.execute("INSERT INTO shorted(ShortID, Url) VALUES('"+link_id+"', '"+site+"');")
    conn.commit()
    if addUrl:
        return dict(Data=link_id)
    else:
        return dict(Data="Eklenirken Hata Oluştu")
    conn.close()


@route("/r/<shortID>", method='GET')
def r(shortID):
    getUrl = conn.execute("SELECT Url FROM shorted WHERE ShortID='"+shortID+"'")
    
    for adres in getUrl.fetchall():
        return template('r', adres=adres[0], url=url)
    else:
        abort(404, "Böyle bir URL Bulunamadı :(")

run(host='localhost', port=8080)