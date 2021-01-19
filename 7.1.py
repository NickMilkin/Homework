class Matrix:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self):
        m_ = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

        for i in range(len(self.m1)):

            for q in range(len(self.m2[i])):
                m_[i][q] = self.m1[i][q] + self.m2[i][q]

        return f'\n'.join(['\t'.join([str(j) for j in i]) for i in m_])


matrix1 = Matrix([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]],
                 [[5, 4, 3],
                  [14, 13, 12],
                  [36, 35, 34]])

print(matrix1.__add__())