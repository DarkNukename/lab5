import {FILTER_EMPS} from './actionTypes';

export const filter = (payload) => {
    return {
        type: FILTER_EMPS,
        payload
    }
}