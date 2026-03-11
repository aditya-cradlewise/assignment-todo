from app.repository.todo_repository import TodoRepository
from datetime import datetime, timedelta

class TodoService:

    def __init__(self):
        self.repo = TodoRepository()

    # LISTS
    def create_list(self, title):
        if not title:
            raise ValueError("Title required")
        return self.repo.create_list(title)

    def get_lists(self):
        return self.repo.get_lists()

    def get_list(self, list_id):
        if not list_id:
            raise ValueError("List id required")
        return self.repo.get_list(list_id)

    def update_list(self, list_id, title):
        if not title or not list_id:
            raise ValueError("Title or list_id required")
        return self.repo.update_list(list_id, title)

    def delete_list(self, list_id):
        if not list_id:
            raise ValueError("List id required")
        return self.repo.delete_list(list_id)

    def archive_list(self, list_id):
        if not list_id:
            raise ValueError("List id required")
        return self.repo.archive_list(list_id)


    # ITEMS
    def create_item(self, list_id, title, due_date=None):
        if not list_id:
            raise ValueError("List id required")

        if not title or not title.strip():
            raise ValueError("Item title required")

        title = title.strip()

        # Validate list exists
        list_data = self.repo.get_list(list_id)
        if not list_data:
            raise ValueError("List not found")

        # Check if list archived
        if list_data[2]:
            raise ValueError("Cannot add item to archived list")

        expiry = None

        if due_date:
            due_date = datetime.fromisoformat(due_date)
            expiry = due_date + timedelta(days=2)

        return self.repo.create_item(list_id, title, due_date, expiry)

    def get_items(self, list_id):
        if not list_id:
            raise ValueError("List id required")

        self.get_list(list_id)  # ensure list exists
        return self.repo.get_items_by_list(list_id)

    def mark_complete(self, item_id):
        if not item_id:
            raise ValueError("Item id required")

        item = self.repo.get_item(item_id)
        if not item:
            raise ValueError("Item not found")

        if item[6]:  # archived
            raise ValueError("Cannot complete archived item")

        self.repo.mark_complete(item_id)

    def archive_item(self, item_id):
        if not item_id:
            raise ValueError("Item id required")

        item = self.repo.get_item(item_id)
        if not item:
            raise ValueError("Item not found")

        if item[6]:  # archived column index
            raise ValueError("Item already archived")

        self.repo.archive_item(item_id)

    def delete_item(self, item_id):
        if not item_id:
            raise ValueError("Item id required")

        item = self.repo.get_item(item_id)
        if not item:
            raise ValueError("Item not found")

        self.repo.delete_item(item_id)
