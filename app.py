#       Name: Jasmine Masopeh 
#       FSUID: jdm21e 
#       Due Date: 2/21/2024
#       The program in this file is the individual work of Jasmine Masopeh 

from flask import Flask, render_template, request
import sqlite3 as sql
from datetime import datetime

app = Flask(__name__)

# Different Routes to HTML Pages
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/addReview")
def new_review():
    return render_template("addReview.html")


@app.route("/getReview")
def get_review():
    return render_template("getReview.html")


@app.route("/getYear")
def get_year():
    return render_template("getYear.html")


# add Review routes back to homepage when submitted
@app.route("/addrec", methods=["POST", "GET"])
def addrec():
    if request.method == "POST":
        try:
            Username = request.form["Username"]
            Rating = request.form["Rating"]
            Review = request.form["Review"]
            Title = request.form["Title"]
            Director = request.form["Director"]
            Genre = request.form["Genre"]
            Year = request.form["Year"]

            ReviewTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            MovieID = Title[:5] + str(Year)

            with sql.connect("movieData.db") as con:
                cur = con.cursor()

                cur.execute(
                    "INSERT INTO Reviews (Username, ReviewTime, Rating, Review, MovieID) VALUES (?, ?, ?, ?, ?)",
                    (Username, ReviewTime, Rating, Review, MovieID),
                )

                cur.execute(
                    "INSERT INTO Movies (MovieID, Title, Director, Genre, Year) VALUES (?, ?, ?, ?, ?)",
                    (
                        MovieID,
                        Title,
                        Director,
                        Genre,
                        Year,
                    ),
                )

                con.commit()
                msg = "Record successfully added"
        except Exception as e:
            con.rollback()
            msg = "error in insert operation: " + str(e)
        finally:
            con.close()
            return render_template("index.html", msg=msg)

# gets all the Movies with the genre inserted into form
@app.route("/genre", methods=["POST", "GET"])
def list_genre():
    genre = request.form.get("Genre")

    with sql.connect("movieData.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM Movies JOIN Reviews ON Movies.MovieID = Reviews.MovieID WHERE Movies.Genre = ?",
            (genre,),
        )

        rows = cur.fetchall()
    return render_template("listByGenre.html", rows=rows, genre=genre)

# gets a list of at most 5 movies witht eh best ratings based on year
@app.route("/getyear", methods=["POST", "GET"])
def best_year():
    year = request.form.get("Year")

    with sql.connect("movieData.db") as con:
        con.row_factory = sql.Row
        cur = con.cursor()

        cur.execute(
            """
         SELECT Title, Genre, AVG(Rating) as AvgRating
         FROM Movies
         JOIN Reviews ON Movies.MovieID = Reviews.MovieID
         WHERE Year = ?
         GROUP BY Movies.MovieID
         ORDER BY AvgRating DESC, Title ASC
         LIMIT 5
      """,
            (year,),
        )

        rows = cur.fetchall()

    return render_template("bestInYear.html", rows=rows, year=year)


if __name__ == "__main__":
    app.run(debug=True)
