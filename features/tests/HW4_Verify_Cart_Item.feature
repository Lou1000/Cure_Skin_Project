# Created by loulouangibeau at 3/2/23
Feature: Test scenario that shows item is in Amazon Cart


  Scenario: User sees the item added in the cart
    Given Open Amazon.com website
    When click on the search input field
    When search for item Hefty Party On Disposable Plastic Cups, Red, 18 Ounce, 30 Count
    When click on the search button
    When click on item
    When add the item to cart
    When go to the users amazon cart
    Given verify that there is only 1 item in the users Amazon cart


