import React from 'react';
import {connect} from 'react-redux';
import {getEMP, patchEMP,patchflag} from '../../../reducers/patcher/actions';
import Patcher from '../components/patcher'

function mapDispatchToProps(dispatch) {
    return {
        getEMP: (uuid) => dispatch(getEMP(uuid)),
        patchEMP: (...args)=> dispatch(patchEMP(...args)),
        patchflag:() => dispatch(patchflag())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Patcher);

function mapStateToProps(state) {
    return {
        isPatched: state.patcher.isPatched,
        emp: state.patcher.emp
      }
  }