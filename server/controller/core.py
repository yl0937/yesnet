import time
from web3 import Web3, HTTPProvider
from yesnet.server.config import CONFIG, ResCode
import json
from hexbytes import HexBytes
import web3


class EthCore:
    '''
    Geth와 W3 통신을 하는 클래스임.
    '''

    def __init__(self):
        self.w3 = Web3(HTTPProvider(CONFIG['RPC-URL']))

    # Account를 생성
    def createAccount(self, parameters):
        # create an account
        addr = self.w3.geth.personal.newAccount(parameters['password'])

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        if isinstance(addr, HexBytes):
            retValue['accountAddr'] = addr.hex()
        else:
            retValue['accountAddr'] = addr

        retValue['username'] = parameters['username']
        retValue['gethpass'] = parameters['gethpass']
        retValue['logpass'] = parameters['logpass']
        return retValue

    # Account의 밸런스 값을 조회해서 넘겨주는 루틴
    def getBalance(self, parameters):
        balance = self.w3.eth.getBalance(
            self.w3.toChecksumAddress(parameters['account']))

        # retValue
        retValue = {'code': ResCode.OK.value}
        retValue['account'] = parameters['account']
        retValue['balance'] = balance

        return retValue


    # Get Block
    def getBlock(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        block_info = self.w3.eth.getBlock(parameters['blockNum'])
        ret_info = {}
        for k in block_info:
            if isinstance(block_info[k], list):
                items = []
                for item in block_info[k]:
                    if isinstance(item, HexBytes):
                        items.append(item.hex())
                    else:
                        items.append(item)
                ret_info[k] = items
            elif isinstance(block_info[k], HexBytes):
                ret_info[k] = block_info[k].hex()
            else:
                ret_info[k] = block_info[k]
        print(ret_info)

        retValue = {'code': ResCode.OK.value}
        retValue['blockInfo'] = ret_info
        return retValue

    # Get Tx
    def getTx(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        ret_info = {}
        tx_info = self.w3.eth.getTransaction(parameters['txHash'])
        if tx_info:
            for k in tx_info:
                if isinstance(tx_info[k], HexBytes):
                    ret_info[k] = tx_info[k].hex()
                else:
                    ret_info[k] = tx_info[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['txInfo'] = ret_info
        return retValue

    # Function를 호출함. Call Function임.
    def callFunction(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
            parameters['account']), parameters['gethpass'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = parameters['contractAddress']

        # abi 인터페이스,
        abi = json.loads(parameters['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        funx = contract_instance.functions[parameters['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in parameters:
            kwargs = parameters['kwargs']
            result = funx(**kwargs).call()
        else:
            result = funx().call()

        print(result)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = result
        print(retValue)

        return retValue

    # Method를 호출함. Tx Method .
    def callTx(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
            parameters['account']), parameters['gethpass'], 0)

        # # 원래는 바이트 이어야 하므로 hex 값에서 바이트 코드로 변경
        # tx_hash = bytes.fromhex(parameters['txHash'])
        #
        # # receipt get
        # tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)

        # contract의 주소를 얻음.
        contract_address = self.w3.toChecksumAddress(parameters['contractAddress'])

        # abi 인터페이스,
        abi = json.loads(parameters['abi'])

        # Contract 인스턴스를 생성
        contract_instance = self.w3.eth.contract(
            address=contract_address,
            abi=abi
        )

        # 함수를 이름을 이용해서 함수 객체를 얻음
        # funx = contract_instance.find_functions_by_name(parameters['functionName'])
        # print(funx)
        funx = contract_instance.functions[parameters['functionName']]
        # result = contract_instance.functions.greet().call()
        # func = getattr(contract_instance.call(), parameters['functionName'])
        # print(contract_instance.call())
        # print('Contract: {}'.format(contract_instance.call().greet()))

        # get parameters
        if 'kwargs' in parameters:
            kwargs = parameters['kwargs']
            txhash = funx(**kwargs).transact({'from': self.w3.toChecksumAddress(parameters['account'])})
        else:
            print('No arguments')
            txhash= funx().transact({'from': self.w3.toChecksumAddress(parameters['account'])})

        tx_receipt = self.w3.eth.waitForTransactionReceipt(txhash)
        print('receipt', tx_receipt)
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['return'] = 'success'
        return retValue


    # DApp을 Deployment

    def deployDApp(self, payload):
        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        self.w3.eth.defaultAccount = self.w3.toChecksumAddress(parameters['account'])

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        self.w3.geth.personal.unlockAccount(self.w3.toChecksumAddress(
            parameters['account']), parameters['passwd'], 0)

        # contract 생성
        print(type(parameters['bin']), ":", parameters['bin'])
        contract = self.w3.eth.contract(abi=parameters['abi'], bytecode=parameters['bin'])

        tx_hash = contract.constructor().transact()

        tx_receipt = self.w3.eth.waitForTransactionReceipt(tx_hash)

        # contract_address = tx_receipt['contractAddress']

        # deploy 요청에 의거한 tx hash
        # tx_hash = contract.deploy(
        #     transaction={'from': self.w3.toChecksumAddress(parameters['account'])})
        # print("tx_hash: {}".format(tx_hash.hex()))
        # print("Finish Deploying")
        #           
        # # 블록이 채굴되기 전에 바로 contract를 요청할 수 없으므로, 기다려야 함.
        # while True:
        #     # 블록에서 hash가 들어있는 블록이 있는지 요청
        #     tx_receipt = self.w3.eth.getTransactionReceipt(tx_hash)
        #
        #     # 아직 채굴 전
        #     if tx_receipt is None:
        #         time.sleep(1)
        #         print("waiting")
        #         continue
        #
        #     # 채굴 완료
        #     print(tx_receipt)
        #     contract_address = tx_receipt['contractAddress']
        #     print(contract_address)
        #
        #     break

        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        ret_info = {}
        if tx_receipt:
            for k in tx_receipt:
                if isinstance(tx_receipt[k], HexBytes):
                    ret_info[k] = tx_receipt[k].hex()
                else:
                    ret_info[k] = tx_receipt[k]
            print(ret_info)
        else:
            ret_info['txInfo'] = 'None'

        retValue = {'code': ResCode.OK.value}
        retValue['dapp_id'] = parameters['dapp_id']
        retValue['deployResult'] = ret_info
        print(retValue)

        return retValue


    def fillEth(self, payload):

        # unlock Adam's pass
        adam_account = self.w3.toChecksumAddress(CONFIG['ADAM'])
        self.w3.geth.personal.unlockAccount(adam_account, 'yes36%')

        # 파라미터를 먼저 얻음.
        parameters = payload['params']

        args = {}
        args['to'] = self.w3.toChecksumAddress(parameters['to'])
        args['from'] = adam_account
        args['value'] = parameters['amount']* pow(10 ,18)

        # 해당 사용자의 패스워드를 이용해서 Unlock 함.
        tx_addr = self.w3.eth.sendTransaction(args)
        print(tx_addr)

        self.w3.eth.waitForTransactionReceipt(tx_addr)

        balance = self.w3.eth.getBalance(args['to'] )

        # retValue
        # 현재는 그냥 100% 성공이라고 했음.
        # 실제로는 에러 처리 코드가 필요함
        retValue = {'code': ResCode.OK.value}
        retValue['balance'] = balance

        return retValue
