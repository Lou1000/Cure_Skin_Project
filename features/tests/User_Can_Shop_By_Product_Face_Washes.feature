# Created by loulouangibeau at 4/21/23
Feature: User can shop by product Face Washes


  Scenario:User can shop by product Face Washes
    Given Open the main page
    Then Click on 'Shop by product' - select Face Washes
    When Verify 2 products 'Face Wash' results is shown



  Scenario:User can shop by product Face Washes in mobile view
    Given Open the main page
    When Click on hamburger menu
    Then Click on 'Shop by product' - select Face Washes
    When Verify 2 products 'Face Wash' results is shown
