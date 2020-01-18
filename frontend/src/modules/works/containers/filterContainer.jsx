import React from 'react';
import {connect} from 'react-redux';
import {filter} from '../../../reducers/filterWorks/actions';
import FilterForm from '../components/filter_form'

function mapDispatchToProps(dispatch) {
    return {
        filter: (payload) => dispatch(filter(payload))
    }
}

export default connect(undefined, mapDispatchToProps)(FilterForm);