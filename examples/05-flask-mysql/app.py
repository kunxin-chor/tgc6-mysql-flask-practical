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

# 3. Create the cursor
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


# To do a create featuire, we need TWO routes
# 1. the first route is to display the form
# 2. the second route is to process the form and save the new data to database
@app.route('/artist/create')
def show_create_artist_form():
    return render_template('create_artist.template.html')


@app.route('/artist/create', methods=["POST"])
def process_create_artist():
    artist_name = request.form.get("artist_name")

    sql = f"""
    insert into Artist (Name) values ("{artist_name}");
    """

    cursor.execute(sql)

    # get the id of the most recently inserted row
    new_artist_id = cursor.lastrowid

    print(sql)

    # Whenever we change the database, we have to remember to COMMIT
    # the transactions
    conn.commit()

    return "new artist id = " + str(new_artist_id)


# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
