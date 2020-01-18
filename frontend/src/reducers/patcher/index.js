import * as types from './actionTypes';

const initialState = {
    isFetching: false,
    isPatched: false,
    emp: {},
    errors:undefined
}

export default (state = initialState, action) => {
    switch(action.type) {
        case types.FETCH_EMP: { 
            return {...state, isFetching: true}
        }
        case types.FETCH_SUCCESS_EMP: {
            return {...state, emp:{...action.payload}, isFetching: false}
        }
        case types.FETCH_FAIL_EMP: {
            return {...state, isFetching: false}
        }

        case types.PATCH_SUCCESS: {
            return {...state, isPatched: true }
        }
        case types.PATCH_FAIL: {
            return {...state, isPatched: false}
        }

        case types.PATCH_FLAG:{
            return{...state, isPatched: false}
        }

        default: return state;
    }
    
}