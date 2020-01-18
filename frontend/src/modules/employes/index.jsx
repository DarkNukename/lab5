import React from 'react';
import EmpList from "./containers/employListContainer";
import Header from "./components/header";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Patcher from "./containers/patchFormContainer"
import Poster from "./containers/addFormContainer"

const data = [
    {
      key: '1',
      name: 'John Brown',
      age: 32,
      address: 'New York No. 1 Lake Park',
      tags: ['nice', 'developer'],
    },
    {
      key: '2',
      name: 'Jim Green',
      age: 42,
      address: 'London No. 1 Lake Park',
      tags: ['loser'],
    },
    {
      key: '3',
      name: 'Joe Black',
      age: 32,
      address: 'Sidney No. 1 Lake Park',
      tags: ['cool', 'teacher'],
    },
  ];
export default ({match}) => (
    <div>
        <Switch>
            <Route path={`${match.path}/patch/:uuid`} component = {Patcher}>
            </Route>
            <Route path={`${match.path}/post`} component = {Poster}/>
            <Route exact path={`${match.path}`}>
                <Header/>
                <EmpList data = {data}/>
            </Route>
        </Switch>
    </div>
)