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

    # Whenever we change the database, we have to remember to COMMIT
    # the transactions
    conn.commit()

    return "new artist id = " + str(new_artist_id)


@app.route('/genre/create')
def show_create_genre_form():
    return render_template("create_genre_form.template.html")


@app.route('/genre/create', methods=["POST"])
def process_create_genre():
    genre = request.form.get('genre')

    sql = f"""
    insert into Genre (Name) values ('{genre}')
    """

    cursor.execute(sql)

    # Must commit all the changes
    conn.commit()

    return "Form recieved"


# create a new album
@app.route('/album/create')
def show_create_album_form():

    # fetch all the possible artists from the database
    sql = """
    select * from Artist
    """

    cursor.execute(sql)

    # pass all the artists into the template to render as part of
    # the drop-down (or the <SELECT>)
    return render_template("create_album.template.html", all_artists=cursor)


# Process the form
@app.route('/album/create', methods=["POST"])
def process_create_album():
    title = request.form.get("title")
    artist = request.form.get("artist")

    sql = f"""
    insert into Album (Title, ArtistId) values ("{title}", {artist})
    """

    print(sql)
    cursor.execute(sql)

    conn.commit()
    return "form recieved"


# UPDATE ROUTE
# 1. we a route to display the form PLUS the existing data
# 2. we also need a route to process the form

# display the form and the existing information
@app.route('/artist/update/<artist_id>')
def display_update_artist_form(artist_id):
    # the following SHOULD only have one result
    sql = f"select * from Artist where ArtistId={artist_id}"
    cursor.execute(sql)
    artist = cursor.fetchone()
    return render_template("update_artist_form.template.html", artist=artist)


@app.route('/artist/update/<artist_id>', methods=["POST"])
def process_update_artist(artist_id):
    artist_name = request.form.get('artist_name')
    sql = f"UPDATE Artist SET Name='{artist_name}' WHERE ArtistId={artist_id}"
    print(sql)
    cursor.execute(sql)
    conn.commit() 
    return redirect(url_for('show_all_artists'))


@app.route('/artists')
def show_all_artists():
    sql = "select * from Artist"
    cursor.execute(sql)
    return render_template('all_artists.template.html', all_artists=cursor)

# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
