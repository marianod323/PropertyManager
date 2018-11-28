CREATE DATABASE IF NOT EXISTS `proprietario`;
USE `proprietario`;

CREATE TABLE IF NOT EXISTS estado_civil (
  id_estado_civil int(11) NOT NULL AUTO_INCREMENT,
  nome varchar(50) DEFAULT NULL,
  PRIMARY KEY (id_estado_civil)
) AUTO_INCREMENT=7;

INSERT INTO estado_civil (id_estado_civil, nome) VALUES
	(1, 'Solteiro'),
	(2, 'Casado'),
	(3, 'Separado'),
	(4, 'Divorciado'),
	(5, 'Viúvo'),
	(6, 'Morto');


CREATE TABLE IF NOT EXISTS pessoa (
  id_pessoa int(11) unsigned NOT NULL AUTO_INCREMENT,
  id_conjuge int(11) unsigned DEFAULT NULL,
  estado_civil int(11) NOT NULL DEFAULT '1',
  nome varchar(50) DEFAULT NULL,
  endereco varchar(50) DEFAULT NULL,
  fone varchar(20) DEFAULT NULL,
  PRIMARY KEY (id_pessoa),
  KEY FK_pessoa_pessoa (id_conjuge),
  KEY FK_pessoa_estado_civil (estado_civil),
  CONSTRAINT FK_pessoa_estado_civil FOREIGN KEY (estado_civil) REFERENCES estado_civil (id_estado_civil) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT FK_pessoa_pessoa FOREIGN KEY (id_conjuge) REFERENCES pessoa (id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
) AUTO_INCREMENT=1;


CREATE TABLE IF NOT EXISTS veiculo (
  num_chassi varchar(50) NOT NULL,
  id_pessoa int(11) unsigned NOT NULL,
  data_da_compra varchar(50) DEFAULT NULL,
  preco float NOT NULL DEFAULT '0',
  cor varchar(50) DEFAULT NULL,
  ano int(11) NOT NULL DEFAULT '2018',
  modelo varchar(50) DEFAULT NULL,
  marca varchar(50) DEFAULT NULL,
  PRIMARY KEY (num_chassi),
  KEY FK_veiculo_pessoa (id_pessoa),
  CONSTRAINT FK_veiculo_pessoa FOREIGN KEY (id_pessoa) REFERENCES pessoa (id_pessoa) ON DELETE NO ACTION ON UPDATE NO ACTION
);

DELIMITER //
CREATE TRIGGER tr_viuvo_bens AFTER UPDATE ON pessoa FOR EACH ROW BEGIN

   UPDATE veiculo v
   JOIN pessoa p ON p.id_pessoa = v.id_pessoa
   JOIN pessoa p2 ON p2.id_conjuge = p.id_pessoa
   SET v.id_pessoa = p2.id_pessoa
   WHERE p2.estado_civil = 5;

   UPDATE veiculo v
   JOIN pessoa p ON v.id_pessoa = p.id_pessoa
   JOIN pessoa p2 ON p.id_conjuge = p2.id_pessoa
   SET v.id_pessoa = p2.id_pessoa
   WHERE p.estado_civil = 6;

END//
DELIMITER ;

CREATE VIEW vw_pessoas AS
SELECT p.id_pessoa AS id_pessoa,
       p.nome AS Nome,
       e.nome AS EstadoCivil,
       p.fone AS fone
       FROM pessoa p JOIN estado_civil e ON p.estado_civil = e.id_estado_civil;


CREATE VIEW vw_veiculos AS
SELECT v.id_pessoa AS id_pessoa,
       v.num_chassi AS num_chassi,
       v.modelo AS modelo,
       v.ano AS ano
       FROM veiculo v;
