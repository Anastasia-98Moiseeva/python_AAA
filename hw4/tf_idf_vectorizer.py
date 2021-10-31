from typing import List
from count_vectorizer import CountVectorizer
from tf_idf_transformer import TfIdfTransformer


class TfIdfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfIdfTransformer()

    def fit_transform(self, corpus: List[str]) -> List[List[float]]:
        """
        Tf-idf преобразование корпуса текстов
        :param corpus: корпуст текстов
        :return:результат преобразования
        """
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    tfIdf_vectorizer = TfIdfVectorizer()
    tfIdf_matrix = tfIdf_vectorizer.fit_transform(corpus)
    print(tfIdf_matrix)