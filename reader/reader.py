class Reader():
    patch = None
    encoding = "utf8"

    def __init__(self, fail, encoding="utf8"):
        self.patch = fail
        self.encoding = encoding

    def __read_v__(self, name):
        with open(self.patch, 'r', encoding=self.encoding) as f:
                all_line = f.readlines()
                for line in all_line:
                    if name == line.split(" ")[0]:
                        return line.split(" ")[1]

    def __write_v__(self, name, var):
        with open(self.patch, 'a', encoding=self.encoding) as f:
            t = "\n"+name+" "+str(var)
            f.write(t)

    def write(self, name,var,start_text="  This file is written in the Reader module from Colden I"):
        if len(name)==len(var):
            with open(self.patch, 'w', encoding=self.encoding) as fa:
                fa.write(start_text)
            for i in range(len(name)):
                self.__write_v__(name[i], var[i])
            return True
        else:
            return False

    def read_int(self, name):
        try:
            res = int(self.__read_v__(name))
        except ValueError:
            return "Reader: read_int Error! -> 'ValueError'"
        else:
            return res

    def read_float(self, name):
        try:
            res = float(self.__read_v__(name))
        except ValueError:
            return "Reader: read_float Error! -> 'ValueError'"
        else:
            return res

    def read(self, name):
        return self.__read_v__(name)