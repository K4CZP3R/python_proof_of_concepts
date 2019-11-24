class PhoneLog(object):
    def __init__(self, direction, time):
        self.direction = direction
        self.time = time
    
    @classmethod
    def fromDict(cls, input_dict:dict):
        return cls(input_dict['direction'], input_dict['time'])
    
    def toDict(self) -> dict:
        return self.__dict__

class PhoneLogs(object):
    def __init__(self, logs:list):
        self.logs = logs
    
    @classmethod
    def fromDict(cls, input_dict:dict):
        logs = list()
        for i in input_dict['logs']:
            logs.append(PhoneLog.fromDict(i))
        return cls(logs)
    
    def toDict(self):
        logs = list()
        for log in self.logs:
            logs.append(log.toDict())
        return {'logs': logs}

    def add_log(self, PhoneLog: PhoneLog):
        self.logs.append(PhoneLog)
    
    def get_log(self, i) -> PhoneLog:
        if i > len(self.logs):
            return None
        return self.logs[i]
    def get_logs_amount(self) -> int:
        return len(self.logs)
    
class Phone(object):
    def __init__(self, PhoneLogs: PhoneLogs, phone_number):
        self.PhoneLogs = PhoneLogs
        self.phone_number = phone_number
    
    @classmethod
    def fromDict(cls, input_dict:dict):
        return cls(
            PhoneLogs.fromDict(input_dict['PhoneLogs']),
            input_dict['phone_number']
        )
    
    def toDict(self):
        return {
            'PhoneLogs': self.PhoneLogs.toDict(),
            'phone_number': self.phone_number
        }
