import React from 'react';
import {BrowserRouter as Router, Switch, Route, Link} from "react-router-dom"
import logo from './logo.svg';
import './App.css';
import CustomHeader from "./components/header"
import 'antd/dist/antd.css';
import { Layout, Menu, Icon } from 'antd';
import CustomCont from "./components/content"

const { Header, Content, Footer, Sider } = Layout;

function App() {
  return (
    <Router>
    <Layout>
    <Sider
      style={{
        overflow: 'auto',
        height: '100vh',
        position: 'fixed',
        left: 0,
      }}
    >
      <div className="logo" />
        <Menu theme="dark" mode="inline" defaultSelectedKeys={['4']}>
          <Menu.Item key="1">
            <Link to="/emp">
              <Icon type="user" />
              <span className="nav-text">Работники</span>
            </Link>
          </Menu.Item>

          <Menu.Item key="2">
            <Link to="/work">
              <Icon type="bank" />
              <span className="nav-text">Контракты</span>
            </Link>
          </Menu.Item>
        </Menu>
      
    </Sider>
    <Layout style={{ marginLeft: 200 }}>
   
      <Content style={{flex: 2, margin: '0 0', overflow: 'initial' }}>
        <div style={{ padding: 24, background: '#fff', textAlign: 'center' }}>
        <CustomCont/>
        </div>
      </Content>
    </Layout>
  </Layout>
  </Router>
  );
}

export default App;
