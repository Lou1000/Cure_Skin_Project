# Created by loulouangibeau at 2/28/23
Feature: Test scenario that shows item is in Amazon Cart


  Scenario: User sees added item in cart
    Given Open Amazon website
    When click on search input field
    When search for item Marvel Avengers: Endgame Logo Super Heroes United T-Shirt
    When click on search button
    When click on the item
    When select a size
    When add product to cart
    When go to users amazon cart
    Given verify that there is Marvel Avengers: Endgame Logo Super Heroes United T-Shirt item in the users Amazon cart