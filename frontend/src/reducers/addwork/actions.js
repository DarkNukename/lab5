
import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const addWork = (values) => {
  return {
    [RSAA]: {
      endpoint: 'http://localhost:8000/works/',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
      types: [
        types.ADD_WORK,
        types.ADD_SUCCESS_WORK,
        types.ADD_FAIL_WORK
      ]
    }
  }
};