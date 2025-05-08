--
-- PostgreSQL database dump
--

-- Dumped from database version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.8 (Ubuntu 16.8-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

-- *not* creating schema, since initdb creates it


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS '';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ability_scores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ability_scores (
    id integer NOT NULL,
    "desc" text,
    full_name character varying(255),
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.ability_scores OWNER TO postgres;

--
-- Name: ability_scores_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ability_scores_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ability_scores_id_seq OWNER TO postgres;

--
-- Name: ability_scores_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ability_scores_id_seq OWNED BY public.ability_scores.id;


--
-- Name: ability_scores_skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ability_scores_skills (
    id integer NOT NULL,
    ability_scores_id integer,
    skills_id integer
);


ALTER TABLE public.ability_scores_skills OWNER TO postgres;

--
-- Name: ability_scores_skills_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ability_scores_skills_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.ability_scores_skills_id_seq OWNER TO postgres;

--
-- Name: ability_scores_skills_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ability_scores_skills_id_seq OWNED BY public.ability_scores_skills.id;


--
-- Name: alignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alignments (
    id integer NOT NULL,
    abbreviation character varying(255),
    "desc" text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.alignments OWNER TO postgres;

--
-- Name: alignments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.alignments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.alignments_id_seq OWNER TO postgres;

--
-- Name: alignments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.alignments_id_seq OWNED BY public.alignments.id;


--
-- Name: backgrounds; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backgrounds (
    id integer NOT NULL,
    index character varying(255),
    language_options text,
    name character varying(255),
    starting_equipment text,
    starting_equipment_options text,
    starting_proficiencies text,
    url character varying(255)
);


ALTER TABLE public.backgrounds OWNER TO postgres;

--
-- Name: backgrounds_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backgrounds_equipment (
    id integer NOT NULL,
    backgrounds_id integer,
    equipment_id integer
);


ALTER TABLE public.backgrounds_equipment OWNER TO postgres;

--
-- Name: backgrounds_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backgrounds_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.backgrounds_equipment_id_seq OWNER TO postgres;

--
-- Name: backgrounds_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backgrounds_equipment_id_seq OWNED BY public.backgrounds_equipment.id;


--
-- Name: backgrounds_from_equipment_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backgrounds_from_equipment_category (
    id integer NOT NULL,
    backgrounds_id integer,
    equipment_categories_id integer
);


ALTER TABLE public.backgrounds_from_equipment_category OWNER TO postgres;

--
-- Name: backgrounds_from_equipment_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backgrounds_from_equipment_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.backgrounds_from_equipment_category_id_seq OWNER TO postgres;

--
-- Name: backgrounds_from_equipment_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backgrounds_from_equipment_category_id_seq OWNED BY public.backgrounds_from_equipment_category.id;


--
-- Name: backgrounds_from_options_alignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backgrounds_from_options_alignments (
    id integer NOT NULL,
    backgrounds_id integer,
    alignments_id integer
);


ALTER TABLE public.backgrounds_from_options_alignments OWNER TO postgres;

--
-- Name: backgrounds_from_options_alignments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backgrounds_from_options_alignments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.backgrounds_from_options_alignments_id_seq OWNER TO postgres;

--
-- Name: backgrounds_from_options_alignments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backgrounds_from_options_alignments_id_seq OWNED BY public.backgrounds_from_options_alignments.id;


--
-- Name: backgrounds_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backgrounds_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.backgrounds_id_seq OWNER TO postgres;

--
-- Name: backgrounds_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backgrounds_id_seq OWNED BY public.backgrounds.id;


--
-- Name: backgrounds_starting_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.backgrounds_starting_proficiencies (
    id integer NOT NULL,
    backgrounds_id integer,
    proficiencies_id integer
);


ALTER TABLE public.backgrounds_starting_proficiencies OWNER TO postgres;

--
-- Name: backgrounds_starting_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.backgrounds_starting_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.backgrounds_starting_proficiencies_id_seq OWNER TO postgres;

--
-- Name: backgrounds_starting_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.backgrounds_starting_proficiencies_id_seq OWNED BY public.backgrounds_starting_proficiencies.id;


--
-- Name: classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes (
    id integer NOT NULL,
    class_levels text,
    hit_die integer,
    index character varying(255),
    multi_classing text,
    name character varying(255),
    proficiency_choices text,
    proficiencies text,
    saving_throws text,
    starting_equipment text,
    starting_equipment_options text,
    subclasses text,
    url character varying(255)
);


ALTER TABLE public.classes OWNER TO postgres;

--
-- Name: classes_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_equipment (
    id integer NOT NULL,
    classes_id integer,
    equipment_id integer
);


ALTER TABLE public.classes_equipment OWNER TO postgres;

--
-- Name: classes_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_equipment_id_seq OWNER TO postgres;

--
-- Name: classes_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_equipment_id_seq OWNED BY public.classes_equipment.id;


--
-- Name: classes_from_options_choice_from_equipment_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_from_options_choice_from_equipment_category (
    id integer NOT NULL,
    classes_id integer,
    equipment_categories_id integer
);


ALTER TABLE public.classes_from_options_choice_from_equipment_category OWNER TO postgres;

--
-- Name: classes_from_options_choice_from_equipment_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_from_options_choice_from_equipment_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_from_options_choice_from_equipment_category_id_seq OWNER TO postgres;

--
-- Name: classes_from_options_choice_from_equipment_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_from_options_choice_from_equipment_category_id_seq OWNED BY public.classes_from_options_choice_from_equipment_category.id;


--
-- Name: classes_from_options_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_from_options_item (
    id integer NOT NULL,
    classes_id integer,
    proficiencies_id integer
);


ALTER TABLE public.classes_from_options_item OWNER TO postgres;

--
-- Name: classes_from_options_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_from_options_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_from_options_item_id_seq OWNER TO postgres;

--
-- Name: classes_from_options_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_from_options_item_id_seq OWNED BY public.classes_from_options_item.id;


--
-- Name: classes_from_options_of; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_from_options_of (
    id integer NOT NULL,
    classes_id integer,
    equipment_id integer
);


ALTER TABLE public.classes_from_options_of OWNER TO postgres;

--
-- Name: classes_from_options_of_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_from_options_of_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_from_options_of_id_seq OWNER TO postgres;

--
-- Name: classes_from_options_of_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_from_options_of_id_seq OWNED BY public.classes_from_options_of.id;


--
-- Name: classes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_id_seq OWNER TO postgres;

--
-- Name: classes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_id_seq OWNED BY public.classes.id;


--
-- Name: classes_prerequisites_ability_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_prerequisites_ability_score (
    id integer NOT NULL,
    classes_id integer,
    ability_scores_id integer
);


ALTER TABLE public.classes_prerequisites_ability_score OWNER TO postgres;

--
-- Name: classes_prerequisites_ability_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_prerequisites_ability_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_prerequisites_ability_score_id_seq OWNER TO postgres;

--
-- Name: classes_prerequisites_ability_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_prerequisites_ability_score_id_seq OWNED BY public.classes_prerequisites_ability_score.id;


--
-- Name: classes_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_proficiencies (
    id integer NOT NULL,
    classes_id integer,
    proficiencies_id integer
);


ALTER TABLE public.classes_proficiencies OWNER TO postgres;

--
-- Name: classes_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_proficiencies_id_seq OWNER TO postgres;

--
-- Name: classes_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_proficiencies_id_seq OWNED BY public.classes_proficiencies.id;


--
-- Name: classes_saving_throws; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_saving_throws (
    id integer NOT NULL,
    classes_id integer,
    ability_scores_id integer
);


ALTER TABLE public.classes_saving_throws OWNER TO postgres;

--
-- Name: classes_saving_throws_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_saving_throws_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_saving_throws_id_seq OWNER TO postgres;

--
-- Name: classes_saving_throws_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_saving_throws_id_seq OWNED BY public.classes_saving_throws.id;


--
-- Name: classes_starting_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_starting_equipment (
    id integer NOT NULL,
    classes_id integer,
    equipment_id integer
);


ALTER TABLE public.classes_starting_equipment OWNER TO postgres;

--
-- Name: classes_starting_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_starting_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_starting_equipment_id_seq OWNER TO postgres;

--
-- Name: classes_starting_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_starting_equipment_id_seq OWNED BY public.classes_starting_equipment.id;


--
-- Name: classes_starting_equipment_option_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_starting_equipment_option_categories (
    id integer NOT NULL,
    classes_id integer,
    equipment_categories_id integer
);


ALTER TABLE public.classes_starting_equipment_option_categories OWNER TO postgres;

--
-- Name: classes_starting_equipment_option_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_starting_equipment_option_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_starting_equipment_option_categories_id_seq OWNER TO postgres;

--
-- Name: classes_starting_equipment_option_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_starting_equipment_option_categories_id_seq OWNED BY public.classes_starting_equipment_option_categories.id;


--
-- Name: classes_starting_equipment_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_starting_equipment_options (
    id integer NOT NULL,
    classes_id integer,
    equipment_id integer
);


ALTER TABLE public.classes_starting_equipment_options OWNER TO postgres;

--
-- Name: classes_starting_equipment_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_starting_equipment_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_starting_equipment_options_id_seq OWNER TO postgres;

--
-- Name: classes_starting_equipment_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_starting_equipment_options_id_seq OWNED BY public.classes_starting_equipment_options.id;


--
-- Name: classes_subclasses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_subclasses (
    id integer NOT NULL,
    classes_id integer,
    subclasses_id integer
);


ALTER TABLE public.classes_subclasses OWNER TO postgres;

--
-- Name: classes_subclasses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_subclasses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_subclasses_id_seq OWNER TO postgres;

--
-- Name: classes_subclasses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_subclasses_id_seq OWNED BY public.classes_subclasses.id;


--
-- Name: conditions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.conditions (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.conditions OWNER TO postgres;

--
-- Name: conditions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.conditions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.conditions_id_seq OWNER TO postgres;

--
-- Name: conditions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.conditions_id_seq OWNED BY public.conditions.id;


--
-- Name: damage_types; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.damage_types (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.damage_types OWNER TO postgres;

--
-- Name: damage_types_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.damage_types_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.damage_types_id_seq OWNER TO postgres;

--
-- Name: damage_types_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.damage_types_id_seq OWNED BY public.damage_types.id;


--
-- Name: equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment (
    id integer NOT NULL,
    category_range character varying(255),
    cost text,
    damage text,
    "desc" text,
    equipment_category text,
    gear_category text,
    index character varying(255),
    name character varying(255),
    properties text,
    range text,
    special text,
    speed text,
    stealth_disadvantage boolean,
    str_minimum integer,
    throw_range text,
    tool_category character varying(255),
    two_handed_damage text,
    url character varying(255),
    vehicle_category character varying(255),
    weight character varying(255),
    weapon_category character varying(255),
    weapon_range character varying(255),
    weapon_range_type character varying(255)
);


ALTER TABLE public.equipment OWNER TO postgres;

--
-- Name: equipment_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_categories (
    id integer NOT NULL,
    equipment text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.equipment_categories OWNER TO postgres;

--
-- Name: equipment_categories_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_categories_equipment (
    id integer NOT NULL,
    equipment_categories_id integer,
    equipment_id integer
);


ALTER TABLE public.equipment_categories_equipment OWNER TO postgres;

--
-- Name: equipment_categories_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_categories_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_categories_equipment_id_seq OWNER TO postgres;

--
-- Name: equipment_categories_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_categories_equipment_id_seq OWNED BY public.equipment_categories_equipment.id;


--
-- Name: equipment_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_categories_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_categories_id_seq OWNER TO postgres;

--
-- Name: equipment_categories_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_categories_id_seq OWNED BY public.equipment_categories.id;


--
-- Name: equipment_damage_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_damage_type (
    id integer NOT NULL,
    equipment_id integer,
    damage_types_id integer
);


ALTER TABLE public.equipment_damage_type OWNER TO postgres;

--
-- Name: equipment_damage_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_damage_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_damage_type_id_seq OWNER TO postgres;

--
-- Name: equipment_damage_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_damage_type_id_seq OWNED BY public.equipment_damage_type.id;


--
-- Name: equipment_equipment_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_equipment_category (
    id integer NOT NULL,
    equipment_id integer,
    equipment_categories_id integer
);


ALTER TABLE public.equipment_equipment_category OWNER TO postgres;

--
-- Name: equipment_equipment_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_equipment_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_equipment_category_id_seq OWNER TO postgres;

--
-- Name: equipment_equipment_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_equipment_category_id_seq OWNED BY public.equipment_equipment_category.id;


--
-- Name: equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_id_seq OWNER TO postgres;

--
-- Name: equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_id_seq OWNED BY public.equipment.id;


--
-- Name: equipment_properties; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_properties (
    id integer NOT NULL,
    equipment_id integer,
    weapon_properties_id integer
);


ALTER TABLE public.equipment_properties OWNER TO postgres;

--
-- Name: equipment_properties_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipment_properties_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipment_properties_id_seq OWNER TO postgres;

--
-- Name: equipment_properties_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.equipment_properties_id_seq OWNED BY public.equipment_properties.id;


--
-- Name: feats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feats (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    prerequisites text,
    url character varying(255)
);


ALTER TABLE public.feats OWNER TO postgres;

--
-- Name: feats_ability_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feats_ability_score (
    id integer NOT NULL,
    feats_id integer,
    ability_scores_id integer
);


ALTER TABLE public.feats_ability_score OWNER TO postgres;

--
-- Name: feats_ability_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.feats_ability_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.feats_ability_score_id_seq OWNER TO postgres;

--
-- Name: feats_ability_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.feats_ability_score_id_seq OWNED BY public.feats_ability_score.id;


--
-- Name: feats_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.feats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.feats_id_seq OWNER TO postgres;

--
-- Name: feats_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.feats_id_seq OWNED BY public.feats.id;


--
-- Name: features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.features (
    id integer NOT NULL,
    class_ character varying(255),
    "desc" text,
    index character varying(255),
    level integer,
    name character varying(255),
    parent character varying(255),
    prerequisites text,
    subclass character varying(255),
    url character varying(255)
);


ALTER TABLE public.features OWNER TO postgres;

--
-- Name: features_class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.features_class (
    id integer NOT NULL,
    features_id integer,
    classes_id integer
);


ALTER TABLE public.features_class OWNER TO postgres;

--
-- Name: features_class_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.features_class_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.features_class_id_seq OWNER TO postgres;

--
-- Name: features_class_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.features_class_id_seq OWNED BY public.features_class.id;


--
-- Name: features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.features_id_seq OWNER TO postgres;

--
-- Name: features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.features_id_seq OWNED BY public.features.id;


--
-- Name: languages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.languages (
    id integer NOT NULL,
    index character varying(255),
    name character varying(255),
    script character varying(255),
    type character varying(255),
    url character varying(255)
);


ALTER TABLE public.languages OWNER TO postgres;

--
-- Name: languages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.languages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.languages_id_seq OWNER TO postgres;

--
-- Name: languages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.languages_id_seq OWNED BY public.languages.id;


--
-- Name: levels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.levels (
    id integer NOT NULL,
    index character varying(255),
    class_ character varying(255),
    level integer,
    ability_score_bonuses integer,
    prof_bonus integer,
    features text,
    spellcasting text,
    subclass character varying(255),
    url character varying(255)
);


ALTER TABLE public.levels OWNER TO postgres;

--
-- Name: levels_class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.levels_class (
    id integer NOT NULL,
    levels_id integer,
    classes_id integer
);


ALTER TABLE public.levels_class OWNER TO postgres;

--
-- Name: levels_class_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.levels_class_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.levels_class_id_seq OWNER TO postgres;

--
-- Name: levels_class_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.levels_class_id_seq OWNED BY public.levels_class.id;


--
-- Name: levels_features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.levels_features (
    id integer NOT NULL,
    levels_id integer,
    features_id integer
);


ALTER TABLE public.levels_features OWNER TO postgres;

--
-- Name: levels_features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.levels_features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.levels_features_id_seq OWNER TO postgres;

--
-- Name: levels_features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.levels_features_id_seq OWNED BY public.levels_features.id;


--
-- Name: levels_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.levels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.levels_id_seq OWNER TO postgres;

--
-- Name: levels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.levels_id_seq OWNED BY public.levels.id;


--
-- Name: magic_items; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.magic_items (
    id integer NOT NULL,
    "desc" text,
    equipment_category text,
    index character varying(255),
    name character varying(255),
    rarity text,
    url character varying(255)
);


ALTER TABLE public.magic_items OWNER TO postgres;

--
-- Name: magic_items_equipment_category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.magic_items_equipment_category (
    id integer NOT NULL,
    magic_items_id integer,
    equipment_categories_id integer
);


ALTER TABLE public.magic_items_equipment_category OWNER TO postgres;

--
-- Name: magic_items_equipment_category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.magic_items_equipment_category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.magic_items_equipment_category_id_seq OWNER TO postgres;

--
-- Name: magic_items_equipment_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.magic_items_equipment_category_id_seq OWNED BY public.magic_items_equipment_category.id;


--
-- Name: magic_items_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.magic_items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.magic_items_id_seq OWNER TO postgres;

--
-- Name: magic_items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.magic_items_id_seq OWNED BY public.magic_items.id;


--
-- Name: magic_schools; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.magic_schools (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.magic_schools OWNER TO postgres;

--
-- Name: magic_schools_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.magic_schools_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.magic_schools_id_seq OWNER TO postgres;

--
-- Name: magic_schools_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.magic_schools_id_seq OWNED BY public.magic_schools.id;


--
-- Name: monsters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters (
    id integer NOT NULL,
    actions text,
    alignment character varying(255),
    armor_class text,
    challenge_rating character varying(255),
    charisma integer,
    condition_immunities text,
    constitution integer,
    damage_immunities text,
    damage_resistances text,
    damage_vulnerabilities text,
    dexterity integer,
    forms text,
    hit_dice character varying(255),
    hit_points integer,
    index character varying(255),
    intelligence integer,
    languages character varying(255),
    legendary_actions text,
    legendary_desc text,
    name character varying(255),
    proficiencies text,
    reactions text,
    senses text,
    size character varying(255),
    special_abilities text,
    speed text,
    strength integer,
    subtype character varying(255),
    type character varying(255),
    url character varying(255),
    wisdom integer,
    xp integer
);


ALTER TABLE public.monsters OWNER TO postgres;

--
-- Name: monsters_condition_immunities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_condition_immunities (
    id integer NOT NULL,
    monsters_id integer,
    conditions_id integer
);


ALTER TABLE public.monsters_condition_immunities OWNER TO postgres;

--
-- Name: monsters_condition_immunities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_condition_immunities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_condition_immunities_id_seq OWNER TO postgres;

--
-- Name: monsters_condition_immunities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_condition_immunities_id_seq OWNED BY public.monsters_condition_immunities.id;


--
-- Name: monsters_damage_damage_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_damage_damage_type (
    id integer NOT NULL,
    monsters_id integer,
    damage_types_id integer
);


ALTER TABLE public.monsters_damage_damage_type OWNER TO postgres;

--
-- Name: monsters_damage_damage_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_damage_damage_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_damage_damage_type_id_seq OWNER TO postgres;

--
-- Name: monsters_damage_damage_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_damage_damage_type_id_seq OWNED BY public.monsters_damage_damage_type.id;


--
-- Name: monsters_dc_dc_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_dc_dc_type (
    id integer NOT NULL,
    monsters_id integer,
    ability_scores_id integer
);


ALTER TABLE public.monsters_dc_dc_type OWNER TO postgres;

--
-- Name: monsters_dc_dc_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_dc_dc_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_dc_dc_type_id_seq OWNER TO postgres;

--
-- Name: monsters_dc_dc_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_dc_dc_type_id_seq OWNED BY public.monsters_dc_dc_type.id;


--
-- Name: monsters_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_id_seq OWNER TO postgres;

--
-- Name: monsters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_id_seq OWNED BY public.monsters.id;


--
-- Name: monsters_proficiency; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_proficiency (
    id integer NOT NULL,
    monsters_id integer,
    proficiencies_id integer
);


ALTER TABLE public.monsters_proficiency OWNER TO postgres;

--
-- Name: monsters_proficiency_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_proficiency_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_proficiency_id_seq OWNER TO postgres;

--
-- Name: monsters_proficiency_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_proficiency_id_seq OWNED BY public.monsters_proficiency.id;


--
-- Name: proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proficiencies (
    id integer NOT NULL,
    index character varying(255),
    name character varying(255),
    "references" text,
    type character varying(255),
    url character varying(255)
);


ALTER TABLE public.proficiencies OWNER TO postgres;

--
-- Name: proficiencies_classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proficiencies_classes (
    id integer NOT NULL,
    proficiencies_id integer,
    classes_id integer
);


ALTER TABLE public.proficiencies_classes OWNER TO postgres;

--
-- Name: proficiencies_classes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proficiencies_classes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proficiencies_classes_id_seq OWNER TO postgres;

--
-- Name: proficiencies_classes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proficiencies_classes_id_seq OWNED BY public.proficiencies_classes.id;


--
-- Name: proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.proficiencies_id_seq OWNER TO postgres;

--
-- Name: proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.proficiencies_id_seq OWNED BY public.proficiencies.id;


--
-- Name: races; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races (
    id integer NOT NULL,
    ability_bonuses text,
    alignment character varying(255),
    age character varying(255),
    index character varying(255),
    language_desc text,
    language_options text,
    languages text,
    name character varying(255),
    size character varying(255),
    size_description text,
    speed integer,
    starting_proficiencies text,
    starting_proficiency_options text,
    subraces text,
    traits text,
    url character varying(255)
);


ALTER TABLE public.races OWNER TO postgres;

--
-- Name: races_ability_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_ability_score (
    id integer NOT NULL,
    races_id integer,
    ability_scores_id integer
);


ALTER TABLE public.races_ability_score OWNER TO postgres;

--
-- Name: races_ability_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_ability_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_ability_score_id_seq OWNER TO postgres;

--
-- Name: races_ability_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_ability_score_id_seq OWNED BY public.races_ability_score.id;


--
-- Name: races_from_options_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_from_options_item (
    id integer NOT NULL,
    races_id integer,
    proficiencies_id integer
);


ALTER TABLE public.races_from_options_item OWNER TO postgres;

--
-- Name: races_from_options_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_from_options_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_from_options_item_id_seq OWNER TO postgres;

--
-- Name: races_from_options_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_from_options_item_id_seq OWNED BY public.races_from_options_item.id;


--
-- Name: races_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_id_seq OWNER TO postgres;

--
-- Name: races_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_id_seq OWNED BY public.races.id;


--
-- Name: races_languages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_languages (
    id integer NOT NULL,
    races_id integer,
    languages_id integer
);


ALTER TABLE public.races_languages OWNER TO postgres;

--
-- Name: races_languages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_languages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_languages_id_seq OWNER TO postgres;

--
-- Name: races_languages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_languages_id_seq OWNED BY public.races_languages.id;


--
-- Name: races_starting_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_starting_proficiencies (
    id integer NOT NULL,
    races_id integer,
    proficiencies_id integer
);


ALTER TABLE public.races_starting_proficiencies OWNER TO postgres;

--
-- Name: races_starting_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_starting_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_starting_proficiencies_id_seq OWNER TO postgres;

--
-- Name: races_starting_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_starting_proficiencies_id_seq OWNED BY public.races_starting_proficiencies.id;


--
-- Name: races_subraces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_subraces (
    id integer NOT NULL,
    races_id integer,
    subraces_id integer
);


ALTER TABLE public.races_subraces OWNER TO postgres;

--
-- Name: races_subraces_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_subraces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_subraces_id_seq OWNER TO postgres;

--
-- Name: races_subraces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_subraces_id_seq OWNED BY public.races_subraces.id;


--
-- Name: races_traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races_traits (
    id integer NOT NULL,
    races_id integer,
    traits_id integer
);


ALTER TABLE public.races_traits OWNER TO postgres;

--
-- Name: races_traits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.races_traits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.races_traits_id_seq OWNER TO postgres;

--
-- Name: races_traits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.races_traits_id_seq OWNED BY public.races_traits.id;


--
-- Name: rule_sections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rule_sections (
    id integer NOT NULL,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.rule_sections OWNER TO postgres;

--
-- Name: rule_sections_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rule_sections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rule_sections_id_seq OWNER TO postgres;

--
-- Name: rule_sections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rule_sections_id_seq OWNED BY public.rule_sections.id;


--
-- Name: rules; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rules (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    subsections text,
    url character varying(255)
);


ALTER TABLE public.rules OWNER TO postgres;

--
-- Name: rules_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rules_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rules_id_seq OWNER TO postgres;

--
-- Name: rules_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rules_id_seq OWNED BY public.rules.id;


--
-- Name: rules_subsections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rules_subsections (
    id integer NOT NULL,
    rules_id integer,
    rule_sections_id integer
);


ALTER TABLE public.rules_subsections OWNER TO postgres;

--
-- Name: rules_subsections_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rules_subsections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rules_subsections_id_seq OWNER TO postgres;

--
-- Name: rules_subsections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rules_subsections_id_seq OWNED BY public.rules_subsections.id;


--
-- Name: skills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skills (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    ability_score text,
    url character varying(255)
);


ALTER TABLE public.skills OWNER TO postgres;

--
-- Name: skills_ability_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.skills_ability_score (
    id integer NOT NULL,
    skills_id integer,
    ability_scores_id integer
);


ALTER TABLE public.skills_ability_score OWNER TO postgres;

--
-- Name: skills_ability_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.skills_ability_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.skills_ability_score_id_seq OWNER TO postgres;

--
-- Name: skills_ability_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.skills_ability_score_id_seq OWNED BY public.skills_ability_score.id;


--
-- Name: skills_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.skills_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.skills_id_seq OWNER TO postgres;

--
-- Name: skills_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.skills_id_seq OWNED BY public.skills.id;


--
-- Name: spells; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells (
    id integer NOT NULL,
    area_of_effect text,
    attack_type character varying(255),
    casting_time character varying(255),
    classes text,
    components text,
    concentration boolean,
    damage text,
    dc text,
    "desc" text,
    duration character varying(255),
    healing text,
    higher_level text,
    index character varying(255),
    level integer,
    material character varying(255),
    name character varying(255),
    range character varying(255),
    ritual boolean,
    saving_throw character varying(255),
    school text,
    subclasses text,
    url character varying(255),
    usage text
);


ALTER TABLE public.spells OWNER TO postgres;

--
-- Name: spells_classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_classes (
    id integer NOT NULL,
    spells_id integer,
    classes_id integer
);


ALTER TABLE public.spells_classes OWNER TO postgres;

--
-- Name: spells_classes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_classes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_classes_id_seq OWNER TO postgres;

--
-- Name: spells_classes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_classes_id_seq OWNED BY public.spells_classes.id;


--
-- Name: spells_conditions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_conditions (
    id integer NOT NULL,
    spells_id integer,
    conditions_id integer
);


ALTER TABLE public.spells_conditions OWNER TO postgres;

--
-- Name: spells_conditions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_conditions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_conditions_id_seq OWNER TO postgres;

--
-- Name: spells_conditions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_conditions_id_seq OWNED BY public.spells_conditions.id;


--
-- Name: spells_damage_type; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_damage_type (
    id integer NOT NULL,
    spells_id integer,
    damage_types_id integer
);


ALTER TABLE public.spells_damage_type OWNER TO postgres;

--
-- Name: spells_damage_type_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_damage_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_damage_type_id_seq OWNER TO postgres;

--
-- Name: spells_damage_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_damage_type_id_seq OWNED BY public.spells_damage_type.id;


--
-- Name: spells_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_id_seq OWNER TO postgres;

--
-- Name: spells_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_id_seq OWNED BY public.spells.id;


--
-- Name: spells_school; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_school (
    id integer NOT NULL,
    spells_id integer,
    magic_schools_id integer
);


ALTER TABLE public.spells_school OWNER TO postgres;

--
-- Name: spells_school_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_school_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_school_id_seq OWNER TO postgres;

--
-- Name: spells_school_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_school_id_seq OWNED BY public.spells_school.id;


--
-- Name: spells_subclasses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_subclasses (
    id integer NOT NULL,
    spells_id integer,
    subclasses_id integer
);


ALTER TABLE public.spells_subclasses OWNER TO postgres;

--
-- Name: spells_subclasses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.spells_subclasses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.spells_subclasses_id_seq OWNER TO postgres;

--
-- Name: spells_subclasses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.spells_subclasses_id_seq OWNED BY public.spells_subclasses.id;


--
-- Name: starting_equipment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.starting_equipment (
    id integer NOT NULL,
    class_ character varying(255),
    equipment text,
    url character varying(255)
);


ALTER TABLE public.starting_equipment OWNER TO postgres;

--
-- Name: starting_equipment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.starting_equipment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.starting_equipment_id_seq OWNER TO postgres;

--
-- Name: starting_equipment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.starting_equipment_id_seq OWNED BY public.starting_equipment.id;


--
-- Name: starting_equipment_option; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.starting_equipment_option (
    id integer NOT NULL,
    "desc" text,
    choose integer
);


ALTER TABLE public.starting_equipment_option OWNER TO postgres;

--
-- Name: starting_equipment_option_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.starting_equipment_option_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.starting_equipment_option_id_seq OWNER TO postgres;

--
-- Name: starting_equipment_option_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.starting_equipment_option_id_seq OWNED BY public.starting_equipment_option.id;


--
-- Name: starting_equipment_option_item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.starting_equipment_option_item (
    id integer NOT NULL,
    option_id integer,
    equipment_id integer,
    equipment_category_id integer,
    quantity integer
);


ALTER TABLE public.starting_equipment_option_item OWNER TO postgres;

--
-- Name: starting_equipment_option_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.starting_equipment_option_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.starting_equipment_option_item_id_seq OWNER TO postgres;

--
-- Name: starting_equipment_option_item_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.starting_equipment_option_item_id_seq OWNED BY public.starting_equipment_option_item.id;


--
-- Name: subclasses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subclasses (
    id integer NOT NULL,
    class_ character varying(255),
    index character varying(255),
    name character varying(255),
    spells text,
    subclass_flavor character varying(255),
    subclass_levels text,
    url character varying(255)
);


ALTER TABLE public.subclasses OWNER TO postgres;

--
-- Name: subclasses_class; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subclasses_class (
    id integer NOT NULL,
    subclasses_id integer,
    classes_id integer
);


ALTER TABLE public.subclasses_class OWNER TO postgres;

--
-- Name: subclasses_class_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subclasses_class_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subclasses_class_id_seq OWNER TO postgres;

--
-- Name: subclasses_class_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subclasses_class_id_seq OWNED BY public.subclasses_class.id;


--
-- Name: subclasses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subclasses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subclasses_id_seq OWNER TO postgres;

--
-- Name: subclasses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subclasses_id_seq OWNED BY public.subclasses.id;


--
-- Name: subraces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subraces (
    id integer NOT NULL,
    index character varying(255),
    language_options text,
    name character varying(255),
    race text,
    racial_traits text,
    starting_proficiencies text,
    url character varying(255)
);


ALTER TABLE public.subraces OWNER TO postgres;

--
-- Name: subraces_ability_score; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subraces_ability_score (
    id integer NOT NULL,
    subraces_id integer,
    ability_scores_id integer
);


ALTER TABLE public.subraces_ability_score OWNER TO postgres;

--
-- Name: subraces_ability_score_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subraces_ability_score_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subraces_ability_score_id_seq OWNER TO postgres;

--
-- Name: subraces_ability_score_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subraces_ability_score_id_seq OWNED BY public.subraces_ability_score.id;


--
-- Name: subraces_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subraces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subraces_id_seq OWNER TO postgres;

--
-- Name: subraces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subraces_id_seq OWNED BY public.subraces.id;


--
-- Name: subraces_race; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subraces_race (
    id integer NOT NULL,
    subraces_id integer,
    races_id integer
);


ALTER TABLE public.subraces_race OWNER TO postgres;

--
-- Name: subraces_race_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subraces_race_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subraces_race_id_seq OWNER TO postgres;

--
-- Name: subraces_race_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subraces_race_id_seq OWNED BY public.subraces_race.id;


--
-- Name: subraces_racial_traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subraces_racial_traits (
    id integer NOT NULL,
    subraces_id integer,
    traits_id integer
);


ALTER TABLE public.subraces_racial_traits OWNER TO postgres;

--
-- Name: subraces_racial_traits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subraces_racial_traits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subraces_racial_traits_id_seq OWNER TO postgres;

--
-- Name: subraces_racial_traits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subraces_racial_traits_id_seq OWNED BY public.subraces_racial_traits.id;


--
-- Name: traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.traits (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    proficiencies text,
    races text,
    subraces text,
    url character varying(255)
);


ALTER TABLE public.traits OWNER TO postgres;

--
-- Name: traits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.traits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.traits_id_seq OWNER TO postgres;

--
-- Name: traits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.traits_id_seq OWNED BY public.traits.id;


--
-- Name: traits_races; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.traits_races (
    id integer NOT NULL,
    traits_id integer,
    races_id integer
);


ALTER TABLE public.traits_races OWNER TO postgres;

--
-- Name: traits_races_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.traits_races_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.traits_races_id_seq OWNER TO postgres;

--
-- Name: traits_races_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.traits_races_id_seq OWNED BY public.traits_races.id;


--
-- Name: weapon_properties; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.weapon_properties (
    id integer NOT NULL,
    "desc" text,
    index character varying(255),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.weapon_properties OWNER TO postgres;

--
-- Name: weapon_properties_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.weapon_properties_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.weapon_properties_id_seq OWNER TO postgres;

--
-- Name: weapon_properties_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.weapon_properties_id_seq OWNED BY public.weapon_properties.id;


--
-- Name: ability_scores id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores ALTER COLUMN id SET DEFAULT nextval('public.ability_scores_id_seq'::regclass);


--
-- Name: ability_scores_skills id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores_skills ALTER COLUMN id SET DEFAULT nextval('public.ability_scores_skills_id_seq'::regclass);


--
-- Name: alignments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alignments ALTER COLUMN id SET DEFAULT nextval('public.alignments_id_seq'::regclass);


--
-- Name: backgrounds id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds ALTER COLUMN id SET DEFAULT nextval('public.backgrounds_id_seq'::regclass);


--
-- Name: backgrounds_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_equipment ALTER COLUMN id SET DEFAULT nextval('public.backgrounds_equipment_id_seq'::regclass);


--
-- Name: backgrounds_from_equipment_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_equipment_category ALTER COLUMN id SET DEFAULT nextval('public.backgrounds_from_equipment_category_id_seq'::regclass);


--
-- Name: backgrounds_from_options_alignments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_options_alignments ALTER COLUMN id SET DEFAULT nextval('public.backgrounds_from_options_alignments_id_seq'::regclass);


--
-- Name: backgrounds_starting_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_starting_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.backgrounds_starting_proficiencies_id_seq'::regclass);


--
-- Name: classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes ALTER COLUMN id SET DEFAULT nextval('public.classes_id_seq'::regclass);


--
-- Name: classes_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_equipment ALTER COLUMN id SET DEFAULT nextval('public.classes_equipment_id_seq'::regclass);


--
-- Name: classes_from_options_choice_from_equipment_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_choice_from_equipment_category ALTER COLUMN id SET DEFAULT nextval('public.classes_from_options_choice_from_equipment_category_id_seq'::regclass);


--
-- Name: classes_from_options_item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_item ALTER COLUMN id SET DEFAULT nextval('public.classes_from_options_item_id_seq'::regclass);


--
-- Name: classes_from_options_of id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_of ALTER COLUMN id SET DEFAULT nextval('public.classes_from_options_of_id_seq'::regclass);


--
-- Name: classes_prerequisites_ability_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_prerequisites_ability_score ALTER COLUMN id SET DEFAULT nextval('public.classes_prerequisites_ability_score_id_seq'::regclass);


--
-- Name: classes_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.classes_proficiencies_id_seq'::regclass);


--
-- Name: classes_saving_throws id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws ALTER COLUMN id SET DEFAULT nextval('public.classes_saving_throws_id_seq'::regclass);


--
-- Name: classes_starting_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment ALTER COLUMN id SET DEFAULT nextval('public.classes_starting_equipment_id_seq'::regclass);


--
-- Name: classes_starting_equipment_option_categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_option_categories ALTER COLUMN id SET DEFAULT nextval('public.classes_starting_equipment_option_categories_id_seq'::regclass);


--
-- Name: classes_starting_equipment_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options ALTER COLUMN id SET DEFAULT nextval('public.classes_starting_equipment_options_id_seq'::regclass);


--
-- Name: classes_subclasses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_subclasses ALTER COLUMN id SET DEFAULT nextval('public.classes_subclasses_id_seq'::regclass);


--
-- Name: conditions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conditions ALTER COLUMN id SET DEFAULT nextval('public.conditions_id_seq'::regclass);


--
-- Name: damage_types id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.damage_types ALTER COLUMN id SET DEFAULT nextval('public.damage_types_id_seq'::regclass);


--
-- Name: equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment ALTER COLUMN id SET DEFAULT nextval('public.equipment_id_seq'::regclass);


--
-- Name: equipment_categories id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories ALTER COLUMN id SET DEFAULT nextval('public.equipment_categories_id_seq'::regclass);


--
-- Name: equipment_categories_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories_equipment ALTER COLUMN id SET DEFAULT nextval('public.equipment_categories_equipment_id_seq'::regclass);


--
-- Name: equipment_damage_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_damage_type ALTER COLUMN id SET DEFAULT nextval('public.equipment_damage_type_id_seq'::regclass);


--
-- Name: equipment_equipment_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_equipment_category ALTER COLUMN id SET DEFAULT nextval('public.equipment_equipment_category_id_seq'::regclass);


--
-- Name: equipment_properties id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties ALTER COLUMN id SET DEFAULT nextval('public.equipment_properties_id_seq'::regclass);


--
-- Name: feats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats ALTER COLUMN id SET DEFAULT nextval('public.feats_id_seq'::regclass);


--
-- Name: feats_ability_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats_ability_score ALTER COLUMN id SET DEFAULT nextval('public.feats_ability_score_id_seq'::regclass);


--
-- Name: features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features ALTER COLUMN id SET DEFAULT nextval('public.features_id_seq'::regclass);


--
-- Name: features_class id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features_class ALTER COLUMN id SET DEFAULT nextval('public.features_class_id_seq'::regclass);


--
-- Name: languages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages ALTER COLUMN id SET DEFAULT nextval('public.languages_id_seq'::regclass);


--
-- Name: levels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels ALTER COLUMN id SET DEFAULT nextval('public.levels_id_seq'::regclass);


--
-- Name: levels_class id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_class ALTER COLUMN id SET DEFAULT nextval('public.levels_class_id_seq'::regclass);


--
-- Name: levels_features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_features ALTER COLUMN id SET DEFAULT nextval('public.levels_features_id_seq'::regclass);


--
-- Name: magic_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items ALTER COLUMN id SET DEFAULT nextval('public.magic_items_id_seq'::regclass);


--
-- Name: magic_items_equipment_category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items_equipment_category ALTER COLUMN id SET DEFAULT nextval('public.magic_items_equipment_category_id_seq'::regclass);


--
-- Name: magic_schools id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_schools ALTER COLUMN id SET DEFAULT nextval('public.magic_schools_id_seq'::regclass);


--
-- Name: monsters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters ALTER COLUMN id SET DEFAULT nextval('public.monsters_id_seq'::regclass);


--
-- Name: monsters_condition_immunities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_condition_immunities ALTER COLUMN id SET DEFAULT nextval('public.monsters_condition_immunities_id_seq'::regclass);


--
-- Name: monsters_damage_damage_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_damage_damage_type ALTER COLUMN id SET DEFAULT nextval('public.monsters_damage_damage_type_id_seq'::regclass);


--
-- Name: monsters_dc_dc_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_dc_dc_type ALTER COLUMN id SET DEFAULT nextval('public.monsters_dc_dc_type_id_seq'::regclass);


--
-- Name: monsters_proficiency id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_proficiency ALTER COLUMN id SET DEFAULT nextval('public.monsters_proficiency_id_seq'::regclass);


--
-- Name: proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies ALTER COLUMN id SET DEFAULT nextval('public.proficiencies_id_seq'::regclass);


--
-- Name: proficiencies_classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies_classes ALTER COLUMN id SET DEFAULT nextval('public.proficiencies_classes_id_seq'::regclass);


--
-- Name: races id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races ALTER COLUMN id SET DEFAULT nextval('public.races_id_seq'::regclass);


--
-- Name: races_ability_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_ability_score ALTER COLUMN id SET DEFAULT nextval('public.races_ability_score_id_seq'::regclass);


--
-- Name: races_from_options_item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_from_options_item ALTER COLUMN id SET DEFAULT nextval('public.races_from_options_item_id_seq'::regclass);


--
-- Name: races_languages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_languages ALTER COLUMN id SET DEFAULT nextval('public.races_languages_id_seq'::regclass);


--
-- Name: races_starting_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_starting_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.races_starting_proficiencies_id_seq'::regclass);


--
-- Name: races_subraces id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_subraces ALTER COLUMN id SET DEFAULT nextval('public.races_subraces_id_seq'::regclass);


--
-- Name: races_traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_traits ALTER COLUMN id SET DEFAULT nextval('public.races_traits_id_seq'::regclass);


--
-- Name: rule_sections id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rule_sections ALTER COLUMN id SET DEFAULT nextval('public.rule_sections_id_seq'::regclass);


--
-- Name: rules id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules ALTER COLUMN id SET DEFAULT nextval('public.rules_id_seq'::regclass);


--
-- Name: rules_subsections id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections ALTER COLUMN id SET DEFAULT nextval('public.rules_subsections_id_seq'::regclass);


--
-- Name: skills id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills ALTER COLUMN id SET DEFAULT nextval('public.skills_id_seq'::regclass);


--
-- Name: skills_ability_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills_ability_score ALTER COLUMN id SET DEFAULT nextval('public.skills_ability_score_id_seq'::regclass);


--
-- Name: spells id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells ALTER COLUMN id SET DEFAULT nextval('public.spells_id_seq'::regclass);


--
-- Name: spells_classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes ALTER COLUMN id SET DEFAULT nextval('public.spells_classes_id_seq'::regclass);


--
-- Name: spells_conditions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_conditions ALTER COLUMN id SET DEFAULT nextval('public.spells_conditions_id_seq'::regclass);


--
-- Name: spells_damage_type id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_damage_type ALTER COLUMN id SET DEFAULT nextval('public.spells_damage_type_id_seq'::regclass);


--
-- Name: spells_school id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_school ALTER COLUMN id SET DEFAULT nextval('public.spells_school_id_seq'::regclass);


--
-- Name: spells_subclasses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses ALTER COLUMN id SET DEFAULT nextval('public.spells_subclasses_id_seq'::regclass);


--
-- Name: starting_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment ALTER COLUMN id SET DEFAULT nextval('public.starting_equipment_id_seq'::regclass);


--
-- Name: starting_equipment_option id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option ALTER COLUMN id SET DEFAULT nextval('public.starting_equipment_option_id_seq'::regclass);


--
-- Name: starting_equipment_option_item id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option_item ALTER COLUMN id SET DEFAULT nextval('public.starting_equipment_option_item_id_seq'::regclass);


--
-- Name: subclasses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses ALTER COLUMN id SET DEFAULT nextval('public.subclasses_id_seq'::regclass);


--
-- Name: subclasses_class id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class ALTER COLUMN id SET DEFAULT nextval('public.subclasses_class_id_seq'::regclass);


--
-- Name: subraces id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces ALTER COLUMN id SET DEFAULT nextval('public.subraces_id_seq'::regclass);


--
-- Name: subraces_ability_score id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_ability_score ALTER COLUMN id SET DEFAULT nextval('public.subraces_ability_score_id_seq'::regclass);


--
-- Name: subraces_race id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_race ALTER COLUMN id SET DEFAULT nextval('public.subraces_race_id_seq'::regclass);


--
-- Name: subraces_racial_traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_racial_traits ALTER COLUMN id SET DEFAULT nextval('public.subraces_racial_traits_id_seq'::regclass);


--
-- Name: traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits ALTER COLUMN id SET DEFAULT nextval('public.traits_id_seq'::regclass);


--
-- Name: traits_races id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_races ALTER COLUMN id SET DEFAULT nextval('public.traits_races_id_seq'::regclass);


--
-- Name: weapon_properties id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon_properties ALTER COLUMN id SET DEFAULT nextval('public.weapon_properties_id_seq'::regclass);


--
-- Name: ability_scores ability_scores_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores
    ADD CONSTRAINT ability_scores_pkey PRIMARY KEY (id);


--
-- Name: ability_scores_skills ability_scores_skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores_skills
    ADD CONSTRAINT ability_scores_skills_pkey PRIMARY KEY (id);


--
-- Name: alignments alignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alignments
    ADD CONSTRAINT alignments_pkey PRIMARY KEY (id);


--
-- Name: backgrounds_equipment backgrounds_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_equipment
    ADD CONSTRAINT backgrounds_equipment_pkey PRIMARY KEY (id);


--
-- Name: backgrounds_from_equipment_category backgrounds_from_equipment_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_equipment_category
    ADD CONSTRAINT backgrounds_from_equipment_category_pkey PRIMARY KEY (id);


--
-- Name: backgrounds_from_options_alignments backgrounds_from_options_alignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_options_alignments
    ADD CONSTRAINT backgrounds_from_options_alignments_pkey PRIMARY KEY (id);


--
-- Name: backgrounds backgrounds_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds
    ADD CONSTRAINT backgrounds_pkey PRIMARY KEY (id);


--
-- Name: backgrounds_starting_proficiencies backgrounds_starting_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_starting_proficiencies
    ADD CONSTRAINT backgrounds_starting_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: classes_equipment classes_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_equipment
    ADD CONSTRAINT classes_equipment_pkey PRIMARY KEY (id);


--
-- Name: classes_from_options_choice_from_equipment_category classes_from_options_choice_from_equipment_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_choice_from_equipment_category
    ADD CONSTRAINT classes_from_options_choice_from_equipment_category_pkey PRIMARY KEY (id);


--
-- Name: classes_from_options_item classes_from_options_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_item
    ADD CONSTRAINT classes_from_options_item_pkey PRIMARY KEY (id);


--
-- Name: classes_from_options_of classes_from_options_of_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_of
    ADD CONSTRAINT classes_from_options_of_pkey PRIMARY KEY (id);


--
-- Name: classes classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_pkey PRIMARY KEY (id);


--
-- Name: classes_prerequisites_ability_score classes_prerequisites_ability_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_prerequisites_ability_score
    ADD CONSTRAINT classes_prerequisites_ability_score_pkey PRIMARY KEY (id);


--
-- Name: classes_proficiencies classes_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: classes_saving_throws classes_saving_throws_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_pkey PRIMARY KEY (id);


--
-- Name: classes_starting_equipment_option_categories classes_starting_equipment_option_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_option_categories
    ADD CONSTRAINT classes_starting_equipment_option_categories_pkey PRIMARY KEY (id);


--
-- Name: classes_starting_equipment_options classes_starting_equipment_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options
    ADD CONSTRAINT classes_starting_equipment_options_pkey PRIMARY KEY (id);


--
-- Name: classes_starting_equipment classes_starting_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment
    ADD CONSTRAINT classes_starting_equipment_pkey PRIMARY KEY (id);


--
-- Name: classes_subclasses classes_subclasses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_subclasses
    ADD CONSTRAINT classes_subclasses_pkey PRIMARY KEY (id);


--
-- Name: conditions conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.conditions
    ADD CONSTRAINT conditions_pkey PRIMARY KEY (id);


--
-- Name: damage_types damage_types_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.damage_types
    ADD CONSTRAINT damage_types_pkey PRIMARY KEY (id);


--
-- Name: equipment_categories_equipment equipment_categories_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories_equipment
    ADD CONSTRAINT equipment_categories_equipment_pkey PRIMARY KEY (id);


--
-- Name: equipment_categories equipment_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories
    ADD CONSTRAINT equipment_categories_pkey PRIMARY KEY (id);


--
-- Name: equipment_damage_type equipment_damage_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_damage_type
    ADD CONSTRAINT equipment_damage_type_pkey PRIMARY KEY (id);


--
-- Name: equipment_equipment_category equipment_equipment_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_equipment_category
    ADD CONSTRAINT equipment_equipment_category_pkey PRIMARY KEY (id);


--
-- Name: equipment equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT equipment_pkey PRIMARY KEY (id);


--
-- Name: equipment_properties equipment_properties_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT equipment_properties_pkey PRIMARY KEY (id);


--
-- Name: feats_ability_score feats_ability_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats_ability_score
    ADD CONSTRAINT feats_ability_score_pkey PRIMARY KEY (id);


--
-- Name: feats feats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats
    ADD CONSTRAINT feats_pkey PRIMARY KEY (id);


--
-- Name: features_class features_class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features_class
    ADD CONSTRAINT features_class_pkey PRIMARY KEY (id);


--
-- Name: features features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT features_pkey PRIMARY KEY (id);


--
-- Name: languages languages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages
    ADD CONSTRAINT languages_pkey PRIMARY KEY (id);


--
-- Name: levels_class levels_class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_class
    ADD CONSTRAINT levels_class_pkey PRIMARY KEY (id);


--
-- Name: levels_features levels_features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_features
    ADD CONSTRAINT levels_features_pkey PRIMARY KEY (id);


--
-- Name: levels levels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_pkey PRIMARY KEY (id);


--
-- Name: magic_items_equipment_category magic_items_equipment_category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items_equipment_category
    ADD CONSTRAINT magic_items_equipment_category_pkey PRIMARY KEY (id);


--
-- Name: magic_items magic_items_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items
    ADD CONSTRAINT magic_items_pkey PRIMARY KEY (id);


--
-- Name: magic_schools magic_schools_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_schools
    ADD CONSTRAINT magic_schools_pkey PRIMARY KEY (id);


--
-- Name: monsters_condition_immunities monsters_condition_immunities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_condition_immunities
    ADD CONSTRAINT monsters_condition_immunities_pkey PRIMARY KEY (id);


--
-- Name: monsters_damage_damage_type monsters_damage_damage_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_damage_damage_type
    ADD CONSTRAINT monsters_damage_damage_type_pkey PRIMARY KEY (id);


--
-- Name: monsters_dc_dc_type monsters_dc_dc_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_dc_dc_type
    ADD CONSTRAINT monsters_dc_dc_type_pkey PRIMARY KEY (id);


--
-- Name: monsters monsters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters
    ADD CONSTRAINT monsters_pkey PRIMARY KEY (id);


--
-- Name: monsters_proficiency monsters_proficiency_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_proficiency
    ADD CONSTRAINT monsters_proficiency_pkey PRIMARY KEY (id);


--
-- Name: proficiencies_classes proficiencies_classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies_classes
    ADD CONSTRAINT proficiencies_classes_pkey PRIMARY KEY (id);


--
-- Name: proficiencies proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT proficiencies_pkey PRIMARY KEY (id);


--
-- Name: races_ability_score races_ability_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_ability_score
    ADD CONSTRAINT races_ability_score_pkey PRIMARY KEY (id);


--
-- Name: races_from_options_item races_from_options_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_from_options_item
    ADD CONSTRAINT races_from_options_item_pkey PRIMARY KEY (id);


--
-- Name: races_languages races_languages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_languages
    ADD CONSTRAINT races_languages_pkey PRIMARY KEY (id);


--
-- Name: races races_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_pkey PRIMARY KEY (id);


--
-- Name: races_starting_proficiencies races_starting_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_starting_proficiencies
    ADD CONSTRAINT races_starting_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: races_subraces races_subraces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_subraces
    ADD CONSTRAINT races_subraces_pkey PRIMARY KEY (id);


--
-- Name: races_traits races_traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_traits
    ADD CONSTRAINT races_traits_pkey PRIMARY KEY (id);


--
-- Name: rule_sections rule_sections_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rule_sections
    ADD CONSTRAINT rule_sections_pkey PRIMARY KEY (id);


--
-- Name: rules rules_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules
    ADD CONSTRAINT rules_pkey PRIMARY KEY (id);


--
-- Name: rules_subsections rules_subsections_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections
    ADD CONSTRAINT rules_subsections_pkey PRIMARY KEY (id);


--
-- Name: skills_ability_score skills_ability_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills_ability_score
    ADD CONSTRAINT skills_ability_score_pkey PRIMARY KEY (id);


--
-- Name: skills skills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT skills_pkey PRIMARY KEY (id);


--
-- Name: spells_classes spells_classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes
    ADD CONSTRAINT spells_classes_pkey PRIMARY KEY (id);


--
-- Name: spells_conditions spells_conditions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_conditions
    ADD CONSTRAINT spells_conditions_pkey PRIMARY KEY (id);


--
-- Name: spells_damage_type spells_damage_type_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_damage_type
    ADD CONSTRAINT spells_damage_type_pkey PRIMARY KEY (id);


--
-- Name: spells spells_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT spells_pkey PRIMARY KEY (id);


--
-- Name: spells_school spells_school_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_school
    ADD CONSTRAINT spells_school_pkey PRIMARY KEY (id);


--
-- Name: spells_subclasses spells_subclasses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_pkey PRIMARY KEY (id);


--
-- Name: starting_equipment_option_item starting_equipment_option_item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option_item
    ADD CONSTRAINT starting_equipment_option_item_pkey PRIMARY KEY (id);


--
-- Name: starting_equipment_option starting_equipment_option_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option
    ADD CONSTRAINT starting_equipment_option_pkey PRIMARY KEY (id);


--
-- Name: starting_equipment starting_equipment_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment
    ADD CONSTRAINT starting_equipment_pkey PRIMARY KEY (id);


--
-- Name: subclasses_class subclasses_class_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class
    ADD CONSTRAINT subclasses_class_pkey PRIMARY KEY (id);


--
-- Name: subclasses subclasses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses
    ADD CONSTRAINT subclasses_pkey PRIMARY KEY (id);


--
-- Name: subraces_ability_score subraces_ability_score_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_ability_score
    ADD CONSTRAINT subraces_ability_score_pkey PRIMARY KEY (id);


--
-- Name: subraces subraces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces
    ADD CONSTRAINT subraces_pkey PRIMARY KEY (id);


--
-- Name: subraces_race subraces_race_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_race
    ADD CONSTRAINT subraces_race_pkey PRIMARY KEY (id);


--
-- Name: subraces_racial_traits subraces_racial_traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_racial_traits
    ADD CONSTRAINT subraces_racial_traits_pkey PRIMARY KEY (id);


--
-- Name: traits traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT traits_pkey PRIMARY KEY (id);


--
-- Name: traits_races traits_races_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_races
    ADD CONSTRAINT traits_races_pkey PRIMARY KEY (id);


--
-- Name: weapon_properties weapon_properties_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon_properties
    ADD CONSTRAINT weapon_properties_pkey PRIMARY KEY (id);


--
-- Name: ability_scores_skills ability_scores_skills_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores_skills
    ADD CONSTRAINT ability_scores_skills_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: ability_scores_skills ability_scores_skills_skills_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ability_scores_skills
    ADD CONSTRAINT ability_scores_skills_skills_id_fkey FOREIGN KEY (skills_id) REFERENCES public.skills(id);


--
-- Name: backgrounds_equipment backgrounds_equipment_backgrounds_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_equipment
    ADD CONSTRAINT backgrounds_equipment_backgrounds_id_fkey FOREIGN KEY (backgrounds_id) REFERENCES public.backgrounds(id);


--
-- Name: backgrounds_equipment backgrounds_equipment_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_equipment
    ADD CONSTRAINT backgrounds_equipment_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: backgrounds_from_equipment_category backgrounds_from_equipment_categor_equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_equipment_category
    ADD CONSTRAINT backgrounds_from_equipment_categor_equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: backgrounds_from_equipment_category backgrounds_from_equipment_category_backgrounds_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_equipment_category
    ADD CONSTRAINT backgrounds_from_equipment_category_backgrounds_id_fkey FOREIGN KEY (backgrounds_id) REFERENCES public.backgrounds(id);


--
-- Name: backgrounds_from_options_alignments backgrounds_from_options_alignments_alignments_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_options_alignments
    ADD CONSTRAINT backgrounds_from_options_alignments_alignments_id_fkey FOREIGN KEY (alignments_id) REFERENCES public.alignments(id);


--
-- Name: backgrounds_from_options_alignments backgrounds_from_options_alignments_backgrounds_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_from_options_alignments
    ADD CONSTRAINT backgrounds_from_options_alignments_backgrounds_id_fkey FOREIGN KEY (backgrounds_id) REFERENCES public.backgrounds(id);


--
-- Name: backgrounds_starting_proficiencies backgrounds_starting_proficiencies_backgrounds_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_starting_proficiencies
    ADD CONSTRAINT backgrounds_starting_proficiencies_backgrounds_id_fkey FOREIGN KEY (backgrounds_id) REFERENCES public.backgrounds(id);


--
-- Name: backgrounds_starting_proficiencies backgrounds_starting_proficiencies_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.backgrounds_starting_proficiencies
    ADD CONSTRAINT backgrounds_starting_proficiencies_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: classes_equipment classes_equipment_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_equipment
    ADD CONSTRAINT classes_equipment_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_equipment classes_equipment_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_equipment
    ADD CONSTRAINT classes_equipment_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: classes_from_options_choice_from_equipment_category classes_from_options_choice_from_e_equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_choice_from_equipment_category
    ADD CONSTRAINT classes_from_options_choice_from_e_equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: classes_from_options_choice_from_equipment_category classes_from_options_choice_from_equipment_cate_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_choice_from_equipment_category
    ADD CONSTRAINT classes_from_options_choice_from_equipment_cate_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_from_options_item classes_from_options_item_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_item
    ADD CONSTRAINT classes_from_options_item_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_from_options_item classes_from_options_item_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_item
    ADD CONSTRAINT classes_from_options_item_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: classes_from_options_of classes_from_options_of_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_of
    ADD CONSTRAINT classes_from_options_of_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_from_options_of classes_from_options_of_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_from_options_of
    ADD CONSTRAINT classes_from_options_of_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: classes_prerequisites_ability_score classes_prerequisites_ability_score_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_prerequisites_ability_score
    ADD CONSTRAINT classes_prerequisites_ability_score_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: classes_prerequisites_ability_score classes_prerequisites_ability_score_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_prerequisites_ability_score
    ADD CONSTRAINT classes_prerequisites_ability_score_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_proficiencies classes_proficiencies_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_proficiencies classes_proficiencies_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: classes_saving_throws classes_saving_throws_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: classes_saving_throws classes_saving_throws_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_starting_equipment classes_starting_equipment_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment
    ADD CONSTRAINT classes_starting_equipment_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_starting_equipment classes_starting_equipment_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment
    ADD CONSTRAINT classes_starting_equipment_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: classes_starting_equipment_option_categories classes_starting_equipment_option__equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_option_categories
    ADD CONSTRAINT classes_starting_equipment_option__equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: classes_starting_equipment_option_categories classes_starting_equipment_option_categories_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_option_categories
    ADD CONSTRAINT classes_starting_equipment_option_categories_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_starting_equipment_options classes_starting_equipment_options_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options
    ADD CONSTRAINT classes_starting_equipment_options_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_starting_equipment_options classes_starting_equipment_options_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options
    ADD CONSTRAINT classes_starting_equipment_options_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: classes_subclasses classes_subclasses_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_subclasses
    ADD CONSTRAINT classes_subclasses_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: classes_subclasses classes_subclasses_subclasses_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_subclasses
    ADD CONSTRAINT classes_subclasses_subclasses_id_fkey FOREIGN KEY (subclasses_id) REFERENCES public.subclasses(id);


--
-- Name: equipment_categories_equipment equipment_categories_equipment_equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories_equipment
    ADD CONSTRAINT equipment_categories_equipment_equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: equipment_categories_equipment equipment_categories_equipment_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories_equipment
    ADD CONSTRAINT equipment_categories_equipment_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: equipment_damage_type equipment_damage_type_damage_types_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_damage_type
    ADD CONSTRAINT equipment_damage_type_damage_types_id_fkey FOREIGN KEY (damage_types_id) REFERENCES public.damage_types(id);


--
-- Name: equipment_damage_type equipment_damage_type_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_damage_type
    ADD CONSTRAINT equipment_damage_type_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: equipment_equipment_category equipment_equipment_category_equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_equipment_category
    ADD CONSTRAINT equipment_equipment_category_equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: equipment_equipment_category equipment_equipment_category_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_equipment_category
    ADD CONSTRAINT equipment_equipment_category_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: equipment_properties equipment_properties_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT equipment_properties_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: equipment_properties equipment_properties_weapon_properties_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT equipment_properties_weapon_properties_id_fkey FOREIGN KEY (weapon_properties_id) REFERENCES public.weapon_properties(id);


--
-- Name: feats_ability_score feats_ability_score_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats_ability_score
    ADD CONSTRAINT feats_ability_score_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: feats_ability_score feats_ability_score_feats_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats_ability_score
    ADD CONSTRAINT feats_ability_score_feats_id_fkey FOREIGN KEY (feats_id) REFERENCES public.feats(id);


--
-- Name: features_class features_class_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features_class
    ADD CONSTRAINT features_class_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: features_class features_class_features_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features_class
    ADD CONSTRAINT features_class_features_id_fkey FOREIGN KEY (features_id) REFERENCES public.features(id);


--
-- Name: levels_class levels_class_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_class
    ADD CONSTRAINT levels_class_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: levels_class levels_class_levels_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_class
    ADD CONSTRAINT levels_class_levels_id_fkey FOREIGN KEY (levels_id) REFERENCES public.levels(id);


--
-- Name: levels_features levels_features_features_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_features
    ADD CONSTRAINT levels_features_features_id_fkey FOREIGN KEY (features_id) REFERENCES public.features(id);


--
-- Name: levels_features levels_features_levels_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels_features
    ADD CONSTRAINT levels_features_levels_id_fkey FOREIGN KEY (levels_id) REFERENCES public.levels(id);


--
-- Name: magic_items_equipment_category magic_items_equipment_category_equipment_categories_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items_equipment_category
    ADD CONSTRAINT magic_items_equipment_category_equipment_categories_id_fkey FOREIGN KEY (equipment_categories_id) REFERENCES public.equipment_categories(id);


--
-- Name: magic_items_equipment_category magic_items_equipment_category_magic_items_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items_equipment_category
    ADD CONSTRAINT magic_items_equipment_category_magic_items_id_fkey FOREIGN KEY (magic_items_id) REFERENCES public.magic_items(id);


--
-- Name: monsters_condition_immunities monsters_condition_immunities_conditions_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_condition_immunities
    ADD CONSTRAINT monsters_condition_immunities_conditions_id_fkey FOREIGN KEY (conditions_id) REFERENCES public.conditions(id);


--
-- Name: monsters_condition_immunities monsters_condition_immunities_monsters_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_condition_immunities
    ADD CONSTRAINT monsters_condition_immunities_monsters_id_fkey FOREIGN KEY (monsters_id) REFERENCES public.monsters(id);


--
-- Name: monsters_damage_damage_type monsters_damage_damage_type_damage_types_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_damage_damage_type
    ADD CONSTRAINT monsters_damage_damage_type_damage_types_id_fkey FOREIGN KEY (damage_types_id) REFERENCES public.damage_types(id);


--
-- Name: monsters_damage_damage_type monsters_damage_damage_type_monsters_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_damage_damage_type
    ADD CONSTRAINT monsters_damage_damage_type_monsters_id_fkey FOREIGN KEY (monsters_id) REFERENCES public.monsters(id);


--
-- Name: monsters_dc_dc_type monsters_dc_dc_type_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_dc_dc_type
    ADD CONSTRAINT monsters_dc_dc_type_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: monsters_dc_dc_type monsters_dc_dc_type_monsters_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_dc_dc_type
    ADD CONSTRAINT monsters_dc_dc_type_monsters_id_fkey FOREIGN KEY (monsters_id) REFERENCES public.monsters(id);


--
-- Name: monsters_proficiency monsters_proficiency_monsters_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_proficiency
    ADD CONSTRAINT monsters_proficiency_monsters_id_fkey FOREIGN KEY (monsters_id) REFERENCES public.monsters(id);


--
-- Name: monsters_proficiency monsters_proficiency_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_proficiency
    ADD CONSTRAINT monsters_proficiency_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: proficiencies_classes proficiencies_classes_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies_classes
    ADD CONSTRAINT proficiencies_classes_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: proficiencies_classes proficiencies_classes_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies_classes
    ADD CONSTRAINT proficiencies_classes_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: races_ability_score races_ability_score_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_ability_score
    ADD CONSTRAINT races_ability_score_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: races_ability_score races_ability_score_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_ability_score
    ADD CONSTRAINT races_ability_score_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_from_options_item races_from_options_item_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_from_options_item
    ADD CONSTRAINT races_from_options_item_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: races_from_options_item races_from_options_item_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_from_options_item
    ADD CONSTRAINT races_from_options_item_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_languages races_languages_languages_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_languages
    ADD CONSTRAINT races_languages_languages_id_fkey FOREIGN KEY (languages_id) REFERENCES public.languages(id);


--
-- Name: races_languages races_languages_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_languages
    ADD CONSTRAINT races_languages_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_starting_proficiencies races_starting_proficiencies_proficiencies_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_starting_proficiencies
    ADD CONSTRAINT races_starting_proficiencies_proficiencies_id_fkey FOREIGN KEY (proficiencies_id) REFERENCES public.proficiencies(id);


--
-- Name: races_starting_proficiencies races_starting_proficiencies_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_starting_proficiencies
    ADD CONSTRAINT races_starting_proficiencies_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_subraces races_subraces_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_subraces
    ADD CONSTRAINT races_subraces_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_subraces races_subraces_subraces_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_subraces
    ADD CONSTRAINT races_subraces_subraces_id_fkey FOREIGN KEY (subraces_id) REFERENCES public.subraces(id);


--
-- Name: races_traits races_traits_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_traits
    ADD CONSTRAINT races_traits_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: races_traits races_traits_traits_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races_traits
    ADD CONSTRAINT races_traits_traits_id_fkey FOREIGN KEY (traits_id) REFERENCES public.traits(id);


--
-- Name: rules_subsections rules_subsections_rule_sections_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections
    ADD CONSTRAINT rules_subsections_rule_sections_id_fkey FOREIGN KEY (rule_sections_id) REFERENCES public.rule_sections(id);


--
-- Name: rules_subsections rules_subsections_rules_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections
    ADD CONSTRAINT rules_subsections_rules_id_fkey FOREIGN KEY (rules_id) REFERENCES public.rules(id);


--
-- Name: skills_ability_score skills_ability_score_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills_ability_score
    ADD CONSTRAINT skills_ability_score_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: skills_ability_score skills_ability_score_skills_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills_ability_score
    ADD CONSTRAINT skills_ability_score_skills_id_fkey FOREIGN KEY (skills_id) REFERENCES public.skills(id);


--
-- Name: spells_classes spells_classes_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes
    ADD CONSTRAINT spells_classes_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: spells_classes spells_classes_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes
    ADD CONSTRAINT spells_classes_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(id);


--
-- Name: spells_conditions spells_conditions_conditions_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_conditions
    ADD CONSTRAINT spells_conditions_conditions_id_fkey FOREIGN KEY (conditions_id) REFERENCES public.conditions(id);


--
-- Name: spells_conditions spells_conditions_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_conditions
    ADD CONSTRAINT spells_conditions_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(id);


--
-- Name: spells_damage_type spells_damage_type_damage_types_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_damage_type
    ADD CONSTRAINT spells_damage_type_damage_types_id_fkey FOREIGN KEY (damage_types_id) REFERENCES public.damage_types(id);


--
-- Name: spells_damage_type spells_damage_type_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_damage_type
    ADD CONSTRAINT spells_damage_type_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(id);


--
-- Name: spells_school spells_school_magic_schools_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_school
    ADD CONSTRAINT spells_school_magic_schools_id_fkey FOREIGN KEY (magic_schools_id) REFERENCES public.magic_schools(id);


--
-- Name: spells_school spells_school_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_school
    ADD CONSTRAINT spells_school_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(id);


--
-- Name: spells_subclasses spells_subclasses_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(id);


--
-- Name: spells_subclasses spells_subclasses_subclasses_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_subclasses_id_fkey FOREIGN KEY (subclasses_id) REFERENCES public.subclasses(id);


--
-- Name: starting_equipment_option_item starting_equipment_option_item_equipment_category_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option_item
    ADD CONSTRAINT starting_equipment_option_item_equipment_category_id_fkey FOREIGN KEY (equipment_category_id) REFERENCES public.equipment_categories(id);


--
-- Name: starting_equipment_option_item starting_equipment_option_item_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option_item
    ADD CONSTRAINT starting_equipment_option_item_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id);


--
-- Name: starting_equipment_option_item starting_equipment_option_item_option_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.starting_equipment_option_item
    ADD CONSTRAINT starting_equipment_option_item_option_id_fkey FOREIGN KEY (option_id) REFERENCES public.starting_equipment_option(id);


--
-- Name: subclasses_class subclasses_class_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class
    ADD CONSTRAINT subclasses_class_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: subclasses_class subclasses_class_subclasses_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class
    ADD CONSTRAINT subclasses_class_subclasses_id_fkey FOREIGN KEY (subclasses_id) REFERENCES public.subclasses(id);


--
-- Name: subraces_ability_score subraces_ability_score_ability_scores_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_ability_score
    ADD CONSTRAINT subraces_ability_score_ability_scores_id_fkey FOREIGN KEY (ability_scores_id) REFERENCES public.ability_scores(id);


--
-- Name: subraces_ability_score subraces_ability_score_subraces_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_ability_score
    ADD CONSTRAINT subraces_ability_score_subraces_id_fkey FOREIGN KEY (subraces_id) REFERENCES public.subraces(id);


--
-- Name: subraces_race subraces_race_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_race
    ADD CONSTRAINT subraces_race_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: subraces_race subraces_race_subraces_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_race
    ADD CONSTRAINT subraces_race_subraces_id_fkey FOREIGN KEY (subraces_id) REFERENCES public.subraces(id);


--
-- Name: subraces_racial_traits subraces_racial_traits_subraces_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_racial_traits
    ADD CONSTRAINT subraces_racial_traits_subraces_id_fkey FOREIGN KEY (subraces_id) REFERENCES public.subraces(id);


--
-- Name: subraces_racial_traits subraces_racial_traits_traits_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces_racial_traits
    ADD CONSTRAINT subraces_racial_traits_traits_id_fkey FOREIGN KEY (traits_id) REFERENCES public.traits(id);


--
-- Name: traits_races traits_races_races_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_races
    ADD CONSTRAINT traits_races_races_id_fkey FOREIGN KEY (races_id) REFERENCES public.races(id);


--
-- Name: traits_races traits_races_traits_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_races
    ADD CONSTRAINT traits_races_traits_id_fkey FOREIGN KEY (traits_id) REFERENCES public.traits(id);


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE USAGE ON SCHEMA public FROM PUBLIC;


--
-- PostgreSQL database dump complete
--

