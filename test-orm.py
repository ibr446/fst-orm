import pytest
from models.user import User



@pytest.mark.asyncio
async def test_create_user():
    user = await User.create(name="Test User", email="test@example.com")
    assert user.id is not None
    assert user.name == "Test User"
    assert user.email == "test@example.com"