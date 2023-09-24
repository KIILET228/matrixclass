from random import randint, choice


class Matrix:
    """Это класс для создания матриц и работы с ними"""
    aplphabet = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    empty = "Пустой"
    null = "Нулевой"
    num = "Числовой"
    let = "Буквенный"
    word = "Словесный"

    def __init__(self, Width: int, Height: int, matrix=list(), type="Пустой"):
        self.Width = Width
        self.Height = Height
        self.matrix = matrix
        self.type = type

    def create_null_matrix(self):
        self.matrix = [[0 for i in range(self.Width)] for o in range(self.Height)]
        self.type = Matrix.null

    def create_random_numbers_matrix(self, a, b):
        self.matrix = [[randint(a, b) for i in range(self.Width)] for o in range(self.Height)]
        self.type = Matrix.num

    def create_random_letters_matrix(self):
        self.matrix = [[choice(Matrix.aplphabet) for i in range(self.Width)] for o in range(self.Height)]
        self.type = Matrix.let

    def create_random_words_matrix(self, lenght):
        self.matrix = [["".join([choice(Matrix.aplphabet) for i in range(lenght)]) for i in range(self.Width)] for o in
                       range(self.Height)]
        self.type = Matrix.word

    def print_matrix(self):
        maxlen = 0
        for row in self.matrix:
            for el in row:
                maxlen = max(len(str(el)), maxlen)
        for row in self.matrix:
            for el in row:
                print(str(el).center(maxlen+2, " "), end="")
            print()

    def change_matrix_size(self, width, height):
        self.Width = width
        self.Height = height
        matrixcopy = self.matrix.copy()

        if self.type == Matrix.empty:
            self.create_null_matrix()
        elif self.type == Matrix.null:
            self.create_null_matrix()
        elif self.type == Matrix.num:
            maxnum = 0
            minnum = matrixcopy[0][0]
            for row in matrixcopy:
                for el in row:
                    maxnum = max(el, maxnum)
                    minnum = min(el, minnum)

            self.create_random_numbers_matrix(minnum, maxnum)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if i < len(matrixcopy) and j < len(matrixcopy[0]):
                        self.matrix[i][j] = matrixcopy[i][j]
        elif self.type == Matrix.let:
            self.create_random_letters_matrix()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if i < len(matrixcopy) and j < len(matrixcopy[0]):
                        self.matrix[i][j] = matrixcopy[i][j]

        elif self.type == Matrix.word:
            maxlen = 0
            for row in matrixcopy:
                for el in row:
                    maxlen = max(len(el), maxlen)
            self.create_random_words_matrix(maxlen)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    if i < len(matrixcopy) and j < len(matrixcopy[0]):
                        self.matrix[i][j] = matrixcopy[i][j]


    def summ_matrixes(self, matrix_for_summ):
        if self.type == matrix_for_summ.type \
                and Matrix.empty not in [self.type, matrix_for_summ.type] \
                and self.Width == matrix_for_summ.Width \
                and self.Height == matrix_for_summ.Height:
            global_list = []
            for i in range(self.Height):
                inside_list = [self.matrix[i][j] + matrix_for_summ.matrix[i][j] for j in range(self.Width)]
                global_list.append(inside_list)
            new_matrix = Matrix(self.Width, self.Height, global_list, self.type)
            return new_matrix

    def multiplication_matrixes(self, matrix_for_multiply):
        if (self.type in [Matrix.null, Matrix.num] or matrix_for_multiply.type in [Matrix.null, Matrix.num]) \
                and Matrix.empty not in [self.type, matrix_for_multiply.type] \
                and self.Width == matrix_for_multiply.Width \
                and self.Height == matrix_for_multiply.Height:
            global_list = []
            for i in range(self.Height):
                inside_list = [self.matrix[i][j] * matrix_for_multiply.matrix[i][j] for j in range(self.Width)]
                global_list.append(inside_list)
            new_matrix = Matrix(self.Width, self.Height, global_list, self.type)
            return new_matrix



matrix1 = Matrix(5, 5)
matrix1.create_random_words_matrix(5)
matrix1.print_matrix()
print()
matrix1.change_matrix_size(3, 10)
matrix1.print_matrix()