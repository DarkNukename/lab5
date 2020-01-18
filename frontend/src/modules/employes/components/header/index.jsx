import React from 'react';
import {PageHeader, Button,Form,Input} from 'antd';

import FilterForm from '../../containers/filterContainer';

export default (props) => (
    <PageHeader
        style={{
        border: '1px solid rgb(235, 237, 240)',
        }}
        title="Работники"
        //subTitle="This is a subtitle"
        {...props}
        extra={[
          ]}
    >
      <FilterForm/>
      </PageHeader>
);

/*
 <Form layout="inline">
            <Form.Item>
                <Input placeholder="Фамилия"/>
            </Form.Item>
            <Form.Item>
              <Input placeholder="Имя"/>
            </Form.Item>
            <Form.Item>
              <Input placeholder="Разряд"/>
            </Form.Item>
            <Form.Item>
              <Input placeholder="Специализация"/>
            </Form.Item>
            <Form.Item>
              <Input placeholder="Уровень английского"/>
            </Form.Item>
            <Form.Item>
              <Button type="primary" htmlType="submit">
                Поиск
              </Button>
            </Form.Item>
          </Form>
*/