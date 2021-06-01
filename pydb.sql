-- CREATE DATABASE pydb;

-- CREATE TABLE ferramenta_comunic(
-- 	id SERIAL PRIMARY KEY,
-- 	nome CHARACTER VARYING(80) NOT NULL
-- );

-- CREATE TABLE linguagem_programacao(
-- 	id SERIAL PRIMARY KEY,
-- 	nome CHARACTER VARYING(80) NOT NULL
-- );

-- CREATE TABLE sistema_operacional(
-- 	id SERIAL PRIMARY KEY,
-- 	nome CHARACTER VARYING(80) NOT NULL
-- );

-- CREATE TABLE empresa(
-- 	id SERIAL PRIMARY KEY,
-- 	tamanho CHARACTER VARYING(80) NOT NULL
-- );

-- CREATE TABLE pais(
-- 	id SERIAL PRIMARY KEY,
-- 	nome CHARACTER VARYING(80)
-- );

-- CREATE TABLE respondente(
-- 	id SERIAL PRIMARY KEY,
-- 	nome CHARACTER VARYING(80) NOT NULL,
-- 	contrib_open_source VARCHAR(20) NOT NULL,
-- 	programa_hobby VARCHAR(20) NOT NULL,
-- 	salario DECIMAL(10,2) NOT NULL,
-- 	sistema_operacional_id INT REFERENCES sistema_operacional(id) NOT NULL,
-- 	pais_id INT REFERENCES pais(id) NOT NULL,
-- 	empresa_id INT REFERENCES empresa(id) NOT NULL
-- );

-- CREATE TABLE resp_usa_ferramenta(
-- 	ferramenta_comunic_id INT REFERENCES ferramenta_comunic(id) NOT NULL,
-- 	respondente_id INT REFERENCES respondente(id) NOT NULL
-- );

-- CREATE TABLE resp_usa_linguagem(
-- 	respondete_id INT REFERENCES respondente(id) NOT NULL,
-- 	linguagem_programacao_id INT REFERENCES linguagem_programacao(id) NOT NULL
-- );


SELECT * FROM respondente;





