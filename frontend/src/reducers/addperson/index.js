import * as types from './actionTypes';

const initialState = {
    isFetching: false,
    errors:undefined
}

export default (state, action) => {
    switch(action.type) {
        case types.ADD_EMPS: {
            return {...state, isFetching: true}
        }
        case types.ADD_FAIL_EMPS: {
            return {...state, errors:{...action.payload}, isFetching: false}
        }
        case types.ADD_SUCCESS_EMPS: {
            return {...state, isFetching: false}
        }
        default: return {...state, ...initialState};
    }
    
}