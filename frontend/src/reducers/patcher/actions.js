import {RSAA} from "redux-api-middleware";
import * as types from './actionTypes';

export const getEMP =(uuid)=>({
    [RSAA]: {
      endpoint: `http://localhost:8000/person/${uuid}`,
      method: 'GET',
      types: [
        types.FETCH_EMP,
        types.FETCH_SUCCESS_EMP,
        types.FETCH_FAIL_EMP
      ]
    }
  });

  
  export const patchEMP = (uuid, values) => {
    console.log(values);
    return {
      [RSAA]: {
        endpoint: `http://localhost:8000/person/${uuid}`,
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(values),
        types: [
          "nothing",  
          types.PATCH_SUCCESS,
          types.PATCH_FAIL,
        ]
      }
    }
  };

  export const patchflag = () => {
    return {
        type: types.PATCH_FLAG
    }
}



