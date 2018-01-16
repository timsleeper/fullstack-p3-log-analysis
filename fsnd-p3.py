#! /usr/bin/env python2

import psycopg2

# Database name to connect
DBNAME = 'news'


def main():

    # Connect to the database

    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()

    qry_articles = """
       SELECT a.title, count(*) as views
       FROM articles as a
       JOIN log as b ON CONCAT('/article/', a.slug) = b.path
       GROUP BY a.title
       ORDER BY views DESC limit 3;
    """
    cur.execute(qry_articles)
    results = cur.fetchall()

    print('Here are the 3 most popular articles of all time:\n')
    for text, value in results:
        print("{text} -- {value} views".format(text=text, value=value))

    qry_authors = """
       SELECT a.name, count(*) as views
       FROM authors as a
       JOIN articles as b ON a.id = b.author
       JOIN log as c ON CONCAT('/article/', b.slug) = c.path
       GROUP BY a.name
       ORDER BY views DESC;
    """
    cur.execute(qry_authors)
    results = cur.fetchall()

    print('\n\nHere are the most popular authors of all time:\n')
    for text, value in results:
        print("{text} -- {value} views".format(text=text, value=value))

    qry_logs = """
       SELECT date, perc::numeric(2, 1)
       FROM (
           SELECT time::date as date,
           sum(case when status != '200 OK' then 1 else 0 end) / 
           count(*)::float * 100 as perc
           FROM log
           GROUP BY date
       ) as error_perc
       where perc > 1;
    """
    cur.execute(qry_logs)
    results = cur.fetchall()

    print('\n\nHere are the days where more than \
    1% of requests lead to errors:\n')
    for text, value in results:
        print("{text} -- {value} % errors".format(text=text, value=value))

    db.close()

if __name__ == '__main__':
    main()