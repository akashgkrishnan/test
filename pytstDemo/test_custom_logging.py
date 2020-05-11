from pytstDemo.baseclass import BaseClass

class TestLogging(BaseClass):
    def test_mainFeature(self, dataload, setup):
        log = self.getlogger()
        log.info(dataload[0])
        log.warning('error customer akash')

        print(dataload[0])

