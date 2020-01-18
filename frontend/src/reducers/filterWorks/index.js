import * as types from './actionTypes';

const initialState = {
    filters: {}
}

export default (state = initialState, action) => {
    switch(action.type) {
        case types.FILTER_WORKS: {
            return {...state, filters: action.payload}
        }
        default: return state;
    }
    
}