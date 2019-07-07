Feature: Tests for Search functionality

  Scenario: Search returns correct results
    Given Open store page
    When Enter search word 'phone'
    And Click search button
    Then Verify search results contain 'phone'