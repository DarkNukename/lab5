import React from 'react';
import {connect} from 'react-redux';
import {addWork} from '../../../reducers/addwork/actions';
import addForm from '../components/add_form'

function mapStateToProps(state) {   
  return {
      isFetching: state.addperson.isFetching,
      errors: state.addperson.errors,
    }
}

function mapDispatchToProps(dispatch) {
    return {
        addWork: (values)=> dispatch(addWork(values))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(addForm);