import sqlite3

db = sqlite3.connect('database.db')
db.execute("CREATE TABLE skills (id INTEGER PRIMARY KEY, title CHAR(100) NOT NULL, description CHAR(255) NOT NULL, url CHAR(255) NOT NULL, image_path CHAR(255) NOT NULL)")
db.execute("INSERT INTO skills (title, description, url, image_path) VALUES ('Actor', 'Actors bring characters to life. We conjure up emotion and laughter with our words and stories.', '/skills/actor', 'https://d1973c4qjhao9m.cloudfront.net/patches/actor_icon_small.png')")
db.execute("INSERT INTO skills (title, description, url, image_path) VALUES ('Angler', 'Anglers find and catch fish.', '/skills/angler', 'https://d1973c4qjhao9m.cloudfront.net/patches/angler_icon.png')")
db.execute("INSERT INTO skills (title, description, url, image_path) VALUES ('Animator', 'Animators are the magicians of movies.', '/skills/animator', 'https://d1973c4qjhao9m.cloudfront.net/patches/animator_icon.png?4')")
db.execute("INSERT INTO skills (title, description, url, image_path) VALUES ('Archer', 'Bows and arrows and a steady hand - these are the tools of an Archer.', '/skills/archer', 'https://d1973c4qjhao9m.cloudfront.net/patches/archer_icon.png')")
db.execute("INSERT INTO skills (title, description, url, image_path) VALUES ('Architect', 'Architects design buildings and structures.', '/skills/architect', 'https://d1973c4qjhao9m.cloudfront.net/patches/architect_icon.png')")
db.commit()
