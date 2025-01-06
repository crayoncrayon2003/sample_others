Feature: Data API Test

Scenario: POST /data-api endpoint
  Given url baseUrl + '/data-api'
  And request { "id": 1, "value": 10 }
  When method post
  Then status 200
  And match response == { "message": "Data created", "id": 1, "value": "10" }

Scenario: GET /data-api endpoint
  Given url baseUrl + '/data-api'
  And param id = 1
  When method get
  Then status 200
  And match response == { "id": 1, "value": "10" }
