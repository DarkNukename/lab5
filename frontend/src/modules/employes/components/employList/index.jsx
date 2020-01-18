import React from 'react';
import { Table, Divider, Tag, Icon, notification, Spin } from 'antd';
import {Link} from 'react-router-dom';
const EN_LEV = ['отсутствует',"A1","A2","B1","B2", "C1", "C2"];
const SPL = ["Монтажник", "Физик", "Технолог", "Программист","Ядерщик", "Кип", "Электрик"]
const SKILL = ["Стажер", "1я категория", "2я категория", "3я категория", "Ведущий"]

function getRandomInt(max) {
    return Math.floor(Math.random() * Math.floor(max));
  }

export default class Emps extends React.Component {
    columns = [
        {
            title: 'Имя',
            dataIndex: 'first_name',
            key: 'name',
        },
        {
            title: 'Фамилия',
            dataIndex: 'second_name',
            key: 'age',
        },
        {
            title: 'Уровень английского',
            dataIndex: 'english_level',
            key: 'address1',
            render: text => EN_LEV[text],
        },
        {
            title: 'Специализация',
            dataIndex: 'specialization',
            key: 'address2',
            render: text => SPL[text],
        },
        {
            title: 'Разряд',
            dataIndex: 'skill',
            key: 'address3',
            render: text => SKILL[text],
        },
        {
            title: 'Зарплата',
            dataIndex: 'salary',
            key: 'address4',
            //render: (id)=>(
            //  ['60000', '70000', '50000'][getRandomInt(3)]
            //)
        },

        {
            title: 'Action',
            key: 'action',
            dataIndex: "uuid",
            render: (uuid) => (
              <span>
                <Link to={`/emp/patch/${uuid}/`}><Icon type="edit" /></Link>
                <Divider type="vertical" />
                <a href="#" onClick={() => this.props.deleteEMP(uuid)}><Icon type="delete" /></a>
              </span>
            ),
          },
      ];

    componentDidMount(){
        const {fetchEmps, filters} = this.props;
        fetchEmps(filters);
    }

    componentDidUpdate(prevProps){
        const {fetchEmps, filters, deleteHandled} = this.props;
        if(prevProps.filters !== filters) {
            fetchEmps(filters);
        }
        if(this.props.isDeleted == true){
            fetchEmps(filters);
            deleteHandled();
        }
    }

    render(){
        const {errors, emps, isFetching} = this.props;
        if(isFetching) return(<Spin/>);
        if(errors){
            notification.error({message: errors.message});
        }
        return (
            <Table columns={this.columns} dataSource={this.props.emps} />
        )
    }
}
