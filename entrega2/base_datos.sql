-- Database generated with pgModeler (PostgreSQL Database Modeler).
-- pgModeler  version: 0.9.3
-- PostgreSQL version: 13.0
-- Project Site: pgmodeler.io
-- Model Author: ---

-- Database creation must be performed outside a multi lined SQL file. 
-- These commands were put in this file only as a convenience.
-- 
-- object: new_database | type: DATABASE --
-- DROP DATABASE IF EXISTS new_database;
CREATE DATABASE new_database;
-- ddl-end --


-- object: public.incidente | type: TABLE --
-- DROP TABLE IF EXISTS public.incidente CASCADE;
CREATE TABLE public.incidente (
	codigo varchar(15) NOT NULL,
	tipo varchar(45) NOT NULL,
	CONSTRAINT incidente_pk PRIMARY KEY (codigo)

);
-- ddl-end --
ALTER TABLE public.incidente OWNER TO postgres;
-- ddl-end --

-- object: public.llamada | type: TABLE --
-- DROP TABLE IF EXISTS public.llamada CASCADE;
CREATE TABLE public.llamada (
	id varchar(45) NOT NULL,
	anio integer NOT NULL,
	mes integer NOT NULL,
	acumulado_incidentes integer NOT NULL,
	codigo_incidente varchar(15),
	id_upz varchar(15),
	CONSTRAINT llamada_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.llamada OWNER TO postgres;
-- ddl-end --

-- object: public.localidad | type: TABLE --
-- DROP TABLE IF EXISTS public.localidad CASCADE;
CREATE TABLE public.localidad (
	id integer NOT NULL,
	nombre varchar(45) NOT NULL,
	CONSTRAINT localidad_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.localidad OWNER TO postgres;
-- ddl-end --

-- object: public.upz | type: TABLE --
-- DROP TABLE IF EXISTS public.upz CASCADE;
CREATE TABLE public.upz (
	id varchar(15) NOT NULL,
	nombre varchar(45) NOT NULL,
	id_localidad integer,
	CONSTRAINT upz_pk PRIMARY KEY (id)

);
-- ddl-end --
ALTER TABLE public.upz OWNER TO postgres;
-- ddl-end --

-- object: public.detalle_incidente | type: TABLE --
-- DROP TABLE IF EXISTS public.detalle_incidente CASCADE;
CREATE TABLE public.detalle_incidente (
	codigo_incidente varchar(15),
	detalle varchar(1650) NOT NULL
);
-- ddl-end --
ALTER TABLE public.detalle_incidente OWNER TO postgres;
-- ddl-end --

-- object: incidente_fk | type: CONSTRAINT --
-- ALTER TABLE public.llamada DROP CONSTRAINT IF EXISTS incidente_fk CASCADE;
ALTER TABLE public.llamada ADD CONSTRAINT incidente_fk FOREIGN KEY (codigo_incidente)
REFERENCES public.incidente (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: localidad_fk | type: CONSTRAINT --
-- ALTER TABLE public.upz DROP CONSTRAINT IF EXISTS localidad_fk CASCADE;
ALTER TABLE public.upz ADD CONSTRAINT localidad_fk FOREIGN KEY (id_localidad)
REFERENCES public.localidad (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: incidente_fk | type: CONSTRAINT --
-- ALTER TABLE public.detalle_incidente DROP CONSTRAINT IF EXISTS incidente_fk CASCADE;
ALTER TABLE public.detalle_incidente ADD CONSTRAINT incidente_fk FOREIGN KEY (codigo_incidente)
REFERENCES public.incidente (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: detalle_incidente_uq | type: CONSTRAINT --
-- ALTER TABLE public.detalle_incidente DROP CONSTRAINT IF EXISTS detalle_incidente_uq CASCADE;
ALTER TABLE public.detalle_incidente ADD CONSTRAINT detalle_incidente_uq UNIQUE (codigo_incidente);
-- ddl-end --

-- object: upz_fk | type: CONSTRAINT --
-- ALTER TABLE public.llamada DROP CONSTRAINT IF EXISTS upz_fk CASCADE;
ALTER TABLE public.llamada ADD CONSTRAINT upz_fk FOREIGN KEY (id_upz)
REFERENCES public.upz (id) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --


