# Python 2.7.10

import psycopg2

# What are the most popular three articles of all time?

query_popArticles_title = "What are the most popular three articles of all time?"
query_popArticles = "SELECT title, views FROM article_view LIMIT 3"

# Who are the most popular article authors of all time?

query_popAuthors_title = "Who are the most popular articles authors of all time?"
query_popAuthors = "SELECT authors.name, sum(article_view.views) AS views FROM article_view,authors WHERE " \
                   "authors.id = article_view.author GROUP BY authors.name ORDER BY views DESC"

# On which days did more than 1% of requests lead to errors?

query_errorLog_title = "On which days did more than 1% of requests lead to errors?"
query_errorLog = "SELECT * FROM error_log_view WHERE \"Percent Error\" > 1"


# Connect to DB = news

def connect(database_name="news"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error: Unable to connect to the database>")


# Return Results
def get_query_results(query):
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


# Print Results

def print_query_results(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print (index + 1, "name:", results[0], "views:", str(results[1]))


def print_error_results(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print(results[0], str(results[1]) + "% errors")


if __name__ == '__main__':
    # Store
    popArticles_results = get_query_results(query_popArticles), query_popArticles_title
    popAuthors_results = get_query_results(query_popAuthors), query_popAuthors_title
    errorLog_results = get_query_results(query_errorLog), query_errorLog_title

    # Print
    print_query_results(popArticles_results)
    print_query_results(popAuthors_results)
    print_query_results(errorLog_results)
