from scraper import get_acting_credits_count


# Entry URL
katies_imdb = 'https://www.imdb.com/name/nm2692146/?ref_=nv_sr_srsg_0'

current_acting_credits_count = get_acting_credits_count(katies_imdb)


def main(current):
        print(f'Katie has {current} acting credits on IMDB!')


if __name__ == '__main__':
    main(current_acting_credits_count)

