import React from 'react';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import { Form, Input, Select, Button } from 'antd';
import './add_form.css';
const { Option } = Select;



class AddForm extends React.Component {
    onSubmit = (e) => {
        e.preventDefault();
        this.props.form.validateFields((err, values) => {
            values.work = Number(values.work);
            if (!err) {
                this.props.addEmps(values);
            }else{
                alert(JSON.stringify(err));
            }
          });
    }
    
    render(){
        const{isFetching, erros} = this.props;

        const { getFieldDecorator } = this.props.form;
        if(isFetching) return(<>Loading...</>);
        return (
        <Form className = 'jojo' onSubmit={this.onSubmit}>
            <h2>Добавить дебила</h2>
            <Form.Item>
            {getFieldDecorator('first_name', {
                rules: [{ required: true, message: 'Please input your username!' }],
                })(
                    <Input
                        placeholder="Имя"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('second_name', {
                rules: [{ required: true, message: 'Please input your username!' }],
                })(
                    <Input
                        placeholder="Фамилия"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('work', {

                })(
                    <Input
                        placeholder="ID работы"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('english_level', {
                rules: [{ required: true, message: 'Please input your username!' }],
                })(
                <Select>
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
                rules: [{ required: true, message: 'Please input your username!' }],
                })(
                <Select>
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
                rules: [{ required: true, message: 'Please input your username!' }],
                })(
                <Select>
                    <Option value="0">Стажер</Option>
                    <Option value="1">1я категория</Option>
                    <Option value="2">2я категория</Option>
                    <Option value="3">3я категория</Option>
                    <Option value="4">Ведущий</Option>
                </Select>
                )
                }
            </Form.Item>
            <Form.Item>
                <Button type="primary" htmlType="submit">
                    Добавить
                </Button>
            </Form.Item>
        </Form>
        )
    }
}

export default Form.create()(AddForm);
