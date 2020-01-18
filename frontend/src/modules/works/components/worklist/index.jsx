import React from 'react';
import { Table, Divider, Tag, Icon, notification, Spin } from 'antd';
import {Link} from 'react-router-dom';

const EN_LEV = ['отсутствует',"A1","A2","B1","B2", "C1", "C2"];
const SPL = ["Монтажник", "Физик", "Технолог", "Программист","Ядерщик", "Кип", "Электрик"]
const SKILL = ["Стажер", "1я категория", "2я категория", "3я категория", "Ведущий"]


export default class Works extends React.Component {
    columns = [
        {
            title: 'Название АЭС',
            dataIndex: 'nps_name',
            key: 'name',
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
            title: 'Коэффициент',
            dataIndex: 'sum',
            key: 'address4',
        },
        

        {
            title: 'Action',
            key: 'action',
            dataIndex: "uuid",
            render: (uuid) => (
              <span>
                <Link to={`/work/patch/${uuid}/`}><Icon type="edit" /></Link>
                <Divider type="vertical" />
                <a href="#" onClick={() => this.props.deleteWork(uuid)}><Icon type="delete" /></a>
              </span>
            ),
          },
      ];

    /*render(){
        const {errors, emps, isFetching} = this.props;
        if(isFetching) return(<Spin/>);
        if(errors){
            notification.error({message: errors.message});
        }
        return (
            <Table columns={this.columns} dataSource={this.props.emps} />
        )
    }*/
    
    componentDidMount(){
        const {fetchWorks, filters} = this.props;
        fetchWorks(filters);
    }

    componentDidUpdate(prevProps){
        const {fetchWorks, filters, deleteHandled} = this.props;
        if(prevProps.filters !== filters) {
            fetchWorks(filters);
        }
        
        if(this.props.isDeleted == true){
            fetchWorks(filters);
            deleteHandled();
        }
       
    }

    render(){
        const {errors, works, isFetching} = this.props;
        if(isFetching) return(<Spin/>);
        if(errors){
            notification.error({message: errors.message});
        }
        return (
            <Table columns={this.columns} dataSource={this.props.works} />
        )
    }
}

    
