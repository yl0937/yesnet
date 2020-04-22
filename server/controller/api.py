import json

from bson import json_util
from flask import Blueprint, render_template, abort, jsonify, request, redirect, session, url_for
from flask import current_app as app
# import bcrypt
from pymongo import MongoClient, collection

from yesnet.server.controller import redisfunction
from yesnet.server.models.database import ZenMongo
from yesnet.server.models.dom import DApp

from yesnet.server.utils import zen_util
from functools import wraps
from datetime import timedelta, datetime
import jwt
from flask import Response
from yesnet.server.models.dom import User

# Zen
from yesnet.server.controller.core import EthCore
core = EthCore()
# Zen

from yesnet.server.controller.redisfunction import MsgHandler
# from app.models.database import LoginAPI

api_page = Blueprint('api_page', 'api_page', template_folder='templates')
api_page.resource = {'JWT_SECRET_KEY': '8akdjfl*#Q@OS)_Dkljdlkdja'}



def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(request.headers)
        access_token = request.headers.get('Authorization')
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, api_page.resource['JWT_SECRET_KEY'], 'HS256')
            except jwt.InvalidTokenError as ex:
                payload = None
                print(ex)

            if payload is None:
                print('111')
                return Response(status=401)

            email = payload['email']
            kwargs['email'] = email
        else:
            print('222')
            return Response(status=401)

        return f(*args, **kwargs)

    return decorated_function

# Login Check
@api_page.route('/login', methods=['POST'])
def login():
    login_email = request.json['email']
    # login_pwd = bcrypt.hashpw(request.json['password'].encode('UTF-8'), bcrypt.gensalt())
    login_pwd = request.json['password'].encode('UTF-8')
    login_pass = login_pwd.decode('ascii')

    # get a hash pwd from the given pwd
    # hashed_pwd = bcrypt.hashpw(login_pwd, bcrypt.gensalt())

    # compare it with DB
    result = api_page.resource['mongo'].auth_user_by_email(login_email, login_pass)
    if result['code'] == 200:
        # Login Success
        payload = {
            'email': login_email,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60)
        }
        token = jwt.encode(payload, api_page.resource['JWT_SECRET_KEY'], 'HS256')
        return jsonify({
            'code': 200,
            'access_token': token.decode('UTF-8')
        })

    else:
        # Login Fail
        return jsonify({
            'code': 404
        })


# Regiser
@api_page.route('/register', methods=['POST'])
def register():
    # get parameters
    username = request.json['username']
    email = request.json['Email']
    logpass = request.json['password']
    gethpass = logpass + 'xaaa'

    # call core
    params = {'password': gethpass, 'username': username, 'logpass': logpass, 'gethpass': gethpass}
    result = core.createAccount(params)

    # get account addr
    account = result['accountAddr']
    user = User(account, username, email, logpass, gethpass)

    # add user to db
    result = api_page.resource['mongo'].add_user(user)
    result = {'code': 200}
    response = json.dumps(result, default=json_util.default)
    return response


@api_page.route('/balance', methods=['GET'])
@login_required
def getbalance(*args, **kwargs):
    email = request.headers.get('email')

    user_info = api_page.resource['mongo'].find_user_by_email(email)

    if user_info['code'] == 200:

        # get params
        print(user_info)

        payload = user_info['payload']
        parameters = { }
        parameters['account'] = payload['account']

        # call core
        result = core.getBalance(parameters)
        response = json.dumps(result, default=json_util.default)
        return response
    else:
        return user_info


# Watch Tx
@api_page.route('/watchtx', methods=['GET', 'POST'])
@login_required
def gettx(*args, **kwargs):

    # get params
    email = kwargs['email']
    print('getTx:', email)
    txHash = request.json['txHash']
    params = {"txHash": txHash}
    print(params)


    # call core
    payload = {'params' : params}
    result = core.getTx(payload)

    response = json.dumps(result, default=json_util.default)
    return response


# Watch Block
@api_page.route('/watchblock', methods=['GET', 'POST'])
@login_required
def getblock(*args, **kwargs):

    # get params
    email = kwargs['email']
    print('getBlock:', email)

    blockNum = request.json['blockNum']
    #blockNum = 852

    params = {"blockNum": blockNum}


    payload = {'params': params}
    print(payload)

    # call core
    result = core.getBlock(payload)
    response = json.dumps(result, default=json_util.default)
    return response


