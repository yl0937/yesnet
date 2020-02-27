#-*- coding:utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo.errors import PyMongoError


class ZenMongo():
    """ 몽고 DB에 접근하는 모든 요청을 처리하는 핸들러 클래스

        Attributes:
        db (MongoDB): MongoDB에 대응되는 db

    """

    def __init__(self, url='mongodb://mj:16900', dbname='yesnet'):
        """ 초기화 함수
        Args:
            url (str): mongodb의 URL, 생성시 지정 가능함.
            dbname (str): 컬렉션이 저장되는 데이터베이스 이름.
       """
        client = MongoClient(url)
        self.db = client[dbname]

    #####################################################
    # core methods
    #####################################################
    def add_one(self, collection, doc):
        """ document를 컬렉션에 추가하는 기본 메서드.

        Args:
            collection: document를 추가할 컬렉션의 이름
            doc: document

        Returns:
            result (dict): 저장 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = {'code': 200}
        try:
            self.db[collection].insert_one(doc)
        except PyMongoError as ex:
            result['code'] = 500
            result['payload'] = str(ex)
        return result

    def del_one(self, collection, query):
        """ document를 컬렉션에서 삭제하는 기본 메서드.

        Args:
            collection: document를 삭제할 컬렉션의 이름
            query: 삭제를 하기 위한 필터

        Returns:
            result (dict): 삭제 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = {'code': 200}
        try:
            self.db[collection].delete_one(query)
        except PyMongoError as ex:
            result['code'] = 500
            result['payload'] = str(ex)
        return result

    def replace_one(self, collection, query, doc):
        """ document를 컬렉션에서 업데이트하기 위한 기본 메서드.

        Args:
            collection: document를 업데이트하기 위한 컬렉션의 이름
            query: document를 업데이트 하기 위한 필터
            doc: 업데이트를 할 document

        Returns:
            result (dict): 업데이트 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = {'code': 200}
        try:
            self.db[collection].replace_one(query, doc)
        except PyMongoError as ex:
            result['code'] = 500
            result['payload'] = str(ex)
        return result

    def find_one(self, collection, query):
        """ document를 컬렉션에서 찾기 위한 기본 메서드.

        Args:
            collection: document를 찾을 컬렉션의 이름
            query: document를 찾기 위한 필터

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 해당 데이터 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = {'code': 200}
        try:
            doc = self.db[collection].find_one(query)
            if doc is None:
                result['code'] = 404
            else:
                for key in doc.keys():
                    if isinstance(doc[key], ObjectId):
                        doc[key] = str(doc[key])
                result['payload'] = doc
        except PyMongoError as ex:
            result['code'] = 500
            result['payload'] = str(ex)
        return result

    def find(self, collection, query):
        """ 여러 document를 컬렉션에서 찾기 위한 기본 메서드.

        Args:
            collection: document를 찾을 컬렉션의 이름
            query: document를 찾기 위한 필터

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 복수개의 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = {'code': 200}
        try:
            count = self.db[collection].count_documents(query)
            if count > 0:
                cursor = self.db[collection].find(query)
                docs = []
                for doc in cursor:
                    for key in doc.keys():
                        if isinstance(doc[key], ObjectId):
                            doc[key] = str(doc[key])
                    docs.append(doc)
                result['payload'] = docs
            else:
                result['code'] = 404
        except PyMongoError as ex:
            result['code'] = 500
            result['payload'] = str(ex)
        return result

    def is_exist(self, collection, query):
        try:
            count = self.db[collection].count_documents(query)
            if count > 0:
                return True
            else:
                return False
        except PyMongoError as ex:
            return False


    #############################################
    # utility methods for users
    #############################################
    def add_user(self, user):
        """ 사용자를 추가

        Args:
            user: 사용자 정보를 담고있는 User 인스턴스

        Returns:
            result (dict): 저장 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        return self.add_one('users', user.get_doc())

    def del_user_by_account(self, account):
        """ 사용자를 account 정보를 이용해서 삭제

        Note:
            보안을 위해서 나중에 account 대신에 session 정보 등을 이용할 필요가 있음.

        Args:
            account: 사용자의 account

        Returns:
            result (dict): 삭제 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'account': account}
        return self.del_one('users', query)

    def del_user_by_id(self, oid):
        """ 사용자를 id 정보를 이용해서 삭제

        Note:
            이게 account로 삭제하는 것보다 보안이 높을 수 있음.

        Args:
            oid: 사용자의 MongoDB document id (_id)

        Returns:
            result (dict): 삭제 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'_id': ObjectId(oid)}
        return self.del_one('users', query)

    def update_user(self, user):
        """ 사용자의 정보를 업데이트

        Args:
            user: 사용자 정보를 담고있는 User 인스턴스

        Returns:
            result (dict): 삭제 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = self.find_user_by_account(user.get_account())
        if result['code'] == 200:
            query = {'account': result['payload']['account']}
            result = self.replace_one('users', query, user.get_doc())
        return result

    def find_user_by_email(self, email):
        """ 사용자를 account로 검색

        Args:
            email: 사용자의 email

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'email': email}
        return self.find_one('users', query)

    def auth_user_by_email(self, email, passwd):
        query = {'email': email, 'logpass': passwd}
        return self.find_one('users', query)

    def find_user_by_account(self, account):
        """ 사용자를 account로 검색

        Args:
            account: 사용자의 account

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'account': account}
        return self.find_one('users', query)

    def find_user_by_id(self, oid):
        """ 사용자를 id로 검색

        Args:
            oid: 사용자의 MongoDB document id (_id)

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'_id': ObjectId(oid)}
        return self.find_one('users', query)

    def auth_user_by_email(self, email, passwd):
        query = {'email': email, 'logpass': passwd}
        return self.find_one('users', query)

    #############################################
    # DAPP utility methods
    #############################################
    def add_dapp(self, dapp):
        """ DApp을 MongoDB에 추가

        Args:
            dapp: 사용자 정보를 담고있는 DApp 인스턴스

        Returns:
            result (dict): 저장 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        return self.add_one('dapps', dapp.get_doc())

    def del_dapp_by_id(self, oid):
        """ DApp을 id 정보를 이용해서 삭제

        Note:
            DApp을 삭제하는 것이 맞는지 잘 모르겠음.
            Disable로 하는 것인 Deployed된 DApp이 있으므로 더 나은 방법이 될 것임.
            나중에 판단할 것.

        Args:
            oid: DApp의 MongoDB document id (_id)

        Returns:
            result (dict): 삭제 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'_id': ObjectId(oid)}
        return self.del_one('dapps', query)

    def find_dapp_by_email(self, email):
        """ DApp을 소유자의 email로 검색

        Args:
            email: 소유자의 email

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 다수의 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = self.find_user_by_email(email)
        if result['code'] == 200:
            print(result['payload']['_id'])
            query = {'user': result['payload']['_id']}
            return self.find('dapps', query)
        else:
            return result

    def find_dapp_by_id(self, oid):
        """ DApp을 DApp의 id로 검색

        Args:
            oid: DApp의 MongoDB document id (_id)

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'_id': ObjectId(oid)}
        return self.find_one('dapps', query)

    #############################################
    # Deployed DAPP utility methods
    #############################################
    def add_deployed(self, deployed):
        """ DApp의 Deploy 정보를 추가

        Args:
            deployed: Deploy 정보를 담고있는 Docu.

        Returns:
            result (dict): 저장 성공시에는 code:200, 애러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        return self.add_one('deploys', deployed)

    def find_deployed_by_account(self, account):
        """ 설치된 DApp을 소유자의 account로 검색

        Args:
            account: 소유자의 account

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 다수의 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = self.find_user_by_account(account)
        if result['code'] == 200:
            query = {'user': result['payload']['_id']}
            return self.find('deploys', query)
        else:
            return result

    def find_deployed_by_id(self, oid):
        """ 설치된 DApp을 설치된 DApp의 id로 검색

        Args:
            oid: 설치된 DApp의 MongoDB document id (_id)

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'_id': ObjectId(oid)}
        result = self.find_one('deploys', query)
        if result['code'] == 200:
            dapp_info = self.find_dapp_by_id(result['payload']['dapp_id'])
            if dapp_info['code'] == 200:
                result['payload']['abi'] = dapp_info['payload']['abi']
            else:
                return dapp_info

        return result

    def find_deployed_by_email(self, email):
        """ 설치된 DApp을 설치된 DApp의 id로 검색

        Args:
            email: 설치된 DApp의 User's email

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'owner_email': email}
        result = self.find('deploys', query)
        if result['code'] == 200:
            ret = {'code': 200}
            payload = []
            for doc in result['payload']:
                print(doc['dapp_id'])
                dapp_info = self.find_dapp_by_id(doc['dapp_id'])
                if dapp_info['code'] == 200:
                    doc['abi'] = dapp_info['payload']['abi']
                    payload.append(doc)
                else:
                    print('No Dapp')
                    return dapp_info
            ret['payload'] = payload
            return ret
        else:
            print("No Deploys")
            return result

    def find_deployed_by_dapp(self, dapp):
        """ 설치된 DApp을 DApp의 id로 검색

        Args:
            dapp: 설치된 DApp에 대응되는 instance

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 다수의 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = self.find_dapp_by_id(dapp['_id'])
        if result['code'] == 200:
            query = {'dapp': ObjectId(result['payload']['_id'])}
            return self.find('deploys', query)
        else:
            return result

    def find_deployed_by_addr(self, addr):
        """ 설치된 DApp을 설치된 주소로 검색

        Args:
            addr: 설치된 DApp의 주소

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        query = {'contact_addr': addr}
        return self.find_one('deploys', query)

    #############################################
    # utility functions for DAPP + Deployed
    #############################################
    def find_deployed_with_dapp(self, addr):
        """ 설치된 DApp을 설치된 주소로 검색하고, dapp 함수 호출을 위한 기본적인 정보를 제공

        Args:
            addr: 설치된 DApp의 주소

        Returns:
            result (dict): 검색 성공시에는 code:200, payload에 query에 맞는 document 반환
                           이때, abi에 대한 정보도 같이 제공함.
                           해당 document가 없으면, code:404 반환
                           에러에는 code:500을 반환하고 payload에 에러메시지 반환

        """
        result = self.find_deployed_by_addr(addr)
        if result['code'] == 200:
            dapp_result = self.find_dapp_by_id(result['payload']['dapp'])
            result['payload']['abi'] = dapp_result['payload']['abi']
        return result