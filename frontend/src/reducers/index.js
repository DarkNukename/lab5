import {combineReducers} from 'redux';
import empList from './empList';
import addperson from './addperson';
import filterEmps from './filterEmps';
import patcher from './patcher';
import workList from './workList'
import filterWorks from './filterWorks'
import addwork from './addwork'
import patchWork from './patchWork'

export default combineReducers({empList, addperson, filterEmps, patcher, workList, filterWorks, addwork, patchWork });