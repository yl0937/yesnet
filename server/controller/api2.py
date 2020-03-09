import json

from bson import json_util
from flask import Blueprint, render_template, abort, jsonify, request, redirect, session, url_for
from flask import current_app as app
# import bcrypt
from pymongo import MongoClient, collection

from yesnet.server.controller import redisfunction
from yesnet.server.models.database import ZenMongo
from yesnet.server.models.dom import DApp


import datetime

from yesnet.server.controller.redisfunction import MsgHandler
# from server.models.database import LoginAPI

api_page = Blueprint('api_page', 'api_page', template_folder='templates')
api_page.resource = {}


@api_page.route('/log', methods=['GET'])
def get_log():
    return jsonify({
        'status': 'success'
    })


ORDERgetTx = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "getTx",
  "params": {
       "txHash": "0x6e8d413365fe89f9b6bcbeebc9748e4686657626ba996bb8b38b45fef673bbff"
}}


@api_page.route('/watchtx', methods=['GET'])
def ping():
    msg = redisfunction.MsgHandler()

    msg.put_order(ORDERgetTx)
    Reponse1 = msg.hget_response(ORDERgetTx)
    print(type(Reponse1), ":", Reponse1)

    return Reponse1


ORDERgetBlock = {
    "ticket": "20190814065206123456",
    "timestamp": 1562069915.0,
    "uid": "dilab@gmail.com",
    "cmd": "getBlock",
    "params": {
        "blockNum": 852
   }
}


@api_page.route('/watchblock', methods=['GET'])
def getblock():
    msg = redisfunction.MsgHandler()

    msg.put_order(ORDERgetBlock)
    Reponse2 = msg.hget_response(ORDERgetBlock)
    print(type(Reponse2), ":", Reponse2)

    return Reponse2


ORDERgetBalance = {
"ticket": "20190814065206123456",
"timestamp": 1562069915.0,
"uid": "dilab@gmail.com",
"cmd": "getBalance",
"params": {
   "account": "0xb3b4ef17ba517e75b79169354fd9dfff51b9d592"
   }
}


@api_page.route('/balance', methods=['GET'])
def getbalance():
    msg = redisfunction.MsgHandler()

    msg.put_order(ORDERgetBalance)
    Reponse3 = msg.hget_response(ORDERgetBalance)
    print(type(Reponse3), ":", Reponse3)

    return Reponse3


ORDERDApp = {
    "ticket": "20190814065206123456",
    "timestamp": 1562069915.0,
    "uid": "dilab@gmail.com",
    "cmd": "deployDApp",
    "params": {

        "account": "0xb3b4ef17ba517e75b79169354fd9dfff51b9d592",

        "passwd": "yes36%",

        "app_name": "hello",

        "bin": '608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610410806101166000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100c5578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100c3600480360381019080803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091929192905050506101e5565b005b3480156100d157600080fd5b506100da6101ff565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561011a5780820151818401526020810190506100ff565b50505050905090810190601f1680156101475780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101fb92919061033f565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102975780601f1061026c57610100808354040283529160200191610297565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a7230582023e221760f10d2a6ca8c3efc216d61879e1e47e45a041b15d684884e6fb346e90029',

        "abi": '''
    [
        {
            "constant": false,
            "inputs": [
                {
                    "name": "_greeting",
                    "type": "string"
                }
            ],
            "name": "setGreeting",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "greet",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "greeting",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "constructor"
        }
    ]'''

   }}


@api_page.route('/DApp', methods=['GET'])
def ping2():
    msg = redisfunction.MsgHandler()

    msg.put_order(ORDERDApp)
    Response4 = msg.hget_response(ORDERDApp)
    print(type(Response4), ":", Response4)

    return Response4


ORDERcallMethod = {
    "ticket": "20190814065206123456",
    "timestamp": 1562069915.0,
    "uid": "dilab@gmail.com",
    "cmd": "callMethod",
    "params": {

        "account": "0xb3b4ef17ba517e75b79169354fd9dfff51b9d592",

        "passwd":  "yes36%",

        "contractAddress": '0x799FA741c0840d6a846b3743f754a8d8839a4546',

        "functionName": 'greet',

        "bin": '608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610410806101166000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100c5578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100c3600480360381019080803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091929192905050506101e5565b005b3480156100d157600080fd5b506100da6101ff565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561011a5780820151818401526020810190506100ff565b50505050905090810190601f1680156101475780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101fb92919061033f565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102975780601f1061026c57610100808354040283529160200191610297565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a7230582023e221760f10d2a6ca8c3efc216d61879e1e47e45a041b15d684884e6fb346e90029',

        "abi": '''
    [
        {
            "constant": false,
            "inputs": [
                {
                    "name": "_greeting",
                    "type": "string"
                }
            ],
            "name": "setGreeting",
            "outputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "greet",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": true,
            "inputs": [],
            "name": "greeting",
            "outputs": [
                {
                    "name": "",
                    "type": "string"
                }
            ],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "payable": false,
            "stateMutability": "nonpayable",
            "type": "constructor"
        }
    ]'''

   }
}


