# test_user.py
import pytest
import allure
from models import User
from base_test import BaseTest

@allure.epic("Petstore API")
@allure.feature("User Operations")
class TestUser(BaseTest):

    @allure.story("Create a new user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user(self):
        user = User(
            id=1,
            username="johndoe",
            firstName="John",
            lastName="Doe",
            email="johndoe@example.com",
            password="password123",
            phone="1234567890",
            userStatus=1
        )
        with allure.step("Send POST request to create user"):
            response = self.send_request(
                method="POST",
                endpoint="/user",
                json=user.dict()
            )
        assert response.status_code == 200
        created_user = User.parse_obj(response.json())
        assert created_user.username == user.username

    @allure.story("Get user by username")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_user(self):
        username = "johndoe"
        with allure.step("Send GET request to retrieve user"):
            response = self.send_request(
                method="GET",
                endpoint=f"/user/{username}"
            )
        assert response.status_code == 200
        user = User.parse_obj(response.json())
        assert user.username == username

    @allure.story("Update existing user")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_user(self):
        user = User(
            id=1,
            username="johndoe",
            firstName="Johnny",
            lastName="Doe",
            email="johnnydoe@example.com",
            password="newpassword123",
            phone="0987654321",
            userStatus=1
        )
        with allure.step("Send PUT request to update user"):
            response = self.send_request(
                method="PUT",
                endpoint="/user",
                json=user.dict()
            )
        assert response.status_code == 200
        updated_user = User.parse_obj(response.json())
        assert updated_user.firstName == "Johnny"

    @allure.story("Delete user")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_user(self):
        username = "johndoe"
        with allure.step("Send DELETE request to remove user"):
            response = self.send_request(
                method="DELETE",
                endpoint=f"/user/{username}"
            )
        assert response.status_code == 200
        with allure.step("Verify user deletion"):
            get_response = self.send_request(
                method="GET",
                endpoint=f"/user/{username}"
            )
            assert get_response.status_code == 404