@api_page.route('/show_dapp', methods=['GET', 'OPTIONS'])
@login_required
#def json_default(value):
#    if isinstance(value):
#        return value.strftime('%Y-%m-%d %H:%M:%S')
def show_dapp(*args, **kwargs):
    email = kwargs['email']

    results = api_page.resource['mongo'].find_dapp_by_email(email)
    # print(type(results), ":", results)
    response = json.dumps(results, default=json_util.default)
    print(response)

    return response


@api_page.route('/add_dapp', methods=['GET', 'POST'])
@login_required
def add_dapp(*args, **kwargs):
    email = kwargs['email']

    result = api_page.resource['mongo'].find_user_by_email(email)
    if result['code'] == 200:
        user = result['payload']
        name = request.json['name']
        desc = request.json['desc']
        abi = request.json['abi']
        binary = request.json['bin']
        dapp = DApp(user, name, desc, abi, binary)
        result = api_page.resource['mongo'].add_dapp(dapp)

    print(result)
    ret_val = jsonify(result)
    print(ret_val)
    return ret_val


@api_page.route('/deploymentPost', methods=['GET', 'POST'])
@login_required
def deploy(*args, **kwargs):
    email = kwargs['email']

    print('deploymentPost:', email)
    dapp_id = request.json['dapp_id']

    user_info = api_page.resource['mongo'].find_user_by_email(email)
    if user_info['code'] == 200:
        dapp_info = api_page.resource['mongo'].find_dapp_by_id(dapp_id)
        if dapp_info['code'] == 200:
            # get params
            params = {'account': user_info['payload']['account'],
                      'passwd': user_info['payload']['gethpass'],
                      'app_name': dapp_info['payload']['name'],
                      'bin': dapp_info['payload']['bin'],
                      'abi': dapp_info['payload']['abi'],
                      'dapp_id': dapp_id}

            payload = {'params': params}

            # call core
            result = core.deployDApp(payload)
            response = json.dumps(result, default=json_util.default)
            return response
        else:
            return dapp_info
    else:
        return user_info

# use it?
@api_page.route('/getTicketDeploy', methods=['GET','POST'])
@login_required
def getTicketDeploy(*args, **kwargs):
    email = kwargs['email']
    ticket = request.json['ticket']
    msg = redisfunction.MsgHandler()
    response = msg.hget_response_with_ticket(ticket)
    json_res = json.loads(response)
    result = json_res['result']
    ret = {'code': result['code']}
    if result['code'] != 200:
        ret['err_name'] = result['err_name']
        ret['reason'] = result['reason']
        return jsonify(ret)
    else:
        deployResult = result['deployResult']
        deployed = {
            'dapp_id': deployResult['dapp_id'],
            'owner_email': email,
            'blockHash': deployResult['blockHash'],
            'blockNumber': deployResult['blockNumber'],
            'contractAddress': deployResult['contractAddress'],
            'gasUsed': deployResult['gasUsed'],
            'transactionHash': deployResult['transactionHash'],
            'timestamp': zen_util.get_timestamp()
        }
        api_page.resource['mongo'].add_deployed(deployed)

    return response


# @api_page.route('/getTicketRegister', methods=['GET','POST'])
# @login_required
# def getTicketRegister(*args, **kwargs):
#     email = kwargs['email']
#     ticket = request.json['ticket']
#
#     msg = redisfunction.MsgHandler()
#     response = msg.hget_response_with_ticket(ticket)
#     json_res = json.loads(response)
#     result = json_res['result']
#     if result['code'] == 200:
#         # request to make an user to yescore
#         account = result['accountAddr']
#         username = result['username']
#         logpass = result['logpass']
#         gethpass = result['gethpass']
#         user = User(account, username, email, logpass, gethpass)
#         result = api_page.resource['mongo'].add_user(user)
#
#     return jsonify(result)

@api_page.route('/fill_eth', methods=['GET'])
@login_required
def fill_eth(*args, **kwargs):
    email = kwargs['email']

    user_info = api_page.resource['mongo'].find_user_by_email(email)
    if user_info['code'] == 200:
        # get params
        params = {
                "to": user_info['payload']['account'],
                "amount": 100
            }

        payload = {"params": params}

        # call core
        result = core.fillEth(payload)
        response = json.dumps(result, default=json_util.default)
        return response
    else:
        return user_info


