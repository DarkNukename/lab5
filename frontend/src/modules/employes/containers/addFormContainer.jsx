import React from 'react';
import {connect} from 'react-redux';
import {addEmps} from '../../../reducers/addperson/actions';
import addForm from '../components/add_form'

function mapStateToProps(state) {   
  return {
      isFetching: state.addperson.isFetching,
      errors: state.addperson.errors,
    }
}

function mapDispatchToProps(dispatch) {
    return {
        addEmps: (values)=> dispatch(addEmps(values))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(addForm);