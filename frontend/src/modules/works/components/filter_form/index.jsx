import React from 'react';
import {BrowserRouter as Router, Switch, Route, Link} from "react-router-dom"
import { Form, Input, Select, Button } from 'antd';
const { Option } = Select;



class FilterForm extends React.Component {
    onSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            values.work = Number(values.work);
            this.props.filter(values);
          });
    }
    render(){
        const { getFieldDecorator } = this.props.form;
        return (
        <Form layout="inline" onSubmit={this.onSubmit}>
            <Form.Item>
            {getFieldDecorator('nps_name', {
                })(
                    <Input
                        placeholder="Имя"/>
                )
            }
            </Form.Item>

            

            <Form.Item>
            {getFieldDecorator('english_level', {
                initialValue: ""
                })(
                <Select style={{ width: 150 }}>
                    <Option value="">Ин. яз.</Option>
                    <Option value="0">отсутствует</Option>
                    <Option value="1">A1</Option>
                    <Option value="2">A2</Option>
                    <Option value="3">B1</Option>
                    <Option value="4">B2</Option>
                    <Option value="5">C1</Option>
                    <Option value="6">C2</Option>
                </Select>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('specialization', {
                })(
                <Select style={{ width: 150 }}>
                    <Option value="0">Монтажник</Option>
                    <Option value="1">Физик</Option>
                    <Option value="2">Технолог</Option>
                    <Option value="3">Программист</Option>
                    <Option value="4">Ядерщик</Option>
                    <Option value="5">Кип</Option>
                    <Option value="6">Электрик</Option>
                </Select>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('skill', {
                })(
                <Select style={{ width: 150 }}>
                    <Option value="0">Стажер</Option>
                    <Option value="1">1я категория</Option>
                    <Option value="2">2я категория</Option>
                    <Option value="3">3я категория</Option>
                    <Option value="4">Ведущий</Option>
                </Select>
                )
                }
            <Form.Item>
            {getFieldDecorator('sum', {
                })(
                    <Input
                        placeholder="Коэффициент"/>
                )
            }
            </Form.Item>




            </Form.Item>
            <Form.Item>
                <Button type="primary" htmlType="submit" style={{marginRight: "10px"}}>
                    Поиск
                </Button>
                
                <Link to={`/work/post/`}>
                    <Button type="secondary" htmlType="submit">
                        Добавить
                    </Button>
                </Link>
                

            </Form.Item>
        </Form>
        )
    }
}

export default Form.create()(FilterForm);