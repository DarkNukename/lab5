import {FILTER_WORKS} from './actionTypes';

export const filter = (payload) => {
    return {
        type: FILTER_WORKS,
        payload
    }
}