@api_page.route('/Method', methods=['GET'])
def callMethod():
    msg = redisfunction.MsgHandler()

    msg.put_order(ORDERcallMethod)
    Response6 = msg.hget_response(ORDERcallMethod)
    print(type(Response6), ":", Response6)

    return Response6


@api_page.route('/dapp_list', methods=['GET'])
def dappList():
    account = request.args.get('account')
    result = api_page.resource['mongo'].find_dapp_by_account(account)
    if result['code'] == 200: # Success
        return jsonify(result['payload'])
    else:
        return jsonify(result)


@api_page.route('/add_user', methods=['GET'])
def add_user():
    given_name = request.args.get('name')
    age = request.args.get('age')
    user = {'name':given_name, 'age':age}
    api_page.resource['mongo'].add_user(user)
    return 'Write Success'


@api_page.route('/del_user', methods=['GET'])
def del_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    api_page.resource['mongo'].del_user(user)
    return 'Del Success'


@api_page.route('/find_user', methods=['GET'])
def find_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    user = api_page.resource['mongo'].find_user(user)
    return user


@api_page.route('/update_user', methods=['GET'])
def update_user():
    given_name = request.args.get('name')
    user = {'name':given_name}
    user = api_page.resource['mongo'].update_user(user)
    return user


@api_page.route('/save_tx', methods=['GET', 'POST'])
def save_tx():
    if request.method == 'POST':
        collection.save({
            "ticket": "20190814065206123456",
            "timestamp": 1562069915.0,
            "uid": "dilab@gmail.com",
            "cmd": "getTx",
            "params": {
                "txHash": "0x6e8d413365fe89f9b6bcbeebc9748e4686657626ba996bb8b38b45fef673bbff"
            }
        })
        return redirect('/')
    else:
        return 'success!'


# @api_page.route('/add_dapp', methods=['GET'])
# def add_dapp():
#     given_bin = request.args.get('bin')
#     tx = request.args.get('tx')
#     dapp = {'bin':given_bin, 'tx':tx}
#     api_page.resource['mongo'].add_dapp(dapp)
#     return 'Write Success'


@api_page.route('/add_dapp', methods=['GET', 'POST'])
def add_dapp():
    uid = request.json['uid']
    result = api_page.resource['mongo'].find_user_by_id(uid)
    if result['code'] == 200:
        user = result['payload']
        name = request.json['name']
        desc = request.json['desc']
        abi = request.json['abi']
        binary = request.json['bin']
        dapp = DApp(user, name, desc, abi, binary)
        result = api_page.resource['mongo'].add_dapp(dapp)

    ret_val = jsonify(result)
    print(ret_val)
    return ret_val




@api_page.route('showdb', methods=['GET'])
#def json_default(value):
#    if isinstance(value):
#        return value.strftime('%Y-%m-%d %H:%M:%S')
def showdb():
    show_document = ZenMongo()
    documents = show_document.find("dapps", {})
    print(type(documents), ":", documents)
    dataset = json.dumps(documents, default=json_util.default)
#    for key, value in dataset.items():
#        print(key, "|", value)
    return dataset
#    return jsonify(documents)


@api_page.route('txtTojson', methods=['POST', 'GET'])
def convert():

    abi = request.json
#    print(type(abi), ":", abi)
    abi2 = json.dumps(abi)
#    print(type(abi2), ":", abi2)
    dicAbi = json.loads(abi2)
    print(type(dicAbi), ":", dicAbi)
    for key, value in dicAbi.items():
        print(key, "|", value)
#        print(type(value))
        """
    abifunction = json.dumps(value)
    print(type(abifunction), ":", abifunction)"""
    dicAbi2 = json.loads(value)
    print(type(dicAbi2), ":", dicAbi2)
    for i in dicAbi2:
