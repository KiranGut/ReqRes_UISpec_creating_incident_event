import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@given('user navigate to the Reqres home page')
def step_impl(context):
    obj_ser = Service("C:/Users/kiran/OneDrive/Documents/chromedriv/chromedriver.exe")
    context.driver = webdriver.Chrome(service=obj_ser)
    context.driver.get("https://reqres.in")
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('click on GET LIST USERS')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "active").click()


@then('verify end point for the request type get list users')
def step_impl2(context):
    endpoint = context.driver.find_element(By.XPATH, "//span[@class='url']").text
    assert endpoint == "/api/users?page=2"


@when('click on GET SINGLE USER')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@data-id='users-single']").click()


@then('verify end point for the request type GET_LIST_USERS')
def step_impl(context):
    endpoint = context.driver.find_element(By.XPATH, "//span[@class='url']").text
    assert endpoint == "/api/users/2"


@then('verify response_GET_SINGLE_USER for the request type')
def step_impl(context):
    ResponseCode = context.driver.find_element(By.XPATH, "//span[@class='response-code']").text
    assert ResponseCode == "200"


@when('click on GET SINGLE USER NOT FOUND')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@data-id='users-single-not-found']").click()
    time.sleep(4)


@then('verify end point for the request type GET_SINGLE_USER_NOT_FOUND')
def step_impl(context):
    endpoint = context.driver.find_element(By.XPATH, "//span[@class='url']").text
    assert endpoint == "/api/users/23"


@then('verify response_GET_SINGLE_USER_NOT_FOUND code bad for the request type')
def step_impl(context):
    ResponseCode = context.driver.find_element(By.XPATH, "//span[@class='response-code bad']").text
    assert ResponseCode == "404"


@when('click on GET LIST RESOURCE')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@data-id='unknown']").click()
    time.sleep(4)


@then('verify end point for the request type GET_LIST_RESOURCE')
def step_impl(context):
    endpoint = context.driver.find_element(By.XPATH, "//span[@class='url']").text
    assert endpoint == "/api/unknown"


@then('verify response_GET_LIST_RESOURCE for the request type')
def step_impl(context):
    ResponseCode = context.driver.find_element(By.XPATH, "//span[@class='response-code']").text
    assert ResponseCode == "200"


@when('click on GET SINGLE RESOURCE')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//li[@data-id='unknown-single']").click()


@then('verify end point for the request type GET_SINGLE_RESOURCE')
def step_impl(context):
    endpoint = context.driver.find_element(By.XPATH, "//span[@class='url']").text
    assert endpoint == "/api/unknown/2"


@then('verify response_GET_SINGLE_RESOURCE for the request type')
def step_impl(context):
    ResponseCode = context.driver.find_element(By.XPATH, "//span[@class='response-code']").text
    assert ResponseCode == "200"