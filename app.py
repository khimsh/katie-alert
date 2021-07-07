import os
from scraper import get_acting_credits_count
from sendMail import send_mail
import sqlite3

conn = sqlite3.connect('acting_credits_count.db')
c = conn.cursor()


def get_actor(name: str):
    """ Get actor from db by name """
    c.execute("SELECT * FROM actors WHERE name=:name", {'name': name})
    return c.fetchone()


def update_actor(name: str, credits: int):
    """ Update acting credits count """
    with conn:
        c.execute("""UPDATE actors SET credits = :credits
                    WHERE name = :name""",
                  {'name': name, 'credits': credits})


EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASS = os.environ.get('EMAIL_PASS')

# Entry URL
katies_imdb = 'https://www.imdb.com/name/nm2692146/?ref_=nv_sr_srsg_0'

prev_credits_count = get_actor('katie mcgrath')[1]
current_acting_credits_count = get_acting_credits_count(katies_imdb)


def main(prev, current):
    if (current != prev):

        send_mail(EMAIL_ADDRESS, EMAIL_PASS)

        # Update Credits count to the current one.
        prev = update_actor('katie mcgrath', current)

    else:
        print('Still the same.')


if __name__ == '__main__':
    main(prev_credits_count, current_acting_credits_count)

conn.close()
