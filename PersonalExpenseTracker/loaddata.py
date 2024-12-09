class DataLoadAndStore:
    __filepath = ""
    def __init__(self, fp):
        self.__filepath = fp
    
    def load(self):
        ret = []
        try:
            with open(self.__filepath, "r") as f:
                add = {}
                lines = f.readlines()
                for i in range(1, len(lines)):
                    fields = lines[i].split(',')
                    add['date'] = fields[0].strip()
                    add['category'] = fields[1].strip()
                    add['amount'] = fields[2].strip()
                    add['description'] = fields[3].strip()
                    ret.append(add)
                return ret
        except FileNotFoundError:
            return ret
    
    def store(self, data):
        with open(self.__filepath, "w+") as f:
            write = []
            write.append("Date,Category,Amount,Description\n")
            for entry in data:
                write.append(f"{entry['date']},{entry['category']},{entry['amount']},{entry['description']}\n")
            f.writelines(write)