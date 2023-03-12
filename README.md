# автотесты для учебного приложения BooksCollector, которое позволяет установить рейтинг книг и добавить их в избранное

tests

        Проверить: нельзя добавить одну и ту же книгу дважды
            test_add_added_book_book_not_added
            
        Проверить: нельзя выставить рейтинг книге, которой нет в списке
            test_set_rating_missing_book
        
        Проверить: нельзя выставить рейтинг меньше 1
            test_set_book_rating_zero_eleven_rating_not_zero
        
        Проверить: нельзя выставить рейтинг больше 10
            test_set_book_rating_more_than10_eleven_rating_not_eleven
        
        Проверить: у не добавленной книги нет рейтинга
            test_get_book_rating_missing_book_rating_none
        
        Проверить: можно добавить книгу в избранное
            test_add_book_in_favorites_book_added_in_favorites
        
        Проверить: нельзя добавить книгу в избранное, если её нет в словаре books_rating
            test_add_book_in_favorites_missing_book_book_not_in_favorites
        
        Проверить: можно удалить книгу из избранного
            test_delete_book_from_favorites_book_deleted_from_favorites
        
        Проверить: можно получить рейтинг книги по её имени
            test_get_book_rating_by_name
        
        Проверить: можно вывести список книг с определённым рейтингом
            test_get_books_with_specific_rating_rating_nine(self)
        
