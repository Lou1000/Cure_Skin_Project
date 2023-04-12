# Created by loulouangibeau at 2/26/23
Feature: Test scenario that shows sub header objects upon clicking best sellers

  Scenario: User is seeing sub header links upon tapping best sellers
    Given Open Amazon page
    When Click on hamburger icon
    When Click on best sellers
    Then Verify that there are 5 links