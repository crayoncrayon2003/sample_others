# make dir
```
mkdir -p ./keycloak ./keycloakDB
```

# build and run
```
docker compose up -d
```

# How to use
## Login
- http://localhost:3000/

select Administration Console. input following.
- Username : admin
- Password : 1234

## Realm
master -> Create realm
- Realm name            : sample_realm
- Enabled               : ON

## Add User
Users -> Create new users

* Required user actions :
* Username              : user1
* Email                 :
* Email verified        :
* First name            :
* Last name             :
* Groups                :

### Details
default

### attributes
default

### credentials
Set password
* Password              : 1234
* Password confirmation : 1234

### Role Mapping
default

### groups
default

### consents
default

### identity providers linkes
default

### sessions
default

## Add Clients
Clients -> Create client

setting following.

* Client type : OpenID Connect
* Client ID   : sample_client
* Name        : sample_client
* Description :

* Client authentication : On
* Authorization         : On
* Authentication flow
    * Standard flow        : ON
    * Direct access grants : ON
    * Implicit flow        : OFF
    * OAuth 2.0 Device Authorization Grant : OFF
    * OIDC CIBA Grant      : OFF

* Root URL
* Home URL
* Valid redirect URIs              : http://localhost:3000/callback
* Valid post logout redirect URIs  : http://localhost:3000/
* Web origins(CORS)                : *

copy Client Secret.
Clients -> sample_client -> Credentials -> Client secret 

# Authentication
## Case1 : CUI
Create Access URL.  input URL for browser.
```
AUTH_URL="http://localhost:8080/realms/sample_realm/protocol/openid-connect/auth"
CLIENT_ID="sample_client"
REDIRECT_URI="http://localhost:3000/callback"
RESPONSE_TYPE="code"
SCOPE="openid"
STATE="1234567890abcdef"

echo "${AUTH_URL}?client_id=${CLIENT_ID}&redirect_uri=${REDIRECT_URI}&response_type=${RESPONSE_TYPE}&scope=${SCOPE}&state=${STATE}"
```

Enter user information.
- Username : user1
- Password : 1234

after login, Browser URL is updated. copy <AUTH_CODE>
```
http://localhost:3000/callback?state=1234567890abcdef&session_state=<SESSION_STATE>&code=<AUTH_CODE>
```

```
TOKEN_URL="http://localhost:8080/realms/sample_realm/protocol/openid-connect/token"
CLIENT_ID="sample_client"
CLIENT_SECRET="<CLIENT_SECRET>"
REDIRECT_URI="http://localhost:3000/callback"
AUTH_CODE="<AUTH_CODE>"

curl -X POST "$TOKEN_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=authorization_code" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET" \
  -d "redirect_uri=$REDIRECT_URI" \
  -d "code=$AUTH_CODE"
```

## Case2 : selenium
Update CLIENT_SECRET  in case02_Selenium.py
```
python case02_selenium.py
```

## Case3 : React App
Update client_secret  in case03_ReactApp/src/keycloak.js
```
cd case03_ReactApp
npm install
yarn start
```

