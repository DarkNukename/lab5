import React from 'react';
import {connect} from 'react-redux';
import {fetchWorks, deleteWork, deleteHandled} from '../../../reducers/workList/actions';
import workList from '../components/worklist'

// вытаскивает из state переменные

function mapStateToProps(state) {
  return {
      isFetching: state.workList.isFetching,
      works: state.workList.works,
      errors: state.workList.errors,
      filters: state.filterWorks.filters,
      isDeleted: state.workList.isDeleted,
    }
}

// передает методы, которые отправляют action в redux

function mapDispatchToProps(dispatch) {
    return {
        fetchWorks: (filters)=> dispatch(fetchWorks(filters)),
        deleteWork: (uuid) => dispatch(deleteWork(uuid)),
        deleteHandled: () => dispatch(deleteHandled())

        // dispatch отправляет action в redux
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(workList);