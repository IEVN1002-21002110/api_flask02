class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER = 'damian'
    MYSQL_PASSWORD='root'
    MYSQL_DB='api_utl'
    MYSQL_PORT = 3307
   
config={
    'development': DevelopmentConfig
}
 