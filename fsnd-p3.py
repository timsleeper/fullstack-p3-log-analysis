#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2
import sys

# Database name to connect
DBNAME = 'news'


def connect(database_name):
    """Connect to the PostgreSQL database. Returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        c = db.cursor()
        return db, c
    except psycopg2.Error as e:
        print("Unable to connect to database")
        sys.exit(1)
        raise e


def execute_query(query):
    """Connect to a database, runs a query
    and returns downloaded query results
    """
    # connect to database, grab cursor
    db, cur = connect(DBNAME)

    cur.execute(query)
    results = cur.fetchall()
    db.close()
    return results


def print_top_articles():
    """Function to get the 3 most popular articles of all time"""
    qry_articles = """
       SELECT a.title, count(*) as views
       FROM articles as a
       JOIN log as b ON CONCAT('/article/', a.slug) = b.path
       GROUP BY a.title
       ORDER BY views DESC limit 3;
    """

    results = execute_query(qry_articles)

    print('Here are the 3 most popular articles of all time:\n')
    for text, value in results:
        print("{text} -- {value} views".format(text=text, value=value))


def print_top_authors():
    """Function to get the most popular authors"""
    qry_authors = """
       SELECT a.name, count(*) as views
       FROM authors as a
       JOIN articles as b ON a.id = b.author
       JOIN log as c ON CONCAT('/article/', b.slug) = c.path
       GROUP BY a.name
       ORDER BY views DESC;
    """

    results = execute_query(qry_authors)

    print('\n\nHere are the most popular authors of all time:\n')
    for text, value in results:
        print("{text} -- {value} views".format(text=text, value=value))


def print_log_error_days():
    """Function to get days with more than 1% error"""
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

    results = execute_query(qry_logs)

    print('\n\nHere are the days where more than \
    1% of requests lead to errors:\n')
    for text, value in results:
        print("{text} -- {value} % errors".format(text=text, value=value))


def main():
    """Main Function. Calls out 3 print functions to
    answer the questions proposed in the project.
    """
    print_top_articles()
    print_top_authors()
    print_log_error_days()


if __name__ == '__main__':
    main()
