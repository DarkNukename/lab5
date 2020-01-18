import './edit.css';
import React from 'react';
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"
import { Form, Input, Select, Button } from 'antd';
const { Option } = Select;





class PatchForm extends React.Component {
    state={initialValues:{}}

    onSubmit = (e) => {
        e.preventDefault();

        this.props.form.validateFields((err, values) => {
            
            if (!err) {
                this.props.patchEMP(this.props.match.params.uuid, values);
            }else{
                alert(JSON.stringify(err));
            }
          });
    }
    
    
    render(){
        const { getFieldDecorator } = this.props.form;
        return (
        <Form onSubmit ={this.onSubmit} className="jojo" >
            <h2>Редактирование</h2>
            <Form.Item>
            {getFieldDecorator('first_name', {
                rules: [{ required: true, message: 'Please input your username!' }],
                initialValue: this.props.emp.first_name
                })(
                    <Input
                        placeholder="Имя"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('second_name', {
                rules: [{ required: true, message: 'Please input your username!' }],
                initialValue: this.props.emp.second_name
                })(
                    <Input
                        placeholder="Фамилия"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('work', {
                initialValue: this.props.emp.work

                })(
                    <Input
                        placeholder="ID работы"/>
                )
            }
            </Form.Item>

            <Form.Item>
            {getFieldDecorator('english_level', {
                rules: [{ required: true, message: 'Please input your username!' }],
                initialValue: this.props.emp.english_level
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
                initialValue: this.props.emp.specialization
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
                initialValue: this.props.emp.skill
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
                    Изменить
                </Button>
            </Form.Item>
        </Form> 
        )
    }
    componentDidUpdate(){
        console.log(this.props);
        if(this.props.isPatched){
            console.log('isPatched')
            this.props.patchflag();
            this.props.history.goBack();
        }
    }
    componentDidMount(){
        const {getEMP} = this.props;
        getEMP(this.props.match.params.uuid);
    }
    
}

export default Form.create()(PatchForm);