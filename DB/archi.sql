--Para Kach!

DROP TABLE IF EXISTS Jugador CASCADE
;

DROP TABLE IF EXISTS Palabra CASCADE
;

CREATE TABLE Jugador (id_jugador serial PRIMARY KEY, nombre varchar(30), fecha timestamp without time zone NOT NULL, puntuacion bigint NOT NULL);

CREATE TABLE Palabra(id_palabra serial PRIMARY KEY, valor varchar(30) NOT NULL);

--Borrado de los datos que hay en la Base de Datos con respecto a las tablas mencionadas
DELETE FROM Jugador CASCADE;
DELETE FROM Palabra CASCADE;

INSERT INTO Jugador(id_jugador, nombre, fecha, puntuacion)
	VALUES (1, 'Admin', '2017-11-5', 1);

INSERT INTO Palabra(id_palabra, valor)
	VALUES (1, 'arbol'),
	(2, 'barco'),
	(3, 'carta'),
	(4, 'dado'),
	(5, 'elixir'),
	(6, 'faro'),
	(7, 'gato'),
	(8, 'hilo'),
	(9, 'indio'),
	(10, 'jaula'),
	(11, 'kilo'),
	(12, 'lira'),
	(13, 'mano'),
	(14, 'nota'),
	(15, 'oso'),
	(16, 'pato'),
	(17, 'queso'),
	(18, 'ramo'),
	(19, 'sapo'),
	(20, 'tina'),
	(21, 'uva'),
	(22, 'vino'),
	(23, 'abaco');
