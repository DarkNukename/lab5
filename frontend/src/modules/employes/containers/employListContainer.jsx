import React from 'react';
import {connect} from 'react-redux';
import {fetchEmps, deleteEMP, deleteHandled} from '../../../reducers/empList/actions';
import employList from '../components/employList'

// вытаскивает из state переменные

function mapStateToProps(state) {
  return {
      isFetching: state.empList.isFetching,
      emps: state.empList.emps,
      errors: state.empList.errors,
      filters: state.filterEmps.filters,
      isDeleted: state.empList.isDeleted,
    }
}

// передает методы, которые отправляют action в redux

function mapDispatchToProps(dispatch) {
    return {
        fetchEmps: (filters)=> dispatch(fetchEmps(filters)),
        deleteEMP: (uuid) => dispatch(deleteEMP(uuid)),
        deleteHandled: () => dispatch(deleteHandled())

        // dispatch отправляет action в redux
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(employList);
