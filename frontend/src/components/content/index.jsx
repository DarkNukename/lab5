import React from 'react';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import Employes from "../../modules/employes"
import Works from "../../modules/works"

export default () => (

        <Switch>
            <Route path='/emp' component={Employes}/>
            <Route path='/work' component = {Works}/>      
            <Route path='/'>1</Route>
        </Switch>

)