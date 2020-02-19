"uninstall redis: line3,14,15"

import redis
import json
import time

REDIS_IP = 'mj'
REDIS_PORT = 15900
ANSWER_BOARD = 'answerBoard'
ORDER_QUE = 'orderQue'


class MsgHandler:
  def __init__(self):
    self._client = redis.StrictRedis(host=REDIS_IP, port=REDIS_PORT, db=0)

  def put_order(self, order):
    jsonPing = json.dumps(order)
    self._client.lpush(ORDER_QUE, jsonPing)
    print('success')

  def hget_response(self, order):
    ticket = order['ticket']
    resAnswer = self._client.hget(ANSWER_BOARD, ticket)
    if resAnswer is None:
      # if there is proper one for the ticket, it returns 404
      resAnswer = '{"code": 404}'
    return resAnswer

  """
    answer = self._client.hdel(ANSWER_BOARD, answer['ticket'])
    print("complete delete")
  """

  def hget_wait_response(self, order, seconds=30):
    ticket = order['ticket']

    while(seconds > 0):
      resAnswer = self._client.hget(ANSWER_BOARD, ticket)
      if resAnswer is None:
        # if there is proper one for the ticket, it returns 404
        time.sleep(1)
        seconds -= 1
      else:
        return resAnswer
    resAnswer = '{"code": 404}'
    return resAnswer

  def hget_response_with_ticket(self, ticket):
    resAnswer = self._client.hget(ANSWER_BOARD, ticket)
    if resAnswer is None:
      # if there is proper one for the ticket, it returns 404
      resAnswer = '{"code": 300}'
    return resAnswer
