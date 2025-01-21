import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import userManager from './keycloak';

const Callback = () => {
  const navigate = useNavigate();

  useEffect(() => {
    userManager.signinRedirectCallback().then((loadedUser) => {
      navigate('/');
    }).catch((error) => {
      console.error('Error during sign-in:', error);
    });
  }, [navigate]);

  return <div>Loading...</div>;
};

export default Callback;
