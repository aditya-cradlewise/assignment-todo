import pytest
from unittest.mock import MagicMock
from app.service.todo_service import TodoService
from tests.factories import TodoListFactory


# Create List Test
def test_create_list_success(monkeypatch):
    service = TodoService()
    service.repo = MagicMock()

    service.repo.create_list.return_value = 1

    result = service.create_list("Test List")

    assert result == 1
    service.repo.create_list.assert_called_once_with("Test List")

# Create List Test without Title
def test_create_list_without_title():
    service = TodoService()

    with pytest.raises(ValueError):
        service.create_list("")

# Create Item Test
def test_create_item_success(monkeypatch):
    service = TodoService()
    service.repo = MagicMock()

    # service.repo.get_list.return_value = (1, "List", False)
    service.repo.create_item.return_value = 10

    mock_list = TodoListFactory(id=1, is_archived=False)
    service.repo.get_list.return_value = (
        mock_list["id"],
        mock_list["title"],
        mock_list["is_archived"],
    )

    item_id = service.create_item(1, "Task", None)

    assert item_id == 10

# Create Item Test Archived
def test_create_item_archived_list():
    service = TodoService()
    service.repo = MagicMock()

    service.repo.get_list.return_value = (1, "List", True)

    with pytest.raises(ValueError):
        service.create_item(1, "Task")

