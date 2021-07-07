# import sqlite3

# conn = sqlite3.connect('acting_credits_count.db')

# c = conn.cursor()

# c.execute(""" CREATE TABLE actors (
#     name text,
#     credits integer
# ) """)

# c.execute("INSERT INTO actors VALUES ('katie mcgrath', 26)")

# c.execute("SELECT * FROM actors WHERE name='katie mcgrath'")


# def get_actor(name):
#     c.execute("SELECT * FROM actors WHERE name=:name", {'name': name})
#     return c.fetchone()


# def update_actor(name, credits):
#     with conn:
#         c.execute("""UPDATE actors SET credits = :credits
#                     WHERE name = :name""",
#                   {'name': name, 'credits': credits})


# katie = get_actor('katie mcgrath')

# print(katie)

# update_actor('katie mcgrath', 27)

# katie = get_actor('katie mcgrath')

# print(katie)


# conn.commit()

# conn.close()
