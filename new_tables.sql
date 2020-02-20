DROP TABLE if exists VOLUME;
#
create table if not exists VOLUME (
  volumeid INT unsigned not null,
  magazineid int not null,
  publicationyear year(4),
  CONSTRAINT fk_magazine FOREIGN KEY (magazineid) REFERENCES MAGAZINE(_id),
  primary key(volumeid,magazineid),
  UNIQUE KEY magazine_vol_year (volumeid,magazineid,publicationyear)
) engine = innodb;

DROP TABLE if exists ARTICLES;
#
create table if not exists ARTICLES (
  articleid INT not null auto_increment,
  volumeid int unsigned not null,
  title varchar(50) not null,
  pageno varchar(50), 
  primary key(articleid),
CONSTRAINT fk_vol FOREIGN KEY (volumeid) REFERENCES VOLUME(volumeid)
) engine = innodb;

DROP TABLE if exists ARTICLE_WRITTEN;
#
create table if not exists ARTICLE_WRITTEN (
  article_id INT not null,
  author_id INT not null ,
  CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES AUTHOR(_id),
  CONSTRAINT fk_article FOREIGN KEY (article_id) REFERENCES ARTICLES(articleid),
  primary key (author_id,article_id)
) engine = innodb;

DROP TABLE if exists CUSTOMER;
#
create table if not exists CUSTOMER (
  customerid INT not null auto_increment,
  fname varchar(30) not null,
  lname varchar(30) ,
  phonenumber varchar(50) ,
  address varchar(50),
  discountcode INT(11),
  primary key(customerid)
  ) engine = innodb;

DROP TABLE if exists TRANSACTIONS;
# 
create table if not exists TRANSACTIONS (
  transactionno INT not null auto_increment,
  transactiondate date ,
  totalpurchaseprice float,
  customerid int,
  CONSTRAINT fk_customer FOREIGN KEY (customerid) REFERENCES CUSTOMER(customerid),
  primary key(transactionno)
  ) engine = innodb;

  
DROP TABLE if exists TRANSACTIONDETAIL;
# 
create table if not exists TRANSACTIONDETAIL(
  transactionno INT not null ,
  itemid BIGINT not null,
  quantity INT, quantity_price float,
  CONSTRAINT fk_transact FOREIGN KEY (transactionno) REFERENCES TRANSACTIONS(transactionno),
  CONSTRAINT fk_item FOREIGN KEY (itemid) REFERENCES ITEM(_id),primary key (transactionno, itemid)
) engine = innodb;

