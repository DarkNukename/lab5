import * as types from './actionTypes';

const initialState = {
    isFetching: false,
    works:[],
    errors:undefined,
    isDeleted: false
}

export default (state = initialState, action) => {
    switch(action.type) {
        case types.FETCH_WORKS: {
            return {...state, isFetching: true}
        }
        case types.FETCH_FAIL_WORKS: {
            return {...state, errors: {...action.payload}, isFetching: false}
        }
        case types.FETCH_SUCCESS_WORKS: {
            return {...state, works: [...action.payload], isFetching: false}
        }
        case types.DELETE_SUCCESS_WORK: {
            return {...state, isDeleted: true}
        }
        case types.DELETE_HANDLED: {
            return {...state, isDeleted: false}
        }
        default: return state;
    }
    
}