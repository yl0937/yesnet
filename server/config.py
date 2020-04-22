import os
import enum

CONFIG = {
    'REDIS-IP' : 'redis',
    'R-CHANNEL': 'orderChannel',    # Receiving Channel
    'S-CHANNEL': 'resChannel',      # Sending Channel
    'RPC-URL': 'http://210.114.89.52:8545', # RPC URL, 실제 적용 시에 적절한 값으로 바뀌어야 함.
    'ADAM': '0xb3b4ef17ba517e75b79169354fd9dfff51b9d592'
}

CMD = {
    'GET_BALANCE': 'getBalance', # query balance
    'CALL_FUNCTION': 'callFunction', # DApp의 메서드를 호출
    'CALL_TX': 'callTx',            # Call Tx of DApp
    'CREATE_ACCOUNT': 'createAccount', # 계정을 생성
    'DEPLOY_DAPP': 'deployDApp',     # DApp을 Deployment
    'GET_BLOCK': 'getBlock',     # Block에 대한 정보를 보여줌.
    'GET_TX': 'getTx',           # TX에 대한 정보를 보여줌.
    'FILL_ETH': 'fillEth',       # ether를 채우는 명령
    'PING': 'ping'               # ping method
}


class ResCode(enum.Enum):
    OK = 200
    SERVER_FAIL = 500
    TIME_OUT = 501

# Error code
ERR_SERVER_FAIL = 500


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
