import React from 'react';
import './App.css';
import Navbar from './Components/Assets/Navbar/Navbar';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ShopCategory from './Pages/ShopCategory';
import Cart from './Pages/Cart';
import LoginSignup from './Pages/LoginSignup';
import Shop from './Pages/Shop';
import Bottom from './Components/Bottom/Bottom'; // Bottom should be imported here

import men_banner from './Components/Assets/gents-banner.gif'
import women_banner from './Components/Assets/ladies-banner.png'
import kids_banner from './Components/Assets/kids-banner.webp'
import others_banner from './Components/Assets/othersss-banner1.png'

import Product from './Pages/Product'

function App() {
  return (
    <div>
      <BrowserRouter>
        <Navbar />

        <Routes>
          <Route path='/' element={<Shop />} /> {/* Default Shop route */}
          <Route path='/mens' element={<ShopCategory banner={men_banner} category="men" />} />
          <Route path='/womens' element={<ShopCategory banner={women_banner} category="women" />} />
          <Route path='/kids' element={<ShopCategory banner={kids_banner} category="kid" />} />
          <Route path='/others' element={<ShopCategory banner={others_banner} category="other" />} />
          <Route path='/product' element={<Product/>}>
            <Route path=':productId' element={<Product/>}/>
          </Route>
          {/* <Route path='/product' element={<Product/>}/> */}
            
        <Route path='/cart' element={<Cart />} />
          <Route path='/login' element={<LoginSignup />} />
        </Routes>

        {/* Bottom component outside the Routes so it shows on every page */}
        <Bottom />
      </BrowserRouter>
    </div>
  );
}

export default App;