#        print(i)
        for key, value in i.items():
            if key == "inputs":
                print(key, "|", value)
    return 'abi2'


@api_page.route('DK', methods=['POST', 'GET'])
def trying():
    return jsonify({

        "ticket": "20190814065206123456",
        "timestamp": 1562069915.0,
        "uid": "dilab@gmail.com",
        "cmd": "callMethod",
        "params": {

            "account": "0xb3b4ef17ba517e75b79169354fd9dfff51b9d592",

            "passwd": "yes36%",

            "contractAddress": '0x799FA741c0840d6a846b3743f754a8d8839a4546',

            "functionName": 'greet',

            "bin": '608060405234801561001057600080fd5b506040805190810160405280600581526020017f48656c6c6f0000000000000000000000000000000000000000000000000000008152506000908051906020019061005c929190610062565b50610107565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106100a357805160ff19168380011785556100d1565b828001600101855582156100d1579182015b828111156100d05782518255916020019190600101906100b5565b5b5090506100de91906100e2565b5090565b61010491905b808211156101005760008160009055506001016100e8565b5090565b90565b610410806101166000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063a41368621461005c578063cfae3217146100c5578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100c3600480360381019080803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091929192905050506101e5565b005b3480156100d157600080fd5b506100da6101ff565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561011a5780820151818401526020810190506100ff565b50505050905090810190601f1680156101475780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b80600090805190602001906101fb92919061033f565b5050565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102975780601f1061026c57610100808354040283529160200191610297565b820191906000526020600020905b81548152906001019060200180831161027a57829003601f168201915b5050505050905090565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a7230582023e221760f10d2a6ca8c3efc216d61879e1e47e45a041b15d684884e6fb346e90029',

            "abi": '''
     [
         {
             "constant": false,
             "inputs": {
                 {
                     "name": "_greeting",
                     "type": "string"
                 }
             },
             "name": "setGreeting",
             "outputs": [],
             "payable": false,
             "stateMutability": "nonpayable",
             "type": "function"
         },
         {
             "constant": true,
             "inputs": [],
             "name": "greet",
             "outputs": {
                 {
                     "name": "",
                     "type": "string"
                 }
             },
             "payable": false,
             "stateMutability": "view",
             "type": "function"
         },
         {
             "constant": true,
             "inputs": [],
             "name": "greeting",
             "outputs": {
                 {
                     "name": "",
                     "type": "string"
                 }
             },
             "payable": false,
             "stateMutability": "view",
             "type": "function"
         },
         {
             "inputs": [],
             "payable": false,
             "stateMutability": "nonpayable",
             "type": "constructor"
         }
     ]'''

        }
    })


@api_page.route('/deploymentPost', methods=['GET', 'POST'])
def deployment_post():
    name = request.json['dapp_id']
    print(name)
    return 'success'


@api_page.route('/Dodeployment', methods=['GET', 'POST'])
def do_deployment():
    _id = request.json['id']
    print(_id)
    return 'success'


'''
@api_page.route('/add_log', methods=['GET'])
def add_log():
    given_function = request.args.get('function')
    fillEther = request.args.get('fillEther')
    log = {'function':given_function, 'fillEther':fillEther}
    api_page.resource['mongo'].add_user(user)
    return 'Write Success'
'''


'''
@api_page.route('/del_dapp', methods=['GET'])
def del_dapp():
    given_bin = request.args.get('bin')
    dapp = {'bin':given_bin}
    api_page.resource['mongo'].del_dapp(dapp)
    return 'Del Success'
'''


'''
@api_page.route('/find_dapp', methods=['GET'])
def find_dapp():
    given_bin = request.args.get('bin')
    dapp = {'bin':given_bin}
    dapp = api_page.resource['mongo'].find_dapp(dapp)
    return dapp
'''


@api_page.route('/getDApp', methods=['GET', 'POST'])
def dapp_info():
    dapp_id = '5d85ea3933d730c484436266'
    result = api_page.resource['mongo'].find_dapp_by_id(dapp_id)
    if result['code'] == 200:
        abi = result['payload']['abi']
        json_abi = json.loads(abi)
        ret_val = []
        for abi_info in json_abi:
            if abi_info['type'] == 'function':
                function_info = {}
                function_info['name'] = abi_info['name']
                function_info['inputs'] = abi_info['inputs']
                ret_val.append(function_info)

        print(ret_val)
        result = jsonify(ret_val)
        return result
    else:
        return result
