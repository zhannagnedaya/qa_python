from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    def test_add_added_book_book_not_added(self):  # нельзя добавить одну и ту же книгу дважды
        collector = BooksCollector()
        collector.add_new_book('Страна багровых туч')
        collector.add_new_book('Страна багровых туч')

        assert len(collector.get_books_rating()) == 1


    def test_set_rating_missing_book(self):  # нельзя выставить рейтинг книге, которой нет в списке
        collector = BooksCollector()
        collector.set_book_rating('Град обреченный', 9)

        assert len(collector.get_books_rating()) == 0


    def test_set_book_rating_zero_eleven_rating_not_zero(self):  # нельзя выставить рейтинг меньше 1
        collector = BooksCollector()
        collector.add_new_book('Страна багровых туч')
        collector.set_book_rating('Страна багровых туч', 0)

        assert collector.books_rating['Страна багровых туч'] != 0


    def test_set_book_rating_more_than10_eleven_rating_not_eleven(self):  # нельзя выставить рейтинг больше 10
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.set_book_rating('Град обреченный', 11)

        assert collector.books_rating['Град обреченный'] != 11


    def test_get_book_rating_missing_book_rating_none(self):  # у не добавленной книги нет рейтинга
        collector = BooksCollector()

        assert collector.books_rating.get('Страна багровых туч') == None


    def test_add_book_in_favorites_book_added_in_favorites(self):  # можно добавить книгу в избранное
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.add_book_in_favorites('Град обреченный')

        assert 'Град обреченный' in collector.get_list_of_favorites_books()


    def test_add_book_in_favorites_missing_book_book_not_in_favorites(self):  # нельзя добавить книгу в избранное, если её нет в словаре books_rating
        collector = BooksCollector()
        collector.add_book_in_favorites('Страна багровых туч')

        assert 'Страна багровых туч' not in collector.get_list_of_favorites_books()


    def test_delete_book_from_favorites_book_deleted_from_favorites(self):  # можно удалить книгу из избранного
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.add_book_in_favorites('Град обреченный')

        assert 'Град обреченный' in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites('Град обреченный')

        assert 'Град обреченный' not in collector.get_list_of_favorites_books()


    def test_get_book_rating_by_name(self):  # можно получить рейтинг книги по её имени
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.add_new_book('Страна багровых туч')
        collector.set_book_rating('Град обреченный', 9)
        collector.set_book_rating('Страна багровых туч', 6)
        rating_by_name = collector.get_book_rating('Страна багровых туч')

        assert rating_by_name == 6


    def test_get_books_with_specific_rating_rating_nine(self):  # можно вывести список книг с определённым рейтингом
        collector = BooksCollector()
        collector.add_new_book('Град обреченный')
        collector.add_new_book('Страна багровых туч')
        collector.set_book_rating('Град обреченный', 9)
        collector.set_book_rating('Страна багровых туч', 6)
        books_rating_nine = collector.get_books_with_specific_rating(9)

        assert ['Град обреченный'] == books_rating_nine