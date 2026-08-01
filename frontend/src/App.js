import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Home } from './components/Home';
import { Result } from './components/Result';
import { Header } from './components/Header'
import { useState } from 'react';

function App() {
  const [result, setResult] = useState(null);
  const [imgUrl, setImgUrl] = useState("");
  return (
    <BrowserRouter>
      <div className="App">
      <Header/>
      <Routes>
      <Route path='/'>
        <Route index element={<Home setResult={setResult} imgUrl={imgUrl} setImgUrl={setImgUrl}/>}/>
        <Route path='result' element={<Result result={result} imgUrl={imgUrl} />}/>
      </Route>
    </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
