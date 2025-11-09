class DevelopmentConfig():
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'damian'
    MYSQL_PASSWORD = 'root'
    MSQL_DB = 'api_utl'

    config={
        'development':DevelopmentConfig,
    }