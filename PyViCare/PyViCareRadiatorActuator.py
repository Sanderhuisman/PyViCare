from typing import Any, List

from PyViCare.PyViCareDevice import (Device)
from PyViCare.PyViCareUtils import (handleNotSupported, handleAPICommandErrors)

class RadiatorActuator(Device):

    @handleNotSupported
    def getTemperature(self):
        return self.service.getProperty("device.sensors.temperature")["properties"]["value"]["value"]

    @handleNotSupported
    def getTargetTemperature(self):
        return self.service.getProperty("trv.temperature")["properties"]["value"]["value"]

    @handleAPICommandErrors
    def setTargetTemperature(self, temperature):
        return self.service.setProperty("trv.temperature", "setTargetTemperature", {'temperature': int(temperature)})
