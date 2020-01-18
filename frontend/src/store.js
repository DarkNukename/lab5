import { createStore, applyMiddleware, combineReducers } from 'redux';
import { apiMiddleware } from 'redux-api-middleware';
import rootReducer from './reducers';


const createStoreWithMiddleware = applyMiddleware(apiMiddleware)(createStore);
export default  createStoreWithMiddleware(rootReducer, {});