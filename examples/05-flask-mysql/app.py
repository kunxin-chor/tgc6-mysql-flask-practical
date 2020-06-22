from flask import Flask, render_template, request, redirect, url_for
import pymysql
from dotenv import load_dotenv
import os

# 1. Load in the environment variables
load_dotenv()

# 2. Create the connection
conn = pymysql.connect(host="localhost",
                       user=os.environ.get("DB_USER"),
                       password=os.environ.get("DB_PASSWORD"),
                       database="Chinook"
                       )

# 1. Create the cursor
cursor = conn.cursor(pymysql.cursors.DictCursor)

app = Flask(__name__)

@app.route("/tracks")
def show_tracks():
    # create the sql statement
    sql = """
        select * from Track
    """

    cursor.execute(sql)

    return render_template("track.template.html", cursor=cursor)


@app.route("/albums")
def show_ablums():
    # create the sql statement
    sql = """
    select * from Album
    """

    cursor.execute(sql)

    return render_template('album.template.html', cursor=cursor)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
