from twitter_bot import TwitterBot


def main():
    try:
        pj = TwitterBot("your_username", "your_password")  # Here put you login credentials
        pj.log_in()
        pj.search('100DaysOfCode')
        pj.like(10)  # like 10 tweets
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
