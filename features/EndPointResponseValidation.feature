Feature: ReqqRes UI Spec This test for creating incident event

  Scenario: Should display sample request and response details after selecting a specific option
    Given user navigate to the Reqres home page
    When click on GET LIST USERS
    Then verify end point for the request type get list users
    When click on GET SINGLE USER
    Then verify end point for the request type GET_LIST_USERS
    Then verify response_GET_SINGLE_USER for the request type
    When click on GET SINGLE USER NOT FOUND
    Then verify end point for the request type GET_SINGLE_USER_NOT_FOUND
    Then verify response_GET_SINGLE_USER_NOT_FOUND code bad for the request type
    When click on GET LIST RESOURCE
    Then verify end point for the request type GET_LIST_RESOURCE
    Then verify response_GET_LIST_RESOURCE for the request type
    When click on GET SINGLE RESOURCE
    Then verify end point for the request type GET_SINGLE_RESOURCE
    Then verify response_GET_SINGLE_RESOURCE for the request type