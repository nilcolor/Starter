# -*- coding: utf-8 -*-
from starter.db_shim import OrderModel

class RepairOrder(object):
    """
    """

    def __init__(self):
        super(RepairOrder, self).__init__()
        self.records_limit = 2
        self._model = None

    def getModel(self):
        if not self._model:
            self._model = OrderModel(None)
        return self._model

    def getListOfRepairOrders(self):
        model = self.getModel()
        data = model.all()[:self.records_limit]
        return data

    def getRepairOrderForID(self, rid):
        model = self.getModel()
        data = model.one(rid)
        return data

    def createNewRepairOrder(self, data):
        model = self.getModel()
        # do something to add new record...
        data["id"] = 11 # is it looks strange? it is...
        return model.one(data["id"])

