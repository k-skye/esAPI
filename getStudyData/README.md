# 查询学生所有信息接口文档

##### 请求方式：
HTTPS - GET
##### URL：
```
https://service-66dnrqg4-1252070599.gz.apigw.tencentcs.com/release/getStudyData?account=学号&password=密码
```
##### 参数：
| 名称      |  说明  |
| :--------| :-----|
| account  | 学号  |
| password | 密码  |
##### 返回均为JSON化后的字符串！以下为json解析后的对象
##### 错误格式（除了登录，考试时间成绩课程表都有可能出错）：
```
{'error':'错误信息'}
```
##### 登录错误信息：
```
{
    "status":"loginError",
    "data":{
        "error":{
            "class_name":"登录接口",
            "msg":"用户名不存在或未按照要求参加教学活动！！"
        }
    }
}
```
```
{
    "status":"loginError",
    "data":{
        "error":{
            "class_name":"登录接口",
            "msg":"密码错误，您还有4次尝试机会！如忘记密码，请与所在学院教务员联系或至行政楼自助机查询!"
        }
    }
}
```
##### 正确返回：
```
{
    "status":"ok",
    "data":{
        "schedule":{
            "schedule_term":"1",
            "schedule_year":"2020-2021",
            "schedule":[
                [
                    [
                        {
                            "color":"blue",
                            "name":"软件项目管理",
                            "weeks_text":"第2-3周",
                            "teacher":"王芳/黄启欣(黄启欣)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                2,
                                3
                            ],
                            "time":"8:40 ~ 10:15"
                        },
                        {
                            "color":"blue",
                            "name":"软件项目管理",
                            "weeks_text":"第8-15周",
                            "teacher":"王芳/黄启欣(黄启欣)",
                            "place":"B5-404",
                            "section":2,
                            "weeks_arr":[
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                15
                            ],
                            "time":"8:40 ~ 10:15"
                        }
                    ],
                    [
                        {
                            "color":"purple",
                            "name":"计算机网络",
                            "weeks_text":"第7-14周,第1-5周",
                            "teacher":"朱朝平(朱朝平)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                1,
                                2,
                                3,
                                4,
                                5
                            ],
                            "time":"10:25 ~ 12:00"
                        }
                    ],
                    [
                        {
                            "color":"red",
                            "name":"UML分析建模",
                            "weeks_text":"第7-9周,第1-5周",
                            "teacher":"王方丽(王方丽)",
                            "place":"A5-111",
                            "section":2,
                            "weeks_arr":[
                                7,
                                8,
                                9,
                                1,
                                2,
                                3,
                                4,
                                5
                            ],
                            "time":"14:15 ~ 15:50"
                        }
                    ],
                    [
                        {
                            "color":"yellow",
                            "name":"形势与政策（五）",
                            "weeks_text":"第14-17周",
                            "teacher":"张忠民",
                            "place":"",
                            "section":2,
                            "weeks_arr":[
                                14,
                                15,
                                16,
                                17
                            ],
                            "time":"16:00 ~ 17:20"
                        },
                        {
                            "color":"yellow",
                            "name":"操作系统",
                            "weeks_text":"第7-13周,第1-5周",
                            "teacher":"邓一星(邓一星)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                1,
                                2,
                                3,
                                4,
                                5
                            ],
                            "time":"16:00 ~ 17:20"
                        }
                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [
                        {
                            "color":"yellow",
                            "name":"UML分析建模",
                            "weeks_text":"第7-13周,第1-5周",
                            "teacher":"王方丽(王方丽)",
                            "place":"B5-404",
                            "section":2,
                            "weeks_arr":[
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                1,
                                2,
                                3,
                                4,
                                5
                            ],
                            "time":"8:40 ~ 10:15"
                        }
                    ],
                    [
                        {
                            "color":"green",
                            "name":"软件项目管理",
                            "weeks_text":"第12-12周",
                            "teacher":"王芳/黄启欣(黄启欣)",
                            "place":"A5-105",
                            "section":2,
                            "weeks_arr":[
                                12
                            ],
                            "time":"10:25 ~ 12:00"
                        }
                    ],
                    [
                        {
                            "color":"blue",
                            "name":"编译原理",
                            "weeks_text":"第14-15周",
                            "teacher":"付春英/钟思斌(付春英,钟思斌)",
                            "place":"B5-304",
                            "section":4,
                            "weeks_arr":[
                                14,
                                15
                            ],
                            "time":"14:15 ~ 17:20"
                        },
                        {
                            "color":"blue",
                            "name":"编译原理",
                            "weeks_text":"第7-12周,第1-5周",
                            "teacher":"付春英/钟思斌(付春英,钟思斌)",
                            "place":"A5-109",
                            "section":2,
                            "weeks_arr":[
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                1,
                                2,
                                3,
                                4,
                                5
                            ],
                            "time":"14:15 ~ 15:50"
                        }
                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [
                        {
                            "color":"purple",
                            "name":"计算机网络",
                            "weeks_text":"第15-17周|单周",
                            "teacher":"朱朝平(朱朝平)",
                            "place":"B5-403",
                            "section":4,
                            "weeks_arr":[
                                15,
                                17
                            ],
                            "time":"8:40 ~ 12:00"
                        }
                    ],
                    [
                        {
                            "color":"red",
                            "name":"编译原理",
                            "weeks_text":"第1-13周",
                            "teacher":"付春英/钟思斌(付春英,钟思斌)",
                            "place":"A5-109",
                            "section":2,
                            "weeks_arr":[
                                1,
                                2,
                                3,
                                4,
                                5,
                                6,
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13
                            ],
                            "time":"10:25 ~ 12:00"
                        }
                    ],
                    [
                        {
                            "color":"yellow",
                            "name":"操作系统",
                            "weeks_text":"第7-13周|单周",
                            "teacher":"邓一星(邓一星)",
                            "place":"B5-404",
                            "section":2,
                            "weeks_arr":[
                                7,
                                9,
                                11,
                                13
                            ],
                            "time":"14:15 ~ 15:50"
                        },
                        {
                            "color":"yellow",
                            "name":"操作系统",
                            "weeks_text":"第1-6周,第8-10周|双周",
                            "teacher":"邓一星(邓一星)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                1,
                                2,
                                3,
                                4,
                                5,
                                6,
                                8,
                                10
                            ],
                            "time":"14:15 ~ 15:50"
                        }
                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [

                    ],
                    [
                        {
                            "color":"yellow",
                            "name":"计算机网络",
                            "weeks_text":"第6-16周,第1-4周",
                            "teacher":"朱朝平(朱朝平)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                6,
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                15,
                                16,
                                1,
                                2,
                                3,
                                4
                            ],
                            "time":"10:25 ~ 12:00"
                        }
                    ],
                    [
                        {
                            "color":"green",
                            "name":"软件项目管理",
                            "weeks_text":"第6-15周,第1-4周",
                            "teacher":"王芳/黄启欣(黄启欣)",
                            "place":"A5-102",
                            "section":2,
                            "weeks_arr":[
                                6,
                                7,
                                8,
                                9,
                                10,
                                11,
                                12,
                                13,
                                14,
                                15,
                                1,
                                2,
                                3,
                                4
                            ],
                            "time":"14:15 ~ 15:50"
                        }
                    ],
                    [
                        {
                            "color":"blue",
                            "name":"软件项目管理",
                            "weeks_text":"第15-15周",
                            "teacher":"王芳/黄启欣(黄启欣)",
                            "place":"A5-202",
                            "section":2,
                            "weeks_arr":[
                                15
                            ],
                            "time":"16:00 ~ 17:20"
                        }
                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ]
                ],
                [
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ],
                    [

                    ]
                ]
            ]
        },
        "examTime":{
            "2020-2021-1":[
                {
                    "no":"(2020-2021-1)-563605-2011036-2",
                    "lesson_name":"操作系统",
                    "date":"第16周周3",
                    "day":"2020-12-16",
                    "time":"19:00-21:00",
                    "time_str":"第16周周3(2020-12-16) 19:00-21:00",
                    "location":"A3-105",
                    "sit_id":3,
                    "sch_place":"分校区"
                },
                {
                    "no":"(2020-2021-1)-883042-2017012-1",
                    "lesson_name":"软件项目管理",
                    "date":"第16周周4",
                    "day":"2020-12-17",
                    "time":"15:00-17:00",
                    "time_str":"第16周周4(2020-12-17) 15:00-17:00",
                    "location":"B5-203(2)",
                    "sit_id":3,
                    "sch_place":"分校区"
                },
                {
                    "no":"(2020-2021-1)-563412-2008024-1",
                    "lesson_name":"编译原理",
                    "date":"第17周周1",
                    "day":"2020-12-21",
                    "time":"09:00-11:00",
                    "time_str":"第17周周1(2020-12-21) 09:00-11:00",
                    "location":"A3-205",
                    "sit_id":3,
                    "sch_place":"分校区"
                },
                {
                    "no":"(2020-2021-1)-563008-2014067-2",
                    "lesson_name":"计算机网络",
                    "date":"第18周周1",
                    "day":"2020-12-28",
                    "time":"09:00-11:00",
                    "time_str":"第18周周1(2020-12-28) 09:00-11:00",
                    "location":"A5-204",
                    "sit_id":18,
                    "sch_place":"分校区"
                },
                {
                    "no":"(2020-2021-1)-563411-2007029-1",
                    "lesson_name":"UML分析建模"
                },
                {
                    "no":"(2020-2021-1)-563407-2009033-1",
                    "lesson_name":"Java EE框架应用开发项目实践"
                },
                {
                    "no":"(2020-2021-1)-563015-2012056-1",
                    "lesson_name":"操作系统课程设计"
                },
                {
                    "no":"(2020-2021-1)-351025-0000000-4",
                    "lesson_name":"形势与政策（五）"
                }
            ]
        },
        "score":{
            "2018-2019":{
                "1":[
                    {
                        "lesson_name":"羽毛球",
                        "credit":1,
                        "point":3.3,
                        "usually_score":90,
                        "last_score":80,
                        "property":"必修课",
                        "score":83
                    },
                    {
                        "lesson_name":"大学生职业生涯规划",
                        "credit":1,
                        "point":3,
                        "usually_score":80,
                        "last_score":79,
                        "property":"必修课",
                        "score":80,
                        "sycj":81
                    },
                    {
                        "lesson_name":"军训",
                        "credit":2,
                        "point":3.7,
                        "usually_score":0,
                        "last_score":85,
                        "property":"必修课",
                        "score":85
                    },
                    {
                        "lesson_name":"思想道德修养与法律基础",
                        "credit":2,
                        "point":2,
                        "usually_score":88,
                        "last_score":58,
                        "property":"必修课",
                        "score":70
                    },
                    {
                        "lesson_name":"形势与政策（一）",
                        "credit":0.5,
                        "point":3,
                        "usually_score":"通过",
                        "last_score":"通过",
                        "property":"必修课",
                        "score":"通过"
                    },
                    {
                        "lesson_name":"高等数学D（一）",
                        "credit":3,
                        "point":1.3,
                        "usually_score":83,
                        "last_score":50,
                        "property":"必修课",
                        "score":60
                    },
                    {
                        "lesson_name":"线性代数A",
                        "credit":2,
                        "point":1.7,
                        "usually_score":80,
                        "last_score":54,
                        "property":"必修课",
                        "score":62
                    },
                    {
                        "lesson_name":"C程序设计基础",
                        "credit":4.5,
                        "point":4,
                        "usually_score":99,
                        "last_score":87,
                        "property":"必修课",
                        "score":91
                    },
                    {
                        "lesson_name":"大数据概论",
                        "credit":3,
                        "point":3,
                        "usually_score":80,
                        "last_score":79,
                        "property":"必修课",
                        "score":79
                    },
                    {
                        "lesson_name":"大学英语（一）",
                        "credit":3.5,
                        "point":2.7,
                        "usually_score":80,
                        "last_score":66,
                        "property":"必修课",
                        "score":76
                    }
                ],
                "2":[
                    {
                        "lesson_name":"网球",
                        "credit":1,
                        "point":3.3,
                        "usually_score":90,
                        "last_score":79,
                        "property":"必修课",
                        "score":82
                    },
                    {
                        "lesson_name":"大学生心理健康教育",
                        "credit":1.5,
                        "point":2.3,
                        "usually_score":85,
                        "last_score":68,
                        "property":"必修课",
                        "score":74,
                        "sycj":81
                    },
                    {
                        "lesson_name":"中国近现代史纲要",
                        "credit":3,
                        "point":3,
                        "usually_score":100,
                        "last_score":60,
                        "property":"必修课",
                        "score":80
                    },
                    {
                        "lesson_name":"形势与政策（二）",
                        "credit":0.25,
                        "point":3.3,
                        "usually_score":80,
                        "last_score":83,
                        "property":"必修课",
                        "score":82
                    },
                    {
                        "lesson_name":"高等数学D（二）",
                        "credit":3,
                        "point":0,
                        "usually_score":80,
                        "last_score":41,
                        "property":"必修课",
                        "score":53,
                        "bkcj":32
                    },
                    {
                        "lesson_name":"离散数学",
                        "credit":4,
                        "point":0,
                        "usually_score":81,
                        "last_score":42,
                        "property":"必修课",
                        "score":58,
                        "bkcj":60,
                        "qzcj":65
                    },
                    {
                        "lesson_name":"微机拆装与维护",
                        "credit":1,
                        "point":4,
                        "usually_score":"优秀",
                        "last_score":"优秀",
                        "property":"必修课",
                        "score":"优秀"
                    },
                    {
                        "lesson_name":"Java面向对象程序设计",
                        "credit":4.5,
                        "point":2.7,
                        "usually_score":85,
                        "last_score":78,
                        "property":"必修课",
                        "score":77,
                        "qzcj":64
                    },
                    {
                        "lesson_name":"大学英语（二）",
                        "credit":4.5,
                        "point":2.3,
                        "usually_score":81,
                        "last_score":58,
                        "property":"必修课",
                        "score":74
                    },
                    {
                        "lesson_name":"专业基础技能实践",
                        "credit":2,
                        "point":3.7,
                        "usually_score":"良好",
                        "last_score":"良好",
                        "property":"必修课",
                        "score":"良好"
                    }
                ]
            },
            "2019-2020":{
                "1":[
                    {
                        "lesson_name":"羽毛球",
                        "credit":1,
                        "point":2.3,
                        "usually_score":75,
                        "last_score":75,
                        "property":"必修课",
                        "score":73,
                        "qzcj":60,
                        "sycj":66.4
                    },
                    {
                        "lesson_name":"马克思主义基本原理概论",
                        "credit":3,
                        "point":2,
                        "usually_score":83,
                        "last_score":56,
                        "property":"必修课",
                        "score":70
                    },
                    {
                        "lesson_name":"思政社会实践",
                        "credit":2,
                        "point":2.7,
                        "usually_score":0,
                        "last_score":75,
                        "property":"必修课",
                        "score":75
                    },
                    {
                        "lesson_name":"形势与政策（三）",
                        "credit":0.25,
                        "point":3,
                        "usually_score":0,
                        "last_score":"通过",
                        "property":"必修课",
                        "score":"通过"
                    },
                    {
                        "lesson_name":"金工实习",
                        "credit":1,
                        "point":2.7,
                        "usually_score":77,
                        "last_score":63,
                        "property":"必修课",
                        "score":75,
                        "sycj":85
                    },
                    {
                        "lesson_name":"概率论与数理统计A",
                        "credit":3,
                        "point":1.7,
                        "usually_score":90,
                        "last_score":50,
                        "property":"必修课",
                        "score":62
                    },
                    {
                        "lesson_name":"数据库原理与应用",
                        "credit":3,
                        "point":1.7,
                        "usually_score":75,
                        "last_score":58,
                        "property":"必修课",
                        "score":63
                    },
                    {
                        "lesson_name":"Java面向对象程序设计大作业",
                        "credit":2,
                        "point":3.7,
                        "usually_score":"良好",
                        "last_score":"良好",
                        "property":"必修课",
                        "score":85
                    },
                    {
                        "lesson_name":"计算机科学导论",
                        "credit":1,
                        "point":3.7,
                        "usually_score":85,
                        "last_score":84,
                        "property":"必修课",
                        "score":85
                    },
                    {
                        "lesson_name":"项目版本管理实践",
                        "credit":1,
                        "point":3.7,
                        "usually_score":"良好",
                        "last_score":"良好",
                        "property":"必修课",
                        "score":"良好"
                    },
                    {
                        "lesson_name":"数据结构",
                        "credit":4,
                        "point":1.3,
                        "usually_score":75,
                        "last_score":51,
                        "property":"必修课",
                        "score":60,
                        "qzcj":71
                    }
                ],
                "2":[
                    {
                        "lesson_name":"羽毛球",
                        "credit":1,
                        "point":4,
                        "usually_score":100,
                        "last_score":85,
                        "property":"必修课",
                        "score":91,
                        "qzcj":85,
                        "sycj":100
                    },
                    {
                        "lesson_name":"毛泽东思想和中国特色社会主义理论体系概论",
                        "credit":4,
                        "point":2.7,
                        "usually_score":81.86,
                        "last_score":69,
                        "property":"必修课",
                        "score":75
                    },
                    {
                        "lesson_name":"形势与政策（四）",
                        "credit":0.25,
                        "point":3.7,
                        "usually_score":95,
                        "last_score":80,
                        "property":"必修课",
                        "score":89
                    },
                    {
                        "lesson_name":"电子工艺实习A",
                        "credit":2,
                        "point":3,
                        "usually_score":0,
                        "last_score":79,
                        "property":"必修课",
                        "score":79
                    },
                    {
                        "lesson_name":"高等数学D（二）",
                        "credit":3,
                        "point":3,
                        "usually_score":74,
                        "last_score":81,
                        "property":"必修课",
                        "score":78
                    },
                    {
                        "lesson_name":"计算机组成原理",
                        "credit":4,
                        "point":1.7,
                        "usually_score":99,
                        "last_score":40,
                        "property":"必修课",
                        "score":64
                    },
                    {
                        "lesson_name":"数据结构大作业",
                        "credit":2,
                        "point":4,
                        "usually_score":"优秀",
                        "last_score":"优秀",
                        "property":"必修课",
                        "score":95
                    },
                    {
                        "lesson_name":"数据库课程设计",
                        "credit":2,
                        "point":2.7,
                        "usually_score":"中等",
                        "last_score":"中等",
                        "property":"必修课",
                        "score":"中等"
                    },
                    {
                        "lesson_name":"算法设计与分析",
                        "credit":4,
                        "point":3,
                        "usually_score":82,
                        "last_score":75,
                        "property":"必修课",
                        "score":79
                    },
                    {
                        "lesson_name":"软件设计与体系结构",
                        "credit":4,
                        "point":3.7,
                        "usually_score":92,
                        "last_score":78,
                        "property":"必修课",
                        "score":85
                    },
                    {
                        "lesson_name":"软件工程导论",
                        "credit":2,
                        "point":0,
                        "usually_score":"不及格",
                        "last_score":"不及格",
                        "property":"必修课",
                        "score":"不及格"
                    }
                ]
            }
        }
    }
}
```