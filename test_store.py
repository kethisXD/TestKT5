# test_store.py
import pytest
import allure
from models import Store
from base_test import BaseTest

@allure.epic("Petstore API")
@allure.feature("Store Operations")
class TestStore(BaseTest):

    @allure.story("Place an order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_place_order(self):
        order = Store(
            id=1001,
            petId=2002,
            quantity=3,
            shipDate="2024-12-01T10:00:00.000Z",
            status="placed",
            complete=False
        )
        with allure.step("Send POST request to place order"):
            response = self.send_request(
                method="POST",
                endpoint="/store/order",
                json=order.dict()
            )
        assert response.status_code == 200
        created_order = Store.parse_obj(response.json())
        assert created_order.id == order.id

    @allure.story("Get order by ID")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_order(self):
        order_id = 1001
        with allure.step("Send GET request to retrieve order"):
            response = self.send_request(
                method="GET",
                endpoint=f"/store/order/{order_id}"
            )
        assert response.status_code == 200
        order = Store.parse_obj(response.json())
        assert order.id == order_id

    @allure.story("Delete order")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_delete_order(self):
        order_id = 1001
        with allure.step("Send DELETE request to remove order"):
            response = self.send_request(
                method="DELETE",
                endpoint=f"/store/order/{order_id}"
            )
        assert response.status_code == 200
        with allure.step("Verify order deletion"):
            get_response = self.send_request(
                method="GET",
                endpoint=f"/store/order/{order_id}"
            )
            assert get_response.status_code == 404

    @allure.story("Get inventory")
    @allure.severity(allure.severity_level.MINOR)
    def test_get_inventory(self):
        with allure.step("Send GET request to retrieve inventory"):
            response = self.send_request(
                method="GET",
                endpoint="/store/inventory"
            )
        assert response.status_code == 200
        inventory = response.json()
        assert isinstance(inventory, dict)
        assert "placed" in inventory
