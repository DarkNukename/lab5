
import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const fetchEmps =(params)=>({
    [RSAA]: {
      endpoint: `http://localhost:8000/persons/${queryParamsGenerator(params)}`,
      method: 'GET',
      types: [
        types.FETCH_EMPS,
        types.FETCH_SUCCESS_EMPS,
        types.FETCH_FAIL_EMPS
      ]
    }
  });

  export const deleteEMP =(uuid)=>({
      [RSAA]: {
        endpoint: `http://localhost:8000/person/${uuid}`,
        method: 'DELETE',
        types: [
          types.DELETE_EMP,
          types.DELETE_SUCCESS_EMP,
          types.DELETE_FAIL_EMP
        ]
      }
    });

    export const deleteHandled = () => {
        return {
            type: types.DELETE_HANDLED
        }
    }



const queryParamsGenerator = (params) => (
  '?'+Object.keys(params).reduce((queryStr,key) =>
    (params[key] ? queryStr+`&${key}=${params[key]}` : queryStr)
  , '').slice(1)
)
