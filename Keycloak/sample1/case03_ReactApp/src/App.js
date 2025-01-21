import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import userManager from './keycloak';

const App = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    userManager.getUser().then((loadedUser) => {
      if (loadedUser) {
        setUser(loadedUser);
      }
    });
  }, []);

  const login = () => {
    userManager.signinRedirect();
  };

  const logout = () => {
    userManager.signoutRedirect();
  };

  return (
    <div>
      <h1>React Keycloak OIDC Sample</h1>
      {!user ? (
        <>
          <p>You are not logged in.</p>
          <button onClick={login}>Log In</button>
        </>
      ) : (
        <>
          <p>Logged in as: {user.profile.preferred_username}</p>
          <button onClick={logout}>Log Out</button>
        </>
      )}
    </div>
  );
};

export default App;
