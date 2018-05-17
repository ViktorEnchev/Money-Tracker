class Parser:

    def __init__(self, file_name):
        with open(file_name, 'r') as file:
            self._data = file.readlines()

    def get_data(self):
        return self._data
