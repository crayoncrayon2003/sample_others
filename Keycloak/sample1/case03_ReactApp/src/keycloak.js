import { UserManager } from 'oidc-client';

const keycloakConfig = {
    authority: 'http://localhost:8080/realms/sample_realm',
    client_id: 'sample_client',
    redirect_uri: 'http://localhost:3000/callback',
    post_logout_redirect_uri: 'http://localhost:3000/',
    response_type: 'code',
    scope: 'openid',
    client_secret: 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
  };

const userManager = new UserManager(keycloakConfig);

export default userManager;
