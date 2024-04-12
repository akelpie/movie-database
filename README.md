# Movie Ratings and Reviews Web Application

## Specifications

This homework assignment involves using `sqlite3` and `flask` libraries to build a text-only ratings and reviews website for movies.

### Database Setup

- **sqlite3**: We'll utilize a sqlite3 database named `movieData.db`. This database will be created during the connection process in Step 2.

### Implementation Steps

1. **Setup Script**: Write a Python script named `setup.py` that connects to the database and creates necessary tables.
2. **Reviews Table**: Create a table `Reviews` with the following fields:
   - Username (text)
   - MovieID (text)
   - ReviewTime (SQL Datetime)
   - Rating (float)
   - Review (text)
3. **Movies Table**: Create a table `Movies` with the following fields:
   - MovieID (text, Primary Key)
   - Title (text)
   - Director (text)
   - Genre (text)
   - Year (integer)

### Web Pages

- **index.html**: Homepage with a welcome message and navigation links.
- **addReview.html**: Form page to submit a movie review.
- **getReviews.html**: Form page to fetch reviews by movie genre.
- **listByGenre.html**: Displays movie reviews by genre in a table format.
- **getYear.html**: Form page to fetch top 5 movies by year based on average ratings.
- **bestInYear.html**: Displays top 5 movies by year with names, genres, and average ratings.

### Navigation

- All pages, except the homepage, should include a "Back to Home" link.

### Flask Application

- **app.py**: Main Flask application script with the following functions:
  - Render the homepage.
  - Add rows to the `Reviews` and `Movies` tables upon form submission on `addReview.html`.
  - Fetch and display all reviews for a genre.
  - Fetch and display the top 5 movies of a given year.
  - Main module to run the application if it's the main module.


### SQL Commands

- Directly write SQL commands for all database interactions. The use of libraries like `sqlalchemy` for SQL generation is not permitted and will result in a loss of points.

### Project Assumptions

- The use of the first 5 characters of a movie's title followed by its release year will uniquely identify movies for this project.
- Verification of data fitting within text fields and user ratings being a numeric value between 1 and 5 will be managed via client-side JavaScript, not within the scope of this assignment.

## Running the Application

### Setting up the Database

Run the `setup.py` script to create and initialize the database and tables:

```bash
python3 setup.py
```
To start the web application, run the following command in your terminal:
```bash
python3 app.py
```

