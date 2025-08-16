import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

//Components
import AppComponent from './components/AppComponent/AppComponent.jsx';
import './components/AppComponent/AppComponent.css'

import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <AppComponent />
  </React.StrictMode>
);

reportWebVitals();
