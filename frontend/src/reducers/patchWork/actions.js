import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const getWork =(uuid)=>({
    [RSAA]: {
      endpoint: `http://localhost:8000/work/${uuid}`,
      method: 'GET',
      types: [
        types.W_FETCH_EMP,
        types.W_FETCH_SUCCESS_EMP,
        types.W_FETCH_FAIL_EMP
      ]
    }
  });

  
  export const patchWork = (uuid, values) => {
    console.log(values);
    return {
      [RSAA]: {
        endpoint: `http://localhost:8000/work/${uuid}`,
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(values),
        types: [
          "nothing",  
          types.W_PATCH_SUCCESS,
          types.W_PATCH_FAIL,
        ]
      }
    }
  };

  export const patchflag = () => {
    return {
        type: types.W_PATCH_FLAG
    }
}



