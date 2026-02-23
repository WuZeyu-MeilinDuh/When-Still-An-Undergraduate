# Question 1 3x3 matrix
# Please DO NOT modify the given function except the TODO part
# You may have your own functions if necessary

class Matrix3x3:
    def __init__(self, matrix):
        """
        Initialize the 3x3 matrix.
        :param matrix: A list of lists representing a 3x3 matrix.
        """
        self.matrix = matrix

    def add(self, other):
        """
        Add two 3x3 matrices.
        :param other_matrix: Another Matrix3x3 object.
        :return: A new 3x3 matrix that is the sum of self and other.
        """
        # TODO: Implement matrix addition

        c11 = self.matrix[0][0] * other.matrix[0][0] + self.matrix[0][1] * other.matrix[1][0] + self.matrix[0][2] * other.matrix[2][0]
        c12 = self.matrix[0][0] * other.matrix[0][1] + self.matrix[0][1] * other.matrix[1][1] + self.matrix[0][2] * other.matrix[2][1]
        c13 = self.matrix[0][0] * other.matrix[0][2] + self.matrix[0][1] * other.matrix[1][2] + self.matrix[0][2] * other.matrix[2][2]

        c21 = self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0] + self.matrix[1][2] * other.matrix[2][0]
        c22 = self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1] + self.matrix[1][2] * other.matrix[2][1]
        c23 = self.matrix[1][0] * other.matrix[0][2] + self.matrix[1][1] * other.matrix[1][2] + self.matrix[1][2] * other.matrix[2][2]

        c31 = self.matrix[2][0] * other.matrix[0][0] + self.matrix[2][1] * other.matrix[1][0] + self.matrix[2][2] * other.matrix[2][0]
        c32 = self.matrix[2][0] * other.matrix[0][1] + self.matrix[2][1] * other.matrix[1][1] + self.matrix[2][2] * other.matrix[2][1]
        c33 = self.matrix[2][0] * other.matrix[0][2] + self.matrix[2][1] * other.matrix[1][2] + self.matrix[2][2] * other.matrix[2][2]

        return [[c11, c12, c13], [c21,c22,c23], [c31, c32, c33]]

    def subtract(self, other):
        """
        Subtract one 3x3 matrix from another.
        :param othermatrix: Another Matrix3x3 object.
        :return: A new 3x3 matrix that is the difference of self and other.
        """
        # TODO: Implement matrix subtraction

        c11 = self.matrix[0][0] - other.matrix[0][0]
        c12 = self.matrix[0][1] - other.matrix[0][1]
        c13 = self.matrix[0][2] - other.matrix[0][2]

        c21 = self.matrix[1][0] - other.matrix[1][0]
        c22 = self.matrix[1][1] - other.matrix[1][1]
        c23 = self.matrix[1][2] - other.matrix[1][2]

        c31 = self.matrix[2][0] - other.matrix[2][0]
        c32 = self.matrix[2][1] - other.matrix[2][1]
        c33 = self.matrix[2][2] - other.matrix[2][2]

        return [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]

    def multiply(self, other):
        """
        Multiply two 3x3 matrices.
        :param other: Another Matrix3x3 object.
        :return: A new 3x3 matrix that is the product of self and other.
        """
        # TODO: Implement matrix multiplication

        c11 = self.matrix[0][0]*other.matrix[0][0] + self.matrix[0][1]*other.matrix[1][0] + self.matrix[0][2]*other.matrix[2][0]
        c12 = self.matrix[0][0]*other.matrix[0][1] + self.matrix[0][1]*other.matrix[1][1] + self.matrix[0][2]*other.matrix[2][1]
        c13 = self.matrix[0][0]*other.matrix[0][2] + self.matrix[0][1]*other.matrix[1][2] + self.matrix[0][2]*other.matrix[2][2]

        c21 = self.matrix[1][0] * other.matrix[0][0] + self.matrix[1][1] * other.matrix[1][0] + self.matrix[1][2] * other.matrix[2][0]
        c22 = self.matrix[1][0] * other.matrix[0][1] + self.matrix[1][1] * other.matrix[1][1] + self.matrix[1][2] * other.matrix[2][1]
        c23 = self.matrix[1][0] * other.matrix[0][2] + self.matrix[1][1] * other.matrix[1][2] + self.matrix[1][2] * other.matrix[2][2]

        c31 = self.matrix[2][0] * other.matrix[0][0] + self.matrix[2][1] * other.matrix[1][0] + self.matrix[2][2] * other.matrix[2][0]
        c32 = self.matrix[2][0] * other.matrix[0][1] + self.matrix[2][1] * other.matrix[1][1] + self.matrix[2][2] * other.matrix[2][1]
        c33 = self.matrix[2][0] * other.matrix[0][2] + self.matrix[2][1] * other.matrix[1][2] + self.matrix[2][2] * other.matrix[2][2]

        return [[c11, c12, c13], [c21, c22, c23], [c31, c32, c33]]

    def determinant(self):
        """
        Calculate the determinant of the 3x3 matrix.
        :return: A float or int representing the determinant of the matrix.
        """
        # TODO: Implement determinant calculation

        x = self.matrix[0][0] * (self.matrix[1][1]*self.matrix[2][2] - self.matrix[1][2]*self.matrix[2][1])
        y = self.matrix[0][1] * (self.matrix[1][0] * self.matrix[2][2] - self.matrix[1][2] * self.matrix[2][0])
        z = self.matrix[0][2] * (self.matrix[1][0] * self.matrix[2][1] - self.matrix[1][1] * self.matrix[2][0])

        return x - y + z

# Example usage
if __name__ == '__main__':
    matrix1 = Matrix3x3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = Matrix3x3([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

    # Students should complete the implementation and test the methods
    # print("Addition result:", matrix1.add(matrix2))
    # print("Subtraction result:", matrix1.subtract(matrix2))
    # print("Multiplication result:", matrix1.multiply(matrix2))
    # print("Determinant:", matrix1.determinant())