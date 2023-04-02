# Created by loulouangibeau at 4/2/23
Feature: Test Scenarios For Empty Cart

    Scenario:  'Your Shopping Cart is empty' shown if no product added
       Given Open Amazon Url
       When Click on cart icon
       Then Verify 'Your Shopping Cart is empty.' text 0 is present