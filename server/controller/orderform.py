from server.controller.redisfunction import MsgHandler

ORDERPING = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "ping",
  "params": {
       "msg": "hello"
}}

ORDERgetBalance = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "getBalance",
  "params": {
       "account": "0xb3b4ef17ba517e75b79169354fd9dfff51b9d592"
}
}

ORDERgetTx = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "getTx",
  "params": {
       "txHash": "0x6e8d413365fe89f9b6bcbeebc9748e4686657626ba996bb8b38b45fef673bbff"
}}


ORDERfillEth = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "fillEth",
  "params": {
       "to":  "0xd7430ee70ec72a72c4b5acc2710a59edc17b552f",
       "amount": 100
}}


ORDERgetTx = {
  "ticket": "20190814065206123456",
  "timestamp": 1562069915.0,
  "uid": "dilab@gmail.com",
  "cmd": "getTx",
  "params": {
       "txHash": "0x6e8d413365fe89f9b6bcbeebc9748e4686657626ba996bb8b38b45fef673bbff"
}}


ORDERgetBlock = {
    "ticket": "20190814065206123456",
    "timestamp": 1562069915.0,
    "uid": "dilab@gmail.com",
    "cmd": "getBlock",
    "params": {
        "blockNum": 852
   }
}


msg = MsgHandler()

msg.put_order(ORDERPING)
msg.hget_response(ORDERPING)