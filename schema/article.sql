create table article
(
    id bigint not null auto_increment,
    user_name varchar(128),
    title varchar(128),
    content text,
    time Date,
    primary key(id)
) DEFAULT CHARACTER SET 'utf8';
ALTER TABLE article ADD INDEX IDX_TIME(time);
