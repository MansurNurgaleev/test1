import pytest

from app.models import Item


@pytest.mark.django_db
def test_item():
    item = Item.objects.create(name='T-Short', description='tshort', price=10)
    assert item.name == 'T-Short'
    assert item.description == 'tshort'
    assert item.price == 10