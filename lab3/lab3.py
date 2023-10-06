class PageRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PageRegistry, cls).__new__(cls)
            cls._instance.pages = []
        return cls._instance

    def add_page(self, page):
        self.pages.append(page)

    def get_next_page_id(self):
        return len(self.pages) + 1

# Клас книг
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.pages = []

    def add_page(self, page):
        self.pages.append(page)

# Класи типів книг
class ScientificBookBuilder:
    def __init__(self):
        self.book = Book("Наукова книга", "Автор наукової книги")

    def add_references(self, references):
        self.book.references = references

    def add_glossary(self, glossary):
        self.book.glossary = glossary

    def get_book(self):
        return self.book

class NovelBookBuilder:
    def __init__(self):
        self.book = Book("Роман", "Автор роману")

    def add_characters(self, characters):
        self.book.characters = characters

    def get_book(self):
        return self.book

class ManualBookBuilder:
    def __init__(self):
        self.book = Book("Посібник", "Автор посібника")

    def add_image(self, image):
        self.book.image = image

    def get_book(self):
        return self.book

# Клас для створення книг сторінка за сторінкою
class BookAssembler:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.add_references(["Джерело 1", "Джерело 2"])
        self.builder.add_glossary({"термін 1": "визначення 1", "термін 2": "визначення 2"})

# Створення об'єкта книги наукового типу
scientific_builder = ScientificBookBuilder()
director = BookAssembler(scientific_builder)
director.construct()
scientific_book = scientific_builder.get_book()

# Створення об'єкта книги роману
novel_builder = NovelBookBuilder()
novel_builder.add_characters(["Персонаж 1", "Персонаж 2"])
novel_book = novel_builder.get_book()

# Створення об'єкта книги посібника
manual_builder = ManualBookBuilder()
manual_builder.add_image("image.jpg")
manual_book = manual_builder.get_book()


page_registry = PageRegistry()
page1_id = page_registry.get_next_page_id()
page2_id = page_registry.get_next_page_id()

scientific_book.add_page({"id": page1_id, "content": "Зміст сторінки 1"})
scientific_book.add_page({"id": page2_id, "content": "Зміст сторінки 2"})

print(scientific_book.__dict__)
print(novel_book.__dict__)
print(manual_book.__dict__)