import inventory_manager


def test_add_item():
    inventory_manager.inventory.clear()
    inventory_manager.add_item("apple", 5)
    assert inventory_manager.inventory["apple"] == 5


def test_add_existing_item():
    inventory_manager.inventory.clear()
    inventory_manager.add_item("apple", 5)
    inventory_manager.add_item("apple", 3)
    assert inventory_manager.inventory["apple"] == 8


def test_remove_item():
    inventory_manager.inventory.clear()
    inventory_manager.add_item("banana", 2)
    inventory_manager.remove_item("banana")
    assert "banana" not in inventory_manager.inventory


def test_update_stock():
    inventory_manager.inventory.clear()
    inventory_manager.add_item("milk", 4)
    inventory_manager.update_stock("milk", 10)
    assert inventory_manager.inventory["milk"] == 10
