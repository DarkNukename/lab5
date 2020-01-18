
import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const addEmps = (values) => {
  return {
    [RSAA]: {
      endpoint: 'http://localhost:8000/persons/',
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
      types: [
        types.ADD_EMPS,
        types.ADD_SUCCESS_EMPS,
        types.ADD_FAIL_EMPS
      ]
    }
  }
};