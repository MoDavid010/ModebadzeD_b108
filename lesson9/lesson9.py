# «Есть некоторый общий класс родитель Tag, который хранит в себе какой-то HTML тег (например: <tag></tag>).
# От Tag наследуются еще четыре класса Image, Input, Text (т. е <p></p>), Link (т. е <a></a>).
# С использованием указанных паттернов реализовать следующее поведение:
# Должна быть возможность создать необходимый тег, явно его не создавая,
# т. е не через img = Image(), а через фабричный метод или фабрику, например factory.create_tag(name).»


class Tag:
    def get_html(self, *version):
        if version:
            return f"<tag {' '.join(version)}></tag>"


class Image(Tag):
    def get_html(self, *version):
        if version:
            return f"<img {' '.join(version)}></img>"


class Input(Tag):
    def get_html(self, *version):
        if version:
            return f"<input {' '.join(version)}></input>"


class Text(Tag):
    def get_html(self, *version):
        if version:
            return f"<p {' '.join(version)}></p>"


class Link(Tag):
    def get_html(self, *version):
        if version:
            return f"<a {' '.join(version)}></a>"


class TagFactory:
    tags = {"image": Image, "input": Input, "p": Text, "a": Link, "": Tag}

    def create_tag(self, name):
        tag_to_create = self.tags.get(name)
        if tag_to_create:
            return tag_to_create()
        else:
            raise ValueError(name)


if __name__ == "__main__":
    factory = TagFactory()
    elements = ["image", "input", "p", "a", ""]

    for i in elements:
        print(factory.create_tag(i).get_html("class="))
