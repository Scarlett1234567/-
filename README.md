# 辽宁大学自动填报程序

## 数据库
- 使用MySQL数据库，表结构为
```
-- 在校时期使用
create table inschool
(
    name        char(20)  null,
    password    char(100) null,
    provinces   char(100) null,
    area        char(50)  null,
    jd          char(100) null,
    community   char(100) null,
    room        char(200) null,
    temperature char(10)  null,
    location    char(100) null,
    ipLocation  char(100) null,
    username    char(100) null,
    status      int       null
);
```
```
-- 在家时使用
create table athome
(
    name        char(20)  null,
    password    char(100) null,
    provinces   char(100) null,
    area        char(50)  null,
    jd          char(100) null,
    community   char(100) null,
    room        char(200) null,
    temperature char(10)  null,
    location    char(100) null,
    ipLocation  char(100) null,
    username    char(100) null,
    status      int       null
);
```

## 登录验证码识别
- 百度即可，多数提供api可以直接使用
