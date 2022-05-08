Feature: Testing wishlist feature

  Background:
    Given automationPractice: user is on the main page

    Scenario: User adds a product to the wishlist
      When automationPractice: user logs in
      When automationPractice: user clicks on a product
      When productPage: user adds the product to the wishlist
      Then productPage: added to wishlist alert is displayed

    Scenario: User proceeds to wishlist page from his account
      When automationPractice: user is already logged in
      When automationPractice: user clicks on the account management button
      When accountDetailsPage: user clicks on wishlist button
      Then wishlistPage: wishlist page currently displayed

    Scenario: A new wishlist should have been created automatically
      When automationPractice: user is already logged in
      When automationPractice: user clicks on the account management button
      When accountDetailsPage: user clicks on wishlist button
      Then wishlistPage: default wishlist "My Wishlist" should be created

    Scenario Outline: User creates an empty wishlist
      When automationPractice: user is already logged in
      When automationPractice: user clicks on the account management button
      When accountDetailsPage: user clicks on wishlist button
      Then wishlistPage: user creates a new wishlist named "<wishlist_name>"

      Examples:
      |   wishlist_name |
      |   test_wishlist |

   Scenario Outline: User tries to view an empty wishlist
      When automationPractice: user is already logged in
      When automationPractice: user clicks on the account management button
      When accountDetailsPage: user clicks on wishlist button
      When wishlistPage: user clicks to view the empty wishlist named "<wishlist_name>"
      Then wishlistPage: No products alert is displayed

      Examples:
     |  wishlist_name |
     |  test_wishlist |

    Scenario Outline: User deletes a wishlist
      When automationPractice: user is already logged in
      When automationPractice: user clicks on the account management button
      When accountDetailsPage: user clicks on wishlist button
      When wishlistPage: user clicks to delete the "<wishlist_name>" wishlist
      Then wishlistPage: "<wishlist_name>" is deleted

      Examples:
      | wishlist_name |
      | test_wishlist |

