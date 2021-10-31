import math
from typing import List


class TfIdfTransformer:
    def __init__(self):
        pass

    def tf_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Tf преобразование матрицы
        :param count_matrix: матрица
        :return: результат преобразования
        """
        tf_matrix = []
        for row in count_matrix:
            tf_row = []
            num = sum(row)
            for item in row:
                tf_row.append(round(item / num, 3))
            tf_matrix.append(tf_row)
        return tf_matrix

    def idf_transform(self, count_matrix: List[List[int]]) -> List[float]:
        """
        Idf преобразование матрицы
        :param count_matrix: матрица
        :return: результат преобразования
        """
        idf = [0.0] * len(count_matrix[0])
        num_docs = len(count_matrix) + 1
        for j in range(len(count_matrix[0])):
            docs_with_word = 0
            for i in range(len(count_matrix)):
                docs_with_word += (count_matrix[i][j] != 0)
                idf[j] = round(math.log(num_docs / (docs_with_word + 1)) + 1, 1)
        return idf

    def fit_transform(self, count_matrix: List[List[int]]) -> List[List[float]]:
        """
        Tf-idf преобразование матрицы
        :param count_matrix: матрица
        :return: результат преобразования
        """
        tf = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])
        return tf_idf

