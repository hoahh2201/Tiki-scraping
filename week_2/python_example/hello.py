import psycopg2

conn = psycopg2.connect("dbname=CoderTicket_development user=minhdh")
cur = conn.cursor()
cur.execute('SELECT * FROM regions')
notes = cur.fetchall()
print(notes)
conn.close()


# Analyze products of Tiki
# -> Get data from tiki.vn(products, comments, rating, users)

# - Get tikinow and avg rating
# - Create database
# - Save products into database
# - Start Analyzing products data
# - Get comments and users
# - Save into database
# - Find more insights
# - Prepare for the presentation on MONDAY MORNING: 2 hour

# Good luck guys!!!
