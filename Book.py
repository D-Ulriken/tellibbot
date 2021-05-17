

class Book:

    def __init__(self, name: str = "", author: str = "",
                 description: str = "", release: str = "", tags: str = "", links: str = ""):
        self.name = name
        self.author = author
        self.description = description
        self.release = release
        self.tags = tags
        self.links = links

    def show_info(self):
        return "📕 Назва книги: " + self.name + "\n\n" \
               + "📗 Автор: " + self.author + "\n\n" \
               + "📔 Опис книги: " + self.description + "\n\n" \
               + "📙 Дата випуску: " + self.release + "\n\n" \
               + "💡 " + self.tags + "\n\n" \
               + "🌍 Завантажити за посиланням: " + self.links
