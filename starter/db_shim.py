# -*- coding: utf-8 -*-

class DBShim:
    def __init__(self):
        self.customer = [
            {
                "id": 1,
                "name": "First",
                "gender": "m",
                "uid": "CNT0001",
            },
            {
                "id": 2,
                "name": "Second",
                "gender": "m",
                "uid": "CNT0002",
            },
            {
                "id": 3,
                "name": "Third",
                "gender": "f",
                "uid": "CNT0003",
            },
            {
                "id": 4,
                "name": "Fourth",
                "gender": "m",
                "uid": "CNT0004",
            },
        ]
        self.order = [
            {
                "id": 11,
                "client": 1,
                "number": "ORD000011",
            },
            {
                "id": 12,
                "client": 3,
                "number": "ORD000012",
            },
            {
                "id": 13,
                "client": 3,
                "number": "ORD000013",
            },
        ]

class OrderModel(object):
    """docstring for Order"""

    @staticmethod
    def init_with_id(id):
        db = DBShim()
        return OrderModel(db.order[id])

    def __init__(self, data):
        super(OrderModel, self).__init__()
        if data:
            self.id = data["id"]
            self.client = data["client"]
            self.number = data["number"]

    def all(self):
        return DBShim().order

    def one(self, num):
        for x in DBShim().order:
            if x["id"] == num:
                return x
        return {}


class Customer(object):
    """docstring for Customer"""
    def __init__(self, data):
        super(Customer, self).__init__()
        self.id = data["id"]
        self.name = data["name"]
        self.gender = data["gender"]

    def one(self, uid):
        for x in DBShim().customer:
            if x["uid"] == uid:
                return x
        return {}

