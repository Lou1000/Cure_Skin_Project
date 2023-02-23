# Created by loulouangibeau at 2/20/23
Feature: Test Scenario showing that verifies user is logged out

  Scenario: Verify that logged out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Clicking on Returns and Orders tab
    Then Sign in text should be shown prompting user to sign in