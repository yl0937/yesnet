from .database import ZenMongo
from .dom import User, DApp, DeployedOne

if __name__ == "__main__":
    zen_mongo = ZenMongo()

    account = 'zedi'
    name = 'Luke'
    email = 'zedai@gmail.com'
    logpass = 'XXXXXlog'
    gethpass = 'gethxxx'
    user = User(account,name, email, logpass, gethpass)

    zen_mongo.update_user(user)

    user_result = zen_mongo.find_user_by_account(account)

    dapp = DApp(user, 'hello3', 'yyyyyyyyyyyyyyyy', '1213254')

    zen_mongo.add_dapp(dapp)

    dapp_result = zen_mongo.find_dapp_by_id('5d74da2d2d4a0e5cb842f535')

    deploy = DeployedOne(user_result['payload'], dapp_result['payload'], 'zzzz', 'zzzz')
    zen_mongo.add_deployed(deploy)

    result = zen_mongo.find_deployed_by_account('aaa')
    if result['code'] == 200:
        for deploy in result['payload']:
            print(deploy)
    elif result['code'] == 404:
        print('nothing')

    result = zen_mongo.find_deployed_by_addr('43234')
    if result['code'] == 200:
        print(result['payload'])
    elif result['code'] == 404:
        print('nothing')

    result = zen_mongo.find_deployed_with_dapp('yyyyyyy')
    if result['code'] == 200:
        print(result['payload'])
    elif result['code'] == 404:
        print('nothing')
