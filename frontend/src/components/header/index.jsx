import React from 'react';
import {PageHeader, Button} from 'antd';

export default (props) => (
    <PageHeader
        style={{
        border: '1px solid rgb(235, 237, 240)',
        }}
        title="Title"
        subTitle="This is a subtitle"
        {...props}
        extra={[
            <Button key="3">Operation</Button>,
            <Button key="2">Operation</Button>,
            <Button key="1" type="primary">
              Primary
            </Button>
          ]}
    />
);