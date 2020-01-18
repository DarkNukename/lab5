import React from 'react';
import WorkList from "./containers/workListContainer";
import Header from "./components/header";
import {BrowserRouter as Router, Switch, Route} from "react-router-dom";
import Patcher from "./containers/patchFormContainer"
import Poster from "./containers/addFormContainer"

export default ({match}) => (
    <div>
        <Switch>
            <Route path={`${match.path}/post`} component = {Poster}/>  
            <Route path={`${match.path}/patch/:uuid`} component = {Patcher}/>
            <Route exact path={`${match.path}`}>
                <Header/>
                <WorkList/>
            </Route>
            
        </Switch>
      
    </div>
)