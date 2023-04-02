# Created by loulouangibeau at 4/2/23
  Feature: Test Scenarios logged out user

  Scenario:  Logged out user sees Sign in page when clicking Orders
    Given Open Amazon Main Page
    When Click Amazon Orders link
    Then Verify Sign in page is opened and shows text
