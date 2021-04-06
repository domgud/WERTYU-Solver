class Converter:

    def __init__(self, rows):
        self.__rows = rows.copy()

    def convert(self, _input):
        """
        Shifts each symbol in given text by one position to the left by QWERTY keyboard keys locations
        :param _input: input text
        :return: text shifted to the left
        """

        output = ""
        for letter in _input:
            if letter == ' ':
                output += letter
                continue

            index = self.find_index(letter)
            #print(self.__rows[index[0]][index[1]])
            output += self.find_symbol(index)
            #print(self.__rows[index[0]][index[1]-1])

        return output

    def find_index(self, symbol):
        """
        Finds symbol indexes in 2d array
        :param symbol: Symbol
        :return: [i, j] coordinates in 2d array
        """
        for i, rows in enumerate(self.__rows):
            for j, item in enumerate(rows):
                if item == symbol:
                    return [i, j]

    def find_symbol(self, index):
        """

        :param index: coordinates of original symbol
        :return: symbol shifted to the left
        """
        return self.__rows[index[0]][index[1]-1]
