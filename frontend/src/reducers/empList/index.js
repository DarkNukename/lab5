import * as types from './actionTypes';

const initialState = {
    isFetching: false,
    emps:[],
    errors:undefined,
    isDeleted: false
}

export default (state = initialState, action) => {
    switch(action.type) {
        case types.FETCH_EMPS: {
            return {...state, isFetching: true}
        }
        case types.FETCH_FAIL_EMPS: {
            return {...state, errors:{...action.payload}, isFetching: false}
        }
        case types.FETCH_SUCCESS_EMPS: {
            return {...state, emps:[...action.payload], isFetching: false}
        }

        case types.DELETE_SUCCESS_EMP: {
            return {...state, isDeleted: true}
        }
        case types.DELETE_HANDLED: {
            return {...state, isDeleted: false}
        }




        default: return state;
    }

}
