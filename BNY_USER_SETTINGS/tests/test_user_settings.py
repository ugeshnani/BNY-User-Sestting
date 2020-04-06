import configparser
import pytest
import os
from src.services.ESGservice import DataMapper
from src.services.user_setting_services import UserSettingService


@pytest.mark.parametrize("test_input1,test_input2,test_input3,expected",
                         [("test1", "emp", {"file_name": "test1(1).csv",
                                            "data": {
                                                "Customer_Name": "nani"}},
                           "Success"),
                          ("test2", "emp", {"file_name": "test2(1).csv",
                                            "data": {
                                                "Customer_Name": "Solo"}},
                           "Success"),

                          ("test3", "emp", {"file_name": "test3(1).csv",
                                            "data": {
                                                "Customer_Name": "Solo"}},
                           "Success")])
def test_save_settings(test_input1, test_input2, test_input3, expected):
    user_settings = UserSettingService()
    result = user_settings.save_settings(test_input1, test_input2, test_input3)
    assert result['pdf1'] == expected


@pytest.mark.parametrize("test_input1,test_input2,expected",
                         [("test1", "emp", "Success"),
                          ("test2", "emp", "Success"), ("test3", "emp", "Success")])
def test_get_settings(test_input1, test_input2, expected):
    user_settings = UserSettingService()
    result = user_settings.get_settings(test_input1, test_input2)
    assert result['pdf1'] == expected



@pytest.mark.parametrize("test_input1,test_input2,expected",
                         [("test1", "emp", "Success"),
                          ("test2", "emp", "Success"), ("test3", "emp", "Success")])
def test_settings_history(test_input1, test_input2, expected):
    user_settings = UserSettingService()
    result = user_settings.settings_history(test_input1, test_input2)
    assert result['pdf1'] == expected
