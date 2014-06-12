import bottle
from bottle.ext import sqlite
from bottle import HTTPError
from json import dumps

app = bottle.Bottle()
plugin = sqlite.Plugin(dbfile='database.db')
app.install(plugin)

@app.get('/skills/<skill_id:int>')
def skills_by_id(skill_id, db):
    row = db.execute('SELECT * FROM skills WHERE id=?', (skill_id,)).fetchone()
    if row:
        return {'title': row['title'], 'description': row['description'], 'url': row['url'], 'image_path': row['image_path']}
    return HTTPError(404, 'Page not found')

@app.get('/skills')
def get_all_skills(db):
    rows = db.execute('SELECT * FROM skills')
    if rows:
        results = []
        for row in rows:
            results.append({'title': row['title'], 'description': row['description'], 'url': row['url'], 'image_path': row['image_path']})
        return dumps(results)
    return HTTPError(404, 'Page not found')

@app.get('/skills/<skill_id:int>/challenges/<challenge_id:int>')
def get_challenge_by_skill_id_and_challenge_id(skill_id, challenge_id, db):
    row = db.execute('SELECT * FROM challenges WHERE skill_id=? AND id=?', (skill_id, challenge_id)).fetchone()
    if row:
        return {'title': row['title']}
    return HTTPError(404, 'Page not found')

@app.get('/skills/<skill_id>/challenges')
def get_all_challenges_by_skill_id(skill_id, db):
    results = []
    rows = db.execute('SELECT * FROM challenges WHERE skill_id=?', (skill_id,))
    if rows:
        for row in rows:
            results.append({'title': row['title']})
        return dumps(results)
    return HTTPError(404, 'Page not found')

app.run(host='localhost', port=8080, debug=True)