@api_page.route('/dapp_list', methods=['GET'])
def dappList():
    account = request.args.get('account')
    result = api_page.resource['mongo'].find_dapp_by_account(account)
    if result['code'] == 200:
        # Success
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

        # get params
        params = {
            "txHash": "0x6e8d413365fe89f9b6bcbeebc9748e4686657626ba996bb8b38b45fef673bbff"
        }
        payload = {"params": params}

        # call core
        result = core.getTx(payload)
        return result & redirect('/')
    else:
        return 'success!'


@api_page.route('/txtTojson', methods=['POST', 'GET'])
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



@api_page.route('/DK', methods=['POST', 'GET'])
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


@api_page.route('/Dodeployment', methods=['GET', 'POST'])
def do_deployment():
    _id = request.json['id']
    print(_id)
    return 'success'


@api_page.route('/getDApp', methods=['GET'])
@login_required
def dapp_info(*args, **kwargs):
    email = kwargs['email']
    print('getDApp:', email)
    # dapp_id = '5dc2a54489335fa2468dd71c'
    # result = api_page.resource['mongo'].find_deployed_by_id(dapp_id)
    result = api_page.resource['mongo'].find_deployed_by_email(email)
    if result['code'] == 200:
        payload = result['payload']
        for doc in payload:
            abi = doc['abi']
            json_abi = json.loads(abi)
            ret_val = []
            for abi_info in json_abi:
                if abi_info['type'] == 'function':
                    function_info = {}
                    function_info['name'] = abi_info['name']
                    function_info['inputs'] = abi_info['inputs']
                    function_info['constant'] = abi_info['constant']
                    ret_val.append(function_info)
            print(ret_val)
            doc['funtions'] = ret_val
            # {payload: [{timestamp:},{timestamp:} ]
        response = json.dumps(result, default=json_util.default)
        return response
    else:
        response = json.dumps(result, default=json_util.default)
        return response


@api_page.route('/callFunction', methods=['GET', 'POST'])
def call_function():
    # todo begins
    # need to set UID
    #uid = request.json['uid']
    email = "anyang@gmail.com"
    # todo ends

    result = api_page.resource['mongo'].find_user_by_email(email)
    print(result)
    if result['code'] == 200:
        account = result['payload']['account']
        gethpass = result['payload']['gethpass']

        contractAddr = request.json['contractAddress']
        functionName = request.json['functionName']
        abi = request.json['abi']

        # get params
        params = {"contractAddress": contractAddr, "functionName": functionName, "abi": abi}
        params['account'] = account
        params['gethpass'] = gethpass
        if 'args' in request.json:
            kwargs = {}
            # there are arguments in the function.
            args = request.json['args']
            for arg_name, arg_val in args.items():
                kwargs[arg_name] = arg_val
            params['kwargs'] = kwargs

        payload = {"params": params}

        # call core
        result = core.callFunction(payload)
        response = json.dumps(result, default=json_util.default)
        return response
    else:
        return json.dumps(result)


@api_page.route('/callTx', methods=['GET', 'POST'])
def tx_function():
    # todo begins
    # need to set UID
    #uid = request.json['uid']
    email = "anyang@gmail.com"
    # todo ends

    result = api_page.resource['mongo'].find_user_by_email(email)
    print(result)
    if result['code'] == 200:
        account = result['payload']['account']
        gethpass = result['payload']['gethpass']

        contractAddr = request.json['contractAddress']
        functionName = request.json['functionName']
        abi = request.json['abi']

        # get params
        params = {"contractAddress": contractAddr, "functionName": functionName, "abi": abi}
        params['account'] = account
        params['gethpass'] = gethpass
        if 'args' in request.json:
            kwargs = {}
            # there are arguments in the function.
            args = request.json['args']
            for arg_name, arg_val in args.items():
                kwargs[arg_name] = arg_val
            params['kwargs'] = kwargs

        payload = {"params": params}

        # call core
        result = core.callTx(payload)
        response = json.dumps(result, default=json_util.default)
        return response
    else:
        return json.dumps(result)


@api_page.route('/dummyCall', methods=['GET', 'POST'])
@login_required
def dummycall(*args, **kwargs):
    email = kwargs['email']
    print('dummyCall:', email)
    blockNum = request.json['blockNum']

    #get params
    payload = {"blockNum": blockNum}

    # call core
    result = core.getBlock(payload)
    response = json.dumps(result, default=json_util.default)
    return response


@api_page.route('/getTicket', methods=['GET','POST'])
@login_required
def getTicket(*args, **kwargs):
    ticket = request.json['ticket']
    msg = redisfunction.MsgHandler()
    response = msg.hget_response_with_ticket(ticket)
    return response
