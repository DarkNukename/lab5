import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const fetchWorks =(params)=>({
    [RSAA]: {
      endpoint: `http://localhost:8000/works/${queryParamsGenerator(params)}`,
      method: 'GET',
      types: [
        types.FETCH_WORKS,
        types.FETCH_SUCCESS_WORKS,
        types.FETCH_FAIL_WORKS
      ]
    }
  });

  export const deleteWork =(uuid)=>({
    [RSAA]: {
      endpoint: `http://localhost:8000/work/${uuid}`,
      method: 'DELETE',
      types: [
        types.DELETE_WORK,
        types.DELETE_SUCCESS_WORK,
        types.DELETE_FAIL_WORK
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