import React from 'react';
import {PageHeader, Button,Form,Input} from 'antd';

import FilterForm from '../../containers/filterContainer';

export default (props) => (
    <PageHeader
        style={{
        border: '1px solid rgb(235, 237, 240)',
        }}
        title="Контракты"
        //subTitle="This is a subtitle"
        {...props}
        extra={[
          ]}
    >
      <FilterForm/>
      </PageHeader>
);