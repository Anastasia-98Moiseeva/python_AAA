from typing import List


class CountVectorizer:

    def __init__(self):
        self.feature_names = []

    def get_feature_names(self) -> List[str]:
        return self.feature_names

    def fit_transform(self, corpus: List[str]) -> List[List[int]]:
        """
        Преобразование корпуса текстов в терм-документную матрицу
        :param corpus: корпус докуметов
        :return: терм-документная матрица
        """
        count_matrix = []
        for text in corpus:
            count_matrix.append(self.count_terms_in_text(text))
        return self.add_nulls_to_matrix_rows(count_matrix)

    def count_terms_in_text(self, text: str) -> List[int]:
        """
        Подсчет количества терминов в тексте
        :param text: текст
        :return: список чисел, в котором каждое число соответствует числу повторений термина в тексте
        """
        terms = text.lower().strip(' \t\r\n').split()
        terms_count = {term: 0 for term in self.feature_names}
        for term in terms:
            if term not in self.feature_names:
                self.feature_names.append(term)
                terms_count.update({term: 1})
            else:
                terms_count.update({term: terms_count.get(term) + 1})
        return list(terms_count.values())

    def add_nulls_to_matrix_rows(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Дополнение строк матрицы нулями
        :param matrix: матрица
        :return: матрица, дополненная нулями
        """
        max_len = self.get_max_row_len_in_matrix(matrix)
        for row in matrix:
            row.extend([0] * (max_len - len(row)))
        return matrix

    def get_max_row_len_in_matrix(self, matrix: List[List[int]]) -> int:
        """
        Нахождение максимальной длинны строки матрицы
        :param matrix: матрица
        :return: максимальная длинна строки
        """
        length_list = [len(row) for row in matrix]
        if not length_list:
            return 0
        return max(length_list)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
