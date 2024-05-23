# Introduction
This project is hosted on the CodeCademy forums as an independant project to gain further understanding of working with fairly basic SQL.
Link: https://discuss.codecademy.com/t/data-science-independent-project-2-explore-a-sample-database/419945

# Database
The database is the example SQLlite database found here: https://www.sqlitetutorial.net/sqlite-sample-database/

The database has data dealing with a music store company and includes information about the music, the employees, the customers, and the orders.

Through some investigation, some tracks show up with multiple TrackId's and have the same name. Despite this potential issue, these aren't fully duplicate values as many other values are also different between them. Since many values are different, these tracks are treated as fully separate entities throughout the analysis. 
## Entity Relationship Diagram
![Entity Relational Diagram](./SQLite_Sample_Database.jpg)
## Table descriptions
The Chinook sample database has 11 tables as follows:
- employees table stores employee data such as id, last name, first name, etc. It also has a field named ReportsTo to specify who reports to whom.
- customers table stores customer data.
- invoices & invoice_items tables: these two tables store invoice data. The invoices table stores invoice header data and the invoice_items table stores the invoice line items data.
- artists table stores artist data. It is a simple table that contains the id and name.
- albums table stores data about a list of tracks. Each album belongs to one artist. However, one artist may have multiple albums.
- media_types table stores media types such as MPEG audio and AAC audio files.
- genres table stores music types such as rock, jazz, metal, etc.
- tracks table stores the data of songs. Each track belongs to one album.
- playlists & playlist_track tables: playlists table stores data about playlists. Each playlist contains a list of tracks. Each track may belong to multiple playlists. The relationship between the playlists and tracks tables is many-to-many. The playlist_track table is used to reflect this relationship.
# Questions
## Basic Questions
1. Which tracks appeared in the most playlists? how many playlist did they appear in?
2. Which track generated the most revenue? which album? which genre?
3. Which countries have the highest sales revenue? What percent of total revenue does each country make up?
4. How many customers did each employee support, what is the average revenue for each sale, and what is their total sale?

## Intermediate Questions
5. Do longer or shorter length albums tend to generate more revenue?
6. Is the number of times a track appear in any playlist a good indicator of sales?

## Advanced Questions
7. How much revenue is generated each year, and what is its percent change from the previous year?