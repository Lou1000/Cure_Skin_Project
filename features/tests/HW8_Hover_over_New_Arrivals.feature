# Created by loulouangibeau at 4/9/23
Feature: Test Scenarios For Hovering Over New Arrivals

  Scenario: Verify user can hover over new arrivals
    Given Open Amazon product link
    When Hover over new arrivals tab
    Then  Verify user can see new arrivals 6 links