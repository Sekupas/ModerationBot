import sqlite3

conn = sqlite3.connect("Discord.db") # или :memory:
cursor = conn.cursor()

with conn:
    conn.execute("""
        CREATE TABLE "Mutes" (
            "id" INT,
            "time" INT,
            "term" TEXT,
            "reason" TEXT
        );
    """)

with conn:
    conn.execute("""
        CREATE TABLE "Bans" (
            "id" INT,
            "perm" INT,
            "time" INT,
            "term" TEXT,
            "reason" TEXT
        );
    """)


with conn:
    conn.execute("""
        CREATE TABLE "Warns" (
            "id" INT,
            "count" INT
        );
    """)


