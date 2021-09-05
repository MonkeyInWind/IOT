import Weather from './modules/weather';
import './App.scss';

function App() {
  return (
    <div className='App'>
      <div className='left-container'>
        <Weather />
      </div>
      <div className='center-container'></div>
      <div className='right-container'></div>
    </div>
  );
}

export default App;
