from yesnet.server.models.database import ZenMongo
import json
zen_mongo = ZenMongo()

def dapp_info(dapp_id):
    info  = zen_mongo.find_dapp_by_id(dapp_id)
    abi = info['payload']['abi']
    print(abi)
    json_abi  = json.loads(abi)
    ret_val = []
    for abi_info in json_abi:
        if  abi_info['type'] == 'function':
            function_info  = {}
            function_info['name'] = abi_info['name']
            function_info['inputs'] = abi_info['inputs']
            ret_val.append(function_info)

    print(ret_val)






dapp_info('5d85ea3933d730c484436266')