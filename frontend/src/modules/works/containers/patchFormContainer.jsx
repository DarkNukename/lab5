import React from 'react';
import {connect} from 'react-redux';
import {getWork, patchWork,patchflag} from '../../../reducers/patchWork/actions';
import Patcher from '../components/patcher'

function mapDispatchToProps(dispatch) {
    return {
        getWork: (uuid) => dispatch(getWork(uuid)),
        patchWork: (...args)=> dispatch(patchWork(...args)),
        patchflag:() => dispatch(patchflag())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Patcher);

function mapStateToProps(state) {
    return {
        isPatched: state.patchWork.isPatched,
        emp: state.patchWork.emp
      }
  }