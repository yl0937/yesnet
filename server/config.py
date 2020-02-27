import os

POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pw': os.getenv('POSTGRES_PASSWORD', 'root'),
    'db': os.getenv('POSTGRES_DB', 'postgres'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', 5432),
}

TEST_POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pw': os.getenv('POSTGRES_PASSWORD', 'root'),
    'db': os.getenv('POSTGRES_DB', 'postgres'),
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': os.getenv('POSTGRES_PORT', 5432),
}


class Config:
    ERROR_404_HELP = False

    SECRET_KEY = os.getenv('APP_SECRET', 'Myljadf09832908uflkjasdDSDS(S&SI*S')

    MONGO_URI = 'mongodb://mj:16900/yesnet'


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True
    DEBUG = True


class ProdConfig(Config):
    DEBUG = False


config = {
    'development': DevConfig,
    'testing': TestConfig,
    'production': ProdConfig
}
