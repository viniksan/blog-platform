import sqlite3

# Connect Database
conn = sqlite3.connect("blog.db", check_same_thread=False)

# Create Cursor
c = conn.cursor()

# Users Table
c.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Posts Table
c.execute("""
CREATE TABLE IF NOT EXISTS posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    author TEXT
)
""")

# Comments Table
c.execute("""
CREATE TABLE IF NOT EXISTS comments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER,
    username TEXT,
    comment TEXT
)
""")

# Likes Table
c.execute("""
CREATE TABLE IF NOT EXISTS likes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER
)
""")

conn.commit()

print("Database Created Successfully")