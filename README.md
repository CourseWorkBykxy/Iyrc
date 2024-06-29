# Iyrc
墨韵读书会

## 简介
IyrcUI使用Python的Tinker库构建，是负责处理用户交互的边界类  
IyrcManager是控制类，负责控制业务流程  
IyrcDB使用SQLLite构建，是存储相关信息的实体类

## 数据库表结构
USER Table  
用户表，存储用户相关信息

| Field     | Type    | Constraints |
|-----------|---------|-------------|
| ID        | INT     | PRIMARY KEY, NOT NULL |
| USERNAME  | TEXT    | NOT NULL    |
| PASSWORD  | TEXT    | NOT NULL    |
| EMAIL     | TEXT    |             |
| TYPE      | TEXT    | NOT NULL    |

BOOK Table  
书籍表，存放书籍相关信息

| Field     | Type    | Constraints |
|-----------|---------|-------------|
| ID        | INT     | PRIMARY KEY, NOT NULL |
| NAME      | TEXT    | NOT NULL    |
| AUTHOR    | TEXT    | NOT NULL    |
| TEXT      | TEXT    |             |

BLOG Table  
博客表，存储博客相关信息

| Field        | Type    | Constraints              |
|--------------|---------|--------------------------|
| ID           | INT     | PRIMARY KEY, NOT NULL     |
| TITLE        | TEXT    | NOT NULL                 |
| AUTHOR       | TEXT    | NOT NULL                 |
| CREATE_TIME  | INT     | NOT NULL                 |
| CHANGE_TIME  | INT     | NOT NULL                 |
| TEXT         | TEXT    |                          |

USERBOOK Table  
用户书籍表，存储用户的书架信息

| Field     | Type    | Constraints |
|-----------|---------|-------------|
| USERID    | TEXT    | NOT NULL    |
| BOOKID    | TEXT    | NOT NULL    |

