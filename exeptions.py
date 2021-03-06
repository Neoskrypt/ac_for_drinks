
class BaseError(Exception):
    def __init__(self,reason:str):
        self._reason = reason
class DrinkAlreadyExists(BaseError):
    def __init__(self,reason):
        super().__init__(reason)
    def __str__(self):
        return "The drink already exists {}".format(self._reason)
class InvalidVol(BaseError):
    def __init__(self,reason):
        super().__init__(reason)
    def __str__(self):
        return "incorrect value of volume \nof drink for replenishment{}".format(self._reason)
class NotFound(BaseError):
    def __init__(self,reason):
        super().__init__(reason)
    def __str__(self):
        return "The drink not found {}".format(self._reason)
class PassArgs(BaseError):
    def __init__(self,reason):
        super().__init__(reason)
    def __str__(self):
        return "Error in the passed arguments {}".format(self._reason)
