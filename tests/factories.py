import factory
from datetime import datetime, timedelta


class TodoListFactory(factory.Factory):
    class Meta:
        model = dict

    id = factory.Sequence(lambda n: n + 1)
    title = factory.Faker("sentence", nb_words=3)
    is_archived = False

# class TodoItemFactory(factory.Factory):
#     class Meta:
#         model = dict
#
#     id = factory.Sequence(lambda n: n + 1)
#     list_id = 1
#     title = factory.Faker("sentence", nb_words=4)
#     completed = False
#     due_date = factory.LazyFunction(datetime.now)
#     expiry = factory.LazyFunction(lambda: datetime.now() + timedelta(days=2))
#     archived = False

class TodoItemFactory(factory.Factory):
    class Meta:
        model = dict

    id = factory.Sequence(lambda n: n + 1)
    list_id = 1
    title = factory.Faker("sentence", nb_words=4)
    completed = False
    archived = False

    due_date = factory.LazyFunction(lambda: datetime.now() - timedelta(days=5))
    expiry = factory.LazyFunction(lambda: datetime.now() - timedelta(days=1))