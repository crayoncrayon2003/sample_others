Feature: Hello API Test

Scenario: GET /hello endpoint
  Given url baseUrl + '/hello'
  When method get
  Then status 200
  And match response == 'hello\n'
