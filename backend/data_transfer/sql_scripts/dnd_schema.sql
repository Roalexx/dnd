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
-- Name: set_detail_id_to_self(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.set_detail_id_to_self() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  UPDATE levels
  SET detail_id = NEW.id
  WHERE id = NEW.id;
  
  RETURN NEW;
END;
$$;


ALTER FUNCTION public.set_detail_id_to_self() OWNER TO postgres;

--
-- Name: sync_levels_detail_id(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.sync_levels_detail_id() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
  -- detail_id = levels_detail.id olan bir level varsa, eşle
  UPDATE levels
  SET detail_id = NEW.id
  WHERE id = NEW.id;
  
  RETURN NEW;
END;
$$;


ALTER FUNCTION public.sync_levels_detail_id() OWNER TO postgres;

--
-- Name: sync_properties_with_id(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.sync_properties_with_id() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.properties := NEW.id;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.sync_properties_with_id() OWNER TO postgres;

--
-- Name: sync_subsections(); Type: FUNCTION; Schema: public; Owner: postgres
--

CREATE FUNCTION public.sync_subsections() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.subsections := NEW.id;
    RETURN NEW;
END;
$$;


ALTER FUNCTION public.sync_subsections() OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ability_scores; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ability_scores (
    id integer NOT NULL,
    description text,
    full_name character varying(255),
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
-- Name: alignments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alignments (
    id integer NOT NULL,
    description text,
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
-- Name: class_multi_classing_prerequisites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.class_multi_classing_prerequisites (
    id integer NOT NULL,
    class_id integer,
    ability_score_id integer,
    minimum_score integer NOT NULL
);


ALTER TABLE public.class_multi_classing_prerequisites OWNER TO postgres;

--
-- Name: class_multi_classing_prerequisites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.class_multi_classing_prerequisites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.class_multi_classing_prerequisites_id_seq OWNER TO postgres;

--
-- Name: class_multi_classing_prerequisites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.class_multi_classing_prerequisites_id_seq OWNED BY public.class_multi_classing_prerequisites.id;


--
-- Name: class_multi_classing_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.class_multi_classing_proficiencies (
    id integer NOT NULL,
    class_id integer,
    proficiency_id integer
);


ALTER TABLE public.class_multi_classing_proficiencies OWNER TO postgres;

--
-- Name: class_multi_classing_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.class_multi_classing_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.class_multi_classing_proficiencies_id_seq OWNER TO postgres;

--
-- Name: class_multi_classing_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.class_multi_classing_proficiencies_id_seq OWNED BY public.class_multi_classing_proficiencies.id;


--
-- Name: classes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes (
    id integer NOT NULL,
    hit_die integer,
    name character varying(255),
    url character varying(255),
    class_levels integer,
    multi_classing integer,
    proficiency_choices integer,
    proficiencies integer,
    saving_throws integer,
    starting_equipment integer,
    starting_equipment_options integer,
    spellcasting_level integer,
    spellcasting_ability_id integer,
    spellcasting_name character varying(255),
    spellcasting_description text,
    subclass_id integer,
    proficiency_choices_desc text,
    proficiency_choices_choose integer,
    starting_equipment_options_choose integer,
    starting_equipment_options_desc text
);


ALTER TABLE public.classes OWNER TO postgres;

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
-- Name: classes_levels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_levels (
    id integer NOT NULL,
    class_id integer,
    level_id integer
);


ALTER TABLE public.classes_levels OWNER TO postgres;

--
-- Name: classes_levels_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_levels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_levels_id_seq OWNER TO postgres;

--
-- Name: classes_levels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_levels_id_seq OWNED BY public.classes_levels.id;


--
-- Name: classes_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_proficiencies (
    id integer NOT NULL,
    class_id integer,
    proficiency_id integer
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
-- Name: classes_proficiency_choices; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_proficiency_choices (
    id integer NOT NULL,
    class_id integer,
    proficiency_id integer
);


ALTER TABLE public.classes_proficiency_choices OWNER TO postgres;

--
-- Name: classes_proficiency_choices_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.classes_proficiency_choices_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.classes_proficiency_choices_id_seq OWNER TO postgres;

--
-- Name: classes_proficiency_choices_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.classes_proficiency_choices_id_seq OWNED BY public.classes_proficiency_choices.id;


--
-- Name: classes_saving_throws; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_saving_throws (
    id integer NOT NULL,
    class_id integer,
    ability_score_id integer
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
    class_id integer,
    equipment_id integer,
    quantity integer NOT NULL
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
-- Name: classes_starting_equipment_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.classes_starting_equipment_options (
    id integer NOT NULL,
    class_id integer,
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
-- Name: conditions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.conditions (
    id integer NOT NULL,
    description text,
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
    description text,
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
    damage_dice character varying(255),
    description text,
    equipment_category integer,
    gear_category integer,
    name character varying(255),
    properties integer,
    range_normal integer,
    special text,
    speed_quantity integer,
    stealth_disadvantage boolean,
    str_minimum integer,
    throw_range_normal integer,
    tool_category character varying(255),
    two_handed_damage_dice character varying(255),
    url character varying(255),
    vehicle_category character varying(255),
    weight integer,
    weapon_category character varying(255),
    weapon_range character varying(255),
    cost_quantity integer,
    cost_unit character varying(255),
    damage_type integer,
    range_long integer,
    speed_unit character varying(255),
    two_handed_damage_type integer,
    throw_range_long integer
);


ALTER TABLE public.equipment OWNER TO postgres;

--
-- Name: equipments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.equipments_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.equipments_id_seq OWNER TO postgres;

--
-- Name: equipment_categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.equipment_categories (
    id integer NOT NULL,
    equipments integer DEFAULT nextval('public.equipments_id_seq'::regclass),
    name character varying(255),
    url character varying(255)
);


ALTER TABLE public.equipment_categories OWNER TO postgres;

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
    equipment_property_key integer,
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
-- Name: expertises; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.expertises (
    id integer NOT NULL,
    expertise_id integer,
    proficiency_id integer
);


ALTER TABLE public.expertises OWNER TO postgres;

--
-- Name: expertises_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.expertises ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.expertises_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: feats; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feats (
    id integer NOT NULL,
    description text,
    name character varying(255),
    ability_score integer,
    url character varying(255),
    minimum_score integer
);


ALTER TABLE public.feats OWNER TO postgres;

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
-- Name: feature_specific; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.feature_specific (
    id integer NOT NULL,
    feature_specific_id integer,
    description text,
    enemy_type_options text,
    choose integer,
    terrain_type_options text,
    invocation_id integer,
    subfeature_id integer,
    expertise_id integer
);


ALTER TABLE public.feature_specific OWNER TO postgres;

--
-- Name: feature_specific_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.feature_specific ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.feature_specific_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.features (
    id integer NOT NULL,
    class_id integer,
    description text,
    level integer,
    name character varying(255),
    parent_id integer,
    prerequisites_id integer,
    subclass_id integer,
    url character varying(255),
    feature_spesific_id integer
);


ALTER TABLE public.features OWNER TO postgres;

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
-- Name: invocations; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.invocations (
    id integer NOT NULL,
    invocation_id integer,
    feature_id integer
);


ALTER TABLE public.invocations OWNER TO postgres;

--
-- Name: invocations_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.invocations ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.invocations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: languages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.languages (
    id integer NOT NULL,
    name character varying(255),
    script character varying(255),
    type character varying(255),
    url character varying(255),
    description text,
    typical_speakers text
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
-- Name: level_detail; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.level_detail (
    id integer NOT NULL,
    cantrips_known integer,
    spells_known integer,
    spell_slots_level_1 integer,
    spell_slots_level_2 integer,
    spell_slots_level_3 integer,
    spell_slots_level_4 integer,
    spell_slots_level_5 integer,
    spell_slots_level_6 integer,
    spell_slots_level_7 integer,
    spell_slots_level_8 integer,
    spell_slots_level_9 integer,
    rage_count integer,
    rage_damage_bonus integer,
    brutal_critical_dice integer,
    bardic_inspiration_die integer,
    song_of_rest_die integer,
    magical_secrets_max_5 integer,
    magical_secrets_max_7 integer,
    magical_secrets_max_9 integer,
    wild_shape_max_cr integer,
    wild_shape_swim boolean,
    wild_shape_fly boolean,
    extra_attacks integer,
    action_surges integer,
    indomitable_uses integer,
    channel_divinity_charges integer,
    destroy_undead_cr integer,
    additional_magical_secrets_max_lvl integer,
    features_id integer
);


ALTER TABLE public.level_detail OWNER TO postgres;

--
-- Name: level_detail_features; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.level_detail_features (
    id integer NOT NULL,
    level_detail_id integer NOT NULL,
    feature_id integer NOT NULL
);


ALTER TABLE public.level_detail_features OWNER TO postgres;

--
-- Name: level_detail_features_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.level_detail_features_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.level_detail_features_id_seq OWNER TO postgres;

--
-- Name: level_detail_features_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.level_detail_features_id_seq OWNED BY public.level_detail_features.id;


--
-- Name: level_detail_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.level_detail_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.level_detail_id_seq OWNER TO postgres;

--
-- Name: level_detail_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.level_detail_id_seq OWNED BY public.level_detail.id;


--
-- Name: levels; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.levels (
    id integer NOT NULL,
    level integer NOT NULL,
    class_id integer NOT NULL,
    subclass_id integer,
    ability_score_bonuses integer DEFAULT 0 NOT NULL,
    prof_bonus integer DEFAULT 0 NOT NULL,
    url text NOT NULL,
    detail_id integer
);


ALTER TABLE public.levels OWNER TO postgres;

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
    description text,
    equipment_category integer,
    name character varying(255),
    rarity character varying(255),
    url character varying(255)
);


ALTER TABLE public.magic_items OWNER TO postgres;

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
    description text,
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
-- Name: monster_actions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_actions (
    id integer NOT NULL,
    monster_id integer,
    name character varying(255),
    description text,
    damage_type integer,
    damage_dice character varying(50)
);


ALTER TABLE public.monster_actions OWNER TO postgres;

--
-- Name: monster_actions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_actions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_actions_id_seq OWNER TO postgres;

--
-- Name: monster_actions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_actions_id_seq OWNED BY public.monster_actions.id;


--
-- Name: monster_condition_immunities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_condition_immunities (
    id integer NOT NULL,
    monster_id integer,
    condition_id integer
);


ALTER TABLE public.monster_condition_immunities OWNER TO postgres;

--
-- Name: monster_condition_immunities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_condition_immunities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_condition_immunities_id_seq OWNER TO postgres;

--
-- Name: monster_condition_immunities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_condition_immunities_id_seq OWNED BY public.monster_condition_immunities.id;


--
-- Name: monster_legendary_actions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_legendary_actions (
    id integer NOT NULL,
    monster_id integer,
    name character varying(255),
    description text,
    dc_type_id integer,
    dc_value integer,
    success_type character varying(50),
    damage_type_id integer,
    damage_dice character varying(50)
);


ALTER TABLE public.monster_legendary_actions OWNER TO postgres;

--
-- Name: monster_legendary_actions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_legendary_actions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_legendary_actions_id_seq OWNER TO postgres;

--
-- Name: monster_legendary_actions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_legendary_actions_id_seq OWNED BY public.monster_legendary_actions.id;


--
-- Name: monster_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_proficiencies (
    id integer NOT NULL,
    monster_id integer,
    proficiency_id integer,
    proficiency_value integer
);


ALTER TABLE public.monster_proficiencies OWNER TO postgres;

--
-- Name: monster_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_proficiencies_id_seq OWNER TO postgres;

--
-- Name: monster_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_proficiencies_id_seq OWNED BY public.monster_proficiencies.id;


--
-- Name: monster_reactions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_reactions (
    id integer NOT NULL,
    monster_id integer,
    name character varying(255),
    description text,
    attack_bonus integer,
    damage_type_id integer,
    damage_dice character varying(50),
    dc_type_id integer,
    dc_value integer,
    success_type character varying(50)
);


ALTER TABLE public.monster_reactions OWNER TO postgres;

--
-- Name: monster_reactions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_reactions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_reactions_id_seq OWNER TO postgres;

--
-- Name: monster_reactions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_reactions_id_seq OWNED BY public.monster_reactions.id;


--
-- Name: monster_spells; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monster_spells (
    id integer NOT NULL,
    monster_special_ability_id integer,
    spell_id integer
);


ALTER TABLE public.monster_spells OWNER TO postgres;

--
-- Name: monster_spells_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monster_spells_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monster_spells_id_seq OWNER TO postgres;

--
-- Name: monster_spells_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monster_spells_id_seq OWNED BY public.monster_spells.id;


--
-- Name: monsters; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters (
    id integer NOT NULL,
    name character varying(255),
    size character varying(50),
    type character varying(50),
    subtype character varying(100),
    alignment character varying(100),
    armor_class_type character varying(100),
    armor_class_value integer,
    hit_points integer,
    hit_dice character varying(50),
    xp integer,
    challenge_rating double precision,
    strength integer,
    dexterity integer,
    constitution integer,
    intelligence integer,
    wisdom integer,
    charisma integer,
    languages text,
    proficiency_bonus integer,
    senses text,
    speed text,
    proficiencies_id integer,
    condition_immunities_id integer,
    actions_id integer,
    legendary_actions_id integer,
    special_abilities_id integer,
    reactions_id integer,
    damage_vulnerabilities text,
    damage_resistances text,
    damage_immunities text
);


ALTER TABLE public.monsters OWNER TO postgres;

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
-- Name: monsters_special_abilities; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.monsters_special_abilities (
    id integer NOT NULL,
    monster_id integer,
    name character varying(255),
    description text,
    damage_type_id integer,
    damage_dice character varying(50),
    dc_type_id integer,
    dc_value integer,
    success_type character varying(50),
    spellcasting_level integer,
    spellcasting_ability_score_id integer,
    spellcasting_modifier integer,
    spellcasting_components_required text,
    spellcasting_school character varying(50),
    spellcasting_slots text
);


ALTER TABLE public.monsters_special_abilities OWNER TO postgres;

--
-- Name: monsters_special_abilities_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.monsters_special_abilities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.monsters_special_abilities_id_seq OWNER TO postgres;

--
-- Name: monsters_special_abilities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.monsters_special_abilities_id_seq OWNED BY public.monsters_special_abilities.id;


--
-- Name: prerequisites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.prerequisites (
    id integer NOT NULL,
    prerequisites_id integer,
    spell_id integer,
    feature_id integer
);


ALTER TABLE public.prerequisites OWNER TO postgres;

--
-- Name: prerequisites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.prerequisites ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.prerequisites_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.proficiencies (
    id integer NOT NULL,
    name character varying(255),
    type character varying(255),
    url character varying(255),
    reference_equipment_id integer,
    reference_equipment_category_id integer,
    reference_skill_id integer,
    reference_ability_score_id integer
);


ALTER TABLE public.proficiencies OWNER TO postgres;

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
-- Name: race_ability_bonus_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_ability_bonus_options (
    id integer NOT NULL,
    race_id integer NOT NULL,
    ability_score_id integer NOT NULL
);


ALTER TABLE public.race_ability_bonus_options OWNER TO postgres;

--
-- Name: race_ability_bonus_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_ability_bonus_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_ability_bonus_options_id_seq OWNER TO postgres;

--
-- Name: race_ability_bonus_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_ability_bonus_options_id_seq OWNED BY public.race_ability_bonus_options.id;


--
-- Name: race_language_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_language_options (
    id integer NOT NULL,
    race_id integer NOT NULL,
    language_id integer NOT NULL
);


ALTER TABLE public.race_language_options OWNER TO postgres;

--
-- Name: race_language_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_language_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_language_options_id_seq OWNER TO postgres;

--
-- Name: race_language_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_language_options_id_seq OWNED BY public.race_language_options.id;


--
-- Name: race_languages; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_languages (
    id integer NOT NULL,
    race_id integer NOT NULL,
    language_id integer NOT NULL
);


ALTER TABLE public.race_languages OWNER TO postgres;

--
-- Name: race_languages_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_languages_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_languages_id_seq OWNER TO postgres;

--
-- Name: race_languages_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_languages_id_seq OWNED BY public.race_languages.id;


--
-- Name: race_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_proficiencies (
    id integer NOT NULL,
    race_id integer NOT NULL,
    proficiency_id integer NOT NULL
);


ALTER TABLE public.race_proficiencies OWNER TO postgres;

--
-- Name: race_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_proficiencies_id_seq OWNER TO postgres;

--
-- Name: race_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_proficiencies_id_seq OWNED BY public.race_proficiencies.id;


--
-- Name: race_proficiency_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_proficiency_options (
    id integer NOT NULL,
    race_id integer NOT NULL,
    proficiency_id integer NOT NULL
);


ALTER TABLE public.race_proficiency_options OWNER TO postgres;

--
-- Name: race_proficiency_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_proficiency_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_proficiency_options_id_seq OWNER TO postgres;

--
-- Name: race_proficiency_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_proficiency_options_id_seq OWNED BY public.race_proficiency_options.id;


--
-- Name: race_subraces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_subraces (
    id integer NOT NULL,
    race_id integer NOT NULL,
    subrace_id integer NOT NULL
);


ALTER TABLE public.race_subraces OWNER TO postgres;

--
-- Name: race_subraces_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_subraces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_subraces_id_seq OWNER TO postgres;

--
-- Name: race_subraces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_subraces_id_seq OWNED BY public.race_subraces.id;


--
-- Name: race_traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.race_traits (
    id integer NOT NULL,
    race_id integer NOT NULL,
    trait_id integer NOT NULL
);


ALTER TABLE public.race_traits OWNER TO postgres;

--
-- Name: race_traits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.race_traits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.race_traits_id_seq OWNER TO postgres;

--
-- Name: race_traits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.race_traits_id_seq OWNED BY public.race_traits.id;


--
-- Name: races; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.races (
    id integer NOT NULL,
    alignment text,
    age text,
    language_desc text,
    name character varying(255),
    size character varying(255),
    size_description text,
    speed integer,
    url character varying(255),
    ability_bonus integer,
    ability_score_id integer,
    ability_bonus_choose integer,
    ability_bonus_option_id integer,
    starting_proficiency_id integer,
    starting_proficiency_option_id integer,
    language_id integer,
    subrace_id integer,
    trait_id integer
);


ALTER TABLE public.races OWNER TO postgres;

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
-- Name: rule_sections; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rule_sections (
    id integer NOT NULL,
    name character varying(255),
    url character varying(255),
    description text
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
    description text,
    name character varying(255),
    subsections integer,
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
    description text,
    name character varying(255),
    ability_score integer,
    url character varying(255)
);


ALTER TABLE public.skills OWNER TO postgres;

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
    attack_type character varying(255),
    casting_time character varying(255),
    components text,
    concentration boolean,
    description text,
    duration character varying(255),
    higher_level text,
    level integer,
    material text,
    name character varying(255),
    range character varying(255),
    ritual boolean,
    saving_throw character varying(255),
    url character varying(255),
    area_of_effect_size integer,
    classes_id integer,
    subclasses_id integer,
    school_id integer,
    dc_id integer,
    damage_type_id integer,
    damage_at_slot_level text,
    heal_at_slot_level text,
    area_of_effect_type character varying(255)
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
-- Name: spells_subclasses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.spells_subclasses (
    id integer NOT NULL,
    spells_id integer,
    subclasses_id integer,
    required_level_id integer,
    required_feature_id integer
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
-- Name: subclasses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subclasses (
    id integer NOT NULL,
    class_id integer,
    name character varying(255),
    spells_id integer,
    url character varying(255),
    description text,
    subclass_flavor character varying(255)
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
-- Name: subfeatures; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subfeatures (
    id integer NOT NULL,
    subfeature_id integer,
    feature_id integer
);


ALTER TABLE public.subfeatures OWNER TO postgres;

--
-- Name: subfeatures_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.subfeatures ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.subfeatures_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: subrace_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subrace_proficiencies (
    id integer NOT NULL,
    subrace_id integer NOT NULL,
    proficiency_id integer NOT NULL
);


ALTER TABLE public.subrace_proficiencies OWNER TO postgres;

--
-- Name: subrace_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subrace_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subrace_proficiencies_id_seq OWNER TO postgres;

--
-- Name: subrace_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subrace_proficiencies_id_seq OWNED BY public.subrace_proficiencies.id;


--
-- Name: subrace_traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subrace_traits (
    id integer NOT NULL,
    subrace_id integer NOT NULL,
    trait_id integer NOT NULL
);


ALTER TABLE public.subrace_traits OWNER TO postgres;

--
-- Name: subrace_traits_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.subrace_traits_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.subrace_traits_id_seq OWNER TO postgres;

--
-- Name: subrace_traits_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.subrace_traits_id_seq OWNED BY public.subrace_traits.id;


--
-- Name: subraces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subraces (
    id integer NOT NULL,
    name character varying(255),
    url character varying(255),
    description text,
    race_id integer,
    ability_score_id integer,
    languages text[],
    proficiency_id integer,
    trait_id integer
);


ALTER TABLE public.subraces OWNER TO postgres;

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
-- Name: trait_options; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trait_options (
    id integer NOT NULL,
    choose integer,
    type character varying(50),
    option_id integer,
    subtrait_id integer,
    spell_id integer,
    proficiency_id integer
);


ALTER TABLE public.trait_options OWNER TO postgres;

--
-- Name: trait_options_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.trait_options_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.trait_options_id_seq OWNER TO postgres;

--
-- Name: trait_options_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.trait_options_id_seq OWNED BY public.trait_options.id;


--
-- Name: traits; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.traits (
    id integer NOT NULL,
    description text,
    name character varying(255),
    proficiencies integer,
    races integer,
    subrace_id integer,
    url character varying(255),
    parent integer,
    extra_language integer,
    trait_proficiency_id integer
);


ALTER TABLE public.traits OWNER TO postgres;

--
-- Name: COLUMN traits.proficiencies; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.traits.proficiencies IS 'trait_proficiencies table identity';


--
-- Name: COLUMN traits.races; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.traits.races IS 'trait_races table identity';


--
-- Name: COLUMN traits.trait_proficiency_id; Type: COMMENT; Schema: public; Owner: postgres
--

COMMENT ON COLUMN public.traits.trait_proficiency_id IS 'traits_options table identity';


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
-- Name: traits_proficiencies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.traits_proficiencies (
    id integer NOT NULL,
    trait_id integer,
    proficiency_id integer
);


ALTER TABLE public.traits_proficiencies OWNER TO postgres;

--
-- Name: traits_proficiencies_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.traits_proficiencies_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.traits_proficiencies_id_seq OWNER TO postgres;

--
-- Name: traits_proficiencies_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.traits_proficiencies_id_seq OWNED BY public.traits_proficiencies.id;


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
    description text,
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
-- Name: alignments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alignments ALTER COLUMN id SET DEFAULT nextval('public.alignments_id_seq'::regclass);


--
-- Name: class_multi_classing_prerequisites id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_prerequisites ALTER COLUMN id SET DEFAULT nextval('public.class_multi_classing_prerequisites_id_seq'::regclass);


--
-- Name: class_multi_classing_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.class_multi_classing_proficiencies_id_seq'::regclass);


--
-- Name: classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes ALTER COLUMN id SET DEFAULT nextval('public.classes_id_seq'::regclass);


--
-- Name: classes_levels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_levels ALTER COLUMN id SET DEFAULT nextval('public.classes_levels_id_seq'::regclass);


--
-- Name: classes_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.classes_proficiencies_id_seq'::regclass);


--
-- Name: classes_proficiency_choices id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiency_choices ALTER COLUMN id SET DEFAULT nextval('public.classes_proficiency_choices_id_seq'::regclass);


--
-- Name: classes_saving_throws id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws ALTER COLUMN id SET DEFAULT nextval('public.classes_saving_throws_id_seq'::regclass);


--
-- Name: classes_starting_equipment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment ALTER COLUMN id SET DEFAULT nextval('public.classes_starting_equipment_id_seq'::regclass);


--
-- Name: classes_starting_equipment_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options ALTER COLUMN id SET DEFAULT nextval('public.classes_starting_equipment_options_id_seq'::regclass);


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
-- Name: equipment_properties id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties ALTER COLUMN id SET DEFAULT nextval('public.equipment_properties_id_seq'::regclass);


--
-- Name: feats id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats ALTER COLUMN id SET DEFAULT nextval('public.feats_id_seq'::regclass);


--
-- Name: features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features ALTER COLUMN id SET DEFAULT nextval('public.features_id_seq'::regclass);


--
-- Name: languages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.languages ALTER COLUMN id SET DEFAULT nextval('public.languages_id_seq'::regclass);


--
-- Name: level_detail id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail ALTER COLUMN id SET DEFAULT nextval('public.level_detail_id_seq'::regclass);


--
-- Name: level_detail_features id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail_features ALTER COLUMN id SET DEFAULT nextval('public.level_detail_features_id_seq'::regclass);


--
-- Name: levels id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels ALTER COLUMN id SET DEFAULT nextval('public.levels_id_seq'::regclass);


--
-- Name: magic_items id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items ALTER COLUMN id SET DEFAULT nextval('public.magic_items_id_seq'::regclass);


--
-- Name: magic_schools id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_schools ALTER COLUMN id SET DEFAULT nextval('public.magic_schools_id_seq'::regclass);


--
-- Name: monster_actions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_actions ALTER COLUMN id SET DEFAULT nextval('public.monster_actions_id_seq'::regclass);


--
-- Name: monster_condition_immunities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_condition_immunities ALTER COLUMN id SET DEFAULT nextval('public.monster_condition_immunities_id_seq'::regclass);


--
-- Name: monster_legendary_actions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_legendary_actions ALTER COLUMN id SET DEFAULT nextval('public.monster_legendary_actions_id_seq'::regclass);


--
-- Name: monster_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.monster_proficiencies_id_seq'::regclass);


--
-- Name: monster_reactions id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_reactions ALTER COLUMN id SET DEFAULT nextval('public.monster_reactions_id_seq'::regclass);


--
-- Name: monster_spells id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_spells ALTER COLUMN id SET DEFAULT nextval('public.monster_spells_id_seq'::regclass);


--
-- Name: monsters id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters ALTER COLUMN id SET DEFAULT nextval('public.monsters_id_seq'::regclass);


--
-- Name: monsters_special_abilities id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities ALTER COLUMN id SET DEFAULT nextval('public.monsters_special_abilities_id_seq'::regclass);


--
-- Name: proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies ALTER COLUMN id SET DEFAULT nextval('public.proficiencies_id_seq'::regclass);


--
-- Name: race_ability_bonus_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_ability_bonus_options ALTER COLUMN id SET DEFAULT nextval('public.race_ability_bonus_options_id_seq'::regclass);


--
-- Name: race_language_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_language_options ALTER COLUMN id SET DEFAULT nextval('public.race_language_options_id_seq'::regclass);


--
-- Name: race_languages id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_languages ALTER COLUMN id SET DEFAULT nextval('public.race_languages_id_seq'::regclass);


--
-- Name: race_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.race_proficiencies_id_seq'::regclass);


--
-- Name: race_proficiency_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiency_options ALTER COLUMN id SET DEFAULT nextval('public.race_proficiency_options_id_seq'::regclass);


--
-- Name: race_subraces id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_subraces ALTER COLUMN id SET DEFAULT nextval('public.race_subraces_id_seq'::regclass);


--
-- Name: race_traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_traits ALTER COLUMN id SET DEFAULT nextval('public.race_traits_id_seq'::regclass);


--
-- Name: races id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races ALTER COLUMN id SET DEFAULT nextval('public.races_id_seq'::regclass);


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
-- Name: spells id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells ALTER COLUMN id SET DEFAULT nextval('public.spells_id_seq'::regclass);


--
-- Name: spells_classes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes ALTER COLUMN id SET DEFAULT nextval('public.spells_classes_id_seq'::regclass);


--
-- Name: spells_subclasses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses ALTER COLUMN id SET DEFAULT nextval('public.spells_subclasses_id_seq'::regclass);


--
-- Name: subclasses id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses ALTER COLUMN id SET DEFAULT nextval('public.subclasses_id_seq'::regclass);


--
-- Name: subclasses_class id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class ALTER COLUMN id SET DEFAULT nextval('public.subclasses_class_id_seq'::regclass);


--
-- Name: subrace_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.subrace_proficiencies_id_seq'::regclass);


--
-- Name: subrace_traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_traits ALTER COLUMN id SET DEFAULT nextval('public.subrace_traits_id_seq'::regclass);


--
-- Name: subraces id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces ALTER COLUMN id SET DEFAULT nextval('public.subraces_id_seq'::regclass);


--
-- Name: trait_options id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options ALTER COLUMN id SET DEFAULT nextval('public.trait_options_id_seq'::regclass);


--
-- Name: traits id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits ALTER COLUMN id SET DEFAULT nextval('public.traits_id_seq'::regclass);


--
-- Name: traits_proficiencies id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_proficiencies ALTER COLUMN id SET DEFAULT nextval('public.traits_proficiencies_id_seq'::regclass);


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
-- Name: alignments alignments_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alignments
    ADD CONSTRAINT alignments_pkey PRIMARY KEY (id);


--
-- Name: class_multi_classing_prerequisites class_multi_classing_prerequisites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_prerequisites
    ADD CONSTRAINT class_multi_classing_prerequisites_pkey PRIMARY KEY (id);


--
-- Name: class_multi_classing_proficiencies class_multi_classing_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_proficiencies
    ADD CONSTRAINT class_multi_classing_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: classes_levels classes_levels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_levels
    ADD CONSTRAINT classes_levels_pkey PRIMARY KEY (id);


--
-- Name: classes classes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_pkey PRIMARY KEY (id);


--
-- Name: classes_proficiencies classes_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: classes_proficiency_choices classes_proficiency_choices_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiency_choices
    ADD CONSTRAINT classes_proficiency_choices_pkey PRIMARY KEY (id);


--
-- Name: classes_saving_throws classes_saving_throws_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_pkey PRIMARY KEY (id);


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
-- Name: equipment_categories equipment_categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_categories
    ADD CONSTRAINT equipment_categories_pkey PRIMARY KEY (id);


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
-- Name: feats feats_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats
    ADD CONSTRAINT feats_pkey PRIMARY KEY (id);


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
-- Name: level_detail level_detail_features_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail
    ADD CONSTRAINT level_detail_features_id_key UNIQUE (features_id);


--
-- Name: level_detail_features level_detail_features_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail_features
    ADD CONSTRAINT level_detail_features_pkey PRIMARY KEY (id);


--
-- Name: level_detail level_detail_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail
    ADD CONSTRAINT level_detail_pkey PRIMARY KEY (id);


--
-- Name: levels levels_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_pkey PRIMARY KEY (id);


--
-- Name: levels levels_url_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_url_key UNIQUE (url);


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
-- Name: monster_actions monster_actions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_actions
    ADD CONSTRAINT monster_actions_pkey PRIMARY KEY (id);


--
-- Name: monster_condition_immunities monster_condition_immunities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_condition_immunities
    ADD CONSTRAINT monster_condition_immunities_pkey PRIMARY KEY (id);


--
-- Name: monster_legendary_actions monster_legendary_actions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_legendary_actions
    ADD CONSTRAINT monster_legendary_actions_pkey PRIMARY KEY (id);


--
-- Name: monster_proficiencies monster_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_proficiencies
    ADD CONSTRAINT monster_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: monster_reactions monster_reactions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_reactions
    ADD CONSTRAINT monster_reactions_pkey PRIMARY KEY (id);


--
-- Name: monster_spells monster_spells_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_spells
    ADD CONSTRAINT monster_spells_pkey PRIMARY KEY (id);


--
-- Name: monsters monsters_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters
    ADD CONSTRAINT monsters_pkey PRIMARY KEY (id);


--
-- Name: monsters_special_abilities monsters_special_abilities_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities
    ADD CONSTRAINT monsters_special_abilities_pkey PRIMARY KEY (id);


--
-- Name: prerequisites prerequisites_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerequisites
    ADD CONSTRAINT prerequisites_pkey PRIMARY KEY (id);


--
-- Name: proficiencies proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT proficiencies_pkey PRIMARY KEY (id);


--
-- Name: race_ability_bonus_options race_ability_bonus_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_ability_bonus_options
    ADD CONSTRAINT race_ability_bonus_options_pkey PRIMARY KEY (id);


--
-- Name: race_language_options race_language_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_language_options
    ADD CONSTRAINT race_language_options_pkey PRIMARY KEY (id);


--
-- Name: race_languages race_languages_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_languages
    ADD CONSTRAINT race_languages_pkey PRIMARY KEY (id);


--
-- Name: race_proficiencies race_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiencies
    ADD CONSTRAINT race_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: race_proficiency_options race_proficiency_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiency_options
    ADD CONSTRAINT race_proficiency_options_pkey PRIMARY KEY (id);


--
-- Name: race_subraces race_subraces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_subraces
    ADD CONSTRAINT race_subraces_pkey PRIMARY KEY (id);


--
-- Name: race_traits race_traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_traits
    ADD CONSTRAINT race_traits_pkey PRIMARY KEY (id);


--
-- Name: races races_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT races_pkey PRIMARY KEY (id);


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
-- Name: spells spells_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT spells_pkey PRIMARY KEY (id);


--
-- Name: spells_subclasses spells_subclasses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_pkey PRIMARY KEY (id);


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
-- Name: subrace_proficiencies subrace_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_proficiencies
    ADD CONSTRAINT subrace_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: subrace_traits subrace_traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_traits
    ADD CONSTRAINT subrace_traits_pkey PRIMARY KEY (id);


--
-- Name: subraces subraces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces
    ADD CONSTRAINT subraces_pkey PRIMARY KEY (id);


--
-- Name: trait_options trait_options_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options
    ADD CONSTRAINT trait_options_pkey PRIMARY KEY (id);


--
-- Name: traits traits_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT traits_pkey PRIMARY KEY (id);


--
-- Name: traits_proficiencies traits_proficiencies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_proficiencies
    ADD CONSTRAINT traits_proficiencies_pkey PRIMARY KEY (id);


--
-- Name: traits_races traits_races_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_races
    ADD CONSTRAINT traits_races_pkey PRIMARY KEY (id);


--
-- Name: spells unique_classes_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT unique_classes_id UNIQUE (classes_id);


--
-- Name: feature_specific unique_expertise_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT unique_expertise_id UNIQUE (expertise_id);


--
-- Name: feature_specific unique_feature_specific_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT unique_feature_specific_id UNIQUE (feature_specific_id);


--
-- Name: features unique_feature_spesific_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT unique_feature_spesific_id UNIQUE (feature_spesific_id);


--
-- Name: feature_specific unique_invocation_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT unique_invocation_id UNIQUE (invocation_id);


--
-- Name: feature_specific unique_invocation_id_feature_specific; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT unique_invocation_id_feature_specific UNIQUE (invocation_id);


--
-- Name: features unique_prerequisites_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT unique_prerequisites_id UNIQUE (prerequisites_id);


--
-- Name: prerequisites unique_prerequisites_prereq_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerequisites
    ADD CONSTRAINT unique_prerequisites_prereq_id UNIQUE (prerequisites_id);


--
-- Name: equipment unique_properties; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT unique_properties UNIQUE (properties);


--
-- Name: spells unique_subclasses_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT unique_subclasses_id UNIQUE (subclasses_id);


--
-- Name: feature_specific unique_subfeature_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT unique_subfeature_id UNIQUE (subfeature_id);


--
-- Name: rules unique_subsections; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules
    ADD CONSTRAINT unique_subsections UNIQUE (subsections);


--
-- Name: traits unique_trait_proficiency_id; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT unique_trait_proficiency_id UNIQUE (trait_proficiency_id);


--
-- Name: weapon_properties weapon_properties_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.weapon_properties
    ADD CONSTRAINT weapon_properties_pkey PRIMARY KEY (id);


--
-- Name: rules set_subsections_equal_id; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER set_subsections_equal_id BEFORE INSERT ON public.rules FOR EACH ROW EXECUTE FUNCTION public.sync_subsections();


--
-- Name: levels trg_set_detail_id; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_set_detail_id AFTER INSERT ON public.levels FOR EACH ROW EXECUTE FUNCTION public.set_detail_id_to_self();


--
-- Name: equipment trg_sync_properties; Type: TRIGGER; Schema: public; Owner: postgres
--

CREATE TRIGGER trg_sync_properties BEFORE INSERT OR UPDATE ON public.equipment FOR EACH ROW EXECUTE FUNCTION public.sync_properties_with_id();


--
-- Name: class_multi_classing_prerequisites class_multi_classing_prerequisites_ability_score_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_prerequisites
    ADD CONSTRAINT class_multi_classing_prerequisites_ability_score_id_fkey FOREIGN KEY (ability_score_id) REFERENCES public.ability_scores(id) ON DELETE CASCADE;


--
-- Name: class_multi_classing_prerequisites class_multi_classing_prerequisites_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_prerequisites
    ADD CONSTRAINT class_multi_classing_prerequisites_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: class_multi_classing_proficiencies class_multi_classing_proficiencies_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_proficiencies
    ADD CONSTRAINT class_multi_classing_proficiencies_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: class_multi_classing_proficiencies class_multi_classing_proficiencies_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.class_multi_classing_proficiencies
    ADD CONSTRAINT class_multi_classing_proficiencies_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: classes_levels classes_levels_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_levels
    ADD CONSTRAINT classes_levels_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_levels classes_levels_level_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_levels
    ADD CONSTRAINT classes_levels_level_id_fkey FOREIGN KEY (level_id) REFERENCES public.levels(id) ON DELETE CASCADE;


--
-- Name: classes_proficiencies classes_proficiencies_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_proficiencies classes_proficiencies_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiencies
    ADD CONSTRAINT classes_proficiencies_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: classes_proficiency_choices classes_proficiency_choices_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiency_choices
    ADD CONSTRAINT classes_proficiency_choices_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_proficiency_choices classes_proficiency_choices_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_proficiency_choices
    ADD CONSTRAINT classes_proficiency_choices_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: classes_saving_throws classes_saving_throws_ability_score_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_ability_score_id_fkey FOREIGN KEY (ability_score_id) REFERENCES public.ability_scores(id) ON DELETE CASCADE;


--
-- Name: classes_saving_throws classes_saving_throws_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_saving_throws
    ADD CONSTRAINT classes_saving_throws_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_starting_equipment classes_starting_equipment_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment
    ADD CONSTRAINT classes_starting_equipment_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_starting_equipment classes_starting_equipment_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment
    ADD CONSTRAINT classes_starting_equipment_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id) ON DELETE CASCADE;


--
-- Name: classes_starting_equipment_options classes_starting_equipment_options_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options
    ADD CONSTRAINT classes_starting_equipment_options_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: classes_starting_equipment_options classes_starting_equipment_options_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes_starting_equipment_options
    ADD CONSTRAINT classes_starting_equipment_options_equipment_id_fkey FOREIGN KEY (equipment_id) REFERENCES public.equipment(id) ON DELETE CASCADE;


--
-- Name: classes classes_subclass_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.classes
    ADD CONSTRAINT classes_subclass_id_fkey FOREIGN KEY (subclass_id) REFERENCES public.subclasses(id) ON DELETE SET NULL;


--
-- Name: equipment_properties equipment_properties_equipment_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT equipment_properties_equipment_id_fkey FOREIGN KEY (equipment_property_key) REFERENCES public.equipment(id);


--
-- Name: equipment_properties equipment_properties_weapon_properties_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT equipment_properties_weapon_properties_id_fkey FOREIGN KEY (weapon_properties_id) REFERENCES public.weapon_properties(id);


--
-- Name: skills fk_ability_score; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.skills
    ADD CONSTRAINT fk_ability_score FOREIGN KEY (ability_score) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: magic_items fk_equipment_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.magic_items
    ADD CONSTRAINT fk_equipment_category FOREIGN KEY (equipment_category) REFERENCES public.equipment_categories(id);


--
-- Name: equipment fk_equipment_damage_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT fk_equipment_damage_type FOREIGN KEY (damage_type) REFERENCES public.damage_types(id);


--
-- Name: equipment fk_equipment_equipment_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT fk_equipment_equipment_category FOREIGN KEY (equipment_category) REFERENCES public.equipment_categories(id);


--
-- Name: equipment fk_equipment_gear_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT fk_equipment_gear_category FOREIGN KEY (gear_category) REFERENCES public.equipment_categories(id);


--
-- Name: equipment_properties fk_equipment_properties_custom; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment_properties
    ADD CONSTRAINT fk_equipment_properties_custom FOREIGN KEY (equipment_property_key) REFERENCES public.equipment(properties);


--
-- Name: equipment fk_equipment_two_handed_damage_type; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.equipment
    ADD CONSTRAINT fk_equipment_two_handed_damage_type FOREIGN KEY (two_handed_damage_type) REFERENCES public.damage_types(id);


--
-- Name: expertises fk_expertises_feature_specific; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.expertises
    ADD CONSTRAINT fk_expertises_feature_specific FOREIGN KEY (expertise_id) REFERENCES public.feature_specific(expertise_id) ON DELETE CASCADE;


--
-- Name: expertises fk_expertises_proficiency; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.expertises
    ADD CONSTRAINT fk_expertises_proficiency FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: feats fk_feats_ability_score; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feats
    ADD CONSTRAINT fk_feats_ability_score FOREIGN KEY (ability_score) REFERENCES public.ability_scores(id);


--
-- Name: features fk_feature_class; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_feature_class FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE SET NULL;


--
-- Name: features fk_feature_parent; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_feature_parent FOREIGN KEY (parent_id) REFERENCES public.features(id) ON DELETE SET NULL;


--
-- Name: feature_specific fk_feature_specific_to_features; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.feature_specific
    ADD CONSTRAINT fk_feature_specific_to_features FOREIGN KEY (feature_specific_id) REFERENCES public.features(feature_spesific_id) ON DELETE CASCADE;


--
-- Name: features fk_feature_subclass; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_feature_subclass FOREIGN KEY (subclass_id) REFERENCES public.subclasses(id) ON DELETE SET NULL;


--
-- Name: features fk_features_to_feature_specific; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_features_to_feature_specific FOREIGN KEY (feature_spesific_id) REFERENCES public.feature_specific(feature_specific_id) ON DELETE SET NULL;


--
-- Name: features fk_features_to_prerequisites_prereq_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.features
    ADD CONSTRAINT fk_features_to_prerequisites_prereq_id FOREIGN KEY (prerequisites_id) REFERENCES public.prerequisites(prerequisites_id) ON DELETE SET NULL;


--
-- Name: invocations fk_invocation_feature; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invocations
    ADD CONSTRAINT fk_invocation_feature FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: invocations fk_invocation_feature_specific; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.invocations
    ADD CONSTRAINT fk_invocation_feature_specific FOREIGN KEY (invocation_id) REFERENCES public.feature_specific(invocation_id);


--
-- Name: levels fk_levels_detail; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT fk_levels_detail FOREIGN KEY (detail_id) REFERENCES public.level_detail(id) ON DELETE CASCADE;


--
-- Name: monster_proficiencies fk_monster_proficiencies_to_monsters; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_proficiencies
    ADD CONSTRAINT fk_monster_proficiencies_to_monsters FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: prerequisites fk_prereq_to_features_id; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerequisites
    ADD CONSTRAINT fk_prereq_to_features_id FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: prerequisites fk_prereq_to_features_reqid; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerequisites
    ADD CONSTRAINT fk_prereq_to_features_reqid FOREIGN KEY (prerequisites_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: prerequisites fk_prereq_to_spells; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.prerequisites
    ADD CONSTRAINT fk_prereq_to_spells FOREIGN KEY (spell_id) REFERENCES public.spells(id) ON DELETE CASCADE;


--
-- Name: proficiencies fk_proficiencies_ability_score; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT fk_proficiencies_ability_score FOREIGN KEY (reference_ability_score_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: proficiencies fk_proficiencies_equipment; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT fk_proficiencies_equipment FOREIGN KEY (reference_equipment_id) REFERENCES public.equipment(id) ON DELETE SET NULL;


--
-- Name: proficiencies fk_proficiencies_equipment_category; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT fk_proficiencies_equipment_category FOREIGN KEY (reference_equipment_category_id) REFERENCES public.equipment_categories(id) ON DELETE SET NULL;


--
-- Name: proficiencies fk_proficiencies_skill; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.proficiencies
    ADD CONSTRAINT fk_proficiencies_skill FOREIGN KEY (reference_skill_id) REFERENCES public.skills(id) ON DELETE SET NULL;


--
-- Name: race_ability_bonus_options fk_rabo_ability; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_ability_bonus_options
    ADD CONSTRAINT fk_rabo_ability FOREIGN KEY (ability_score_id) REFERENCES public.ability_scores(id) ON DELETE CASCADE;


--
-- Name: race_ability_bonus_options fk_rabo_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_ability_bonus_options
    ADD CONSTRAINT fk_rabo_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: races fk_races_to_ability_scores; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT fk_races_to_ability_scores FOREIGN KEY (ability_score_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: races fk_races_to_subraces; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.races
    ADD CONSTRAINT fk_races_to_subraces FOREIGN KEY (subrace_id) REFERENCES public.subraces(id) ON DELETE SET NULL;


--
-- Name: race_languages fk_rl_lang; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_languages
    ADD CONSTRAINT fk_rl_lang FOREIGN KEY (language_id) REFERENCES public.languages(id) ON DELETE CASCADE;


--
-- Name: race_languages fk_rl_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_languages
    ADD CONSTRAINT fk_rl_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_language_options fk_rlo_lang; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_language_options
    ADD CONSTRAINT fk_rlo_lang FOREIGN KEY (language_id) REFERENCES public.languages(id) ON DELETE CASCADE;


--
-- Name: race_language_options fk_rlo_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_language_options
    ADD CONSTRAINT fk_rlo_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_proficiencies fk_rp_proficiency; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiencies
    ADD CONSTRAINT fk_rp_proficiency FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: race_proficiencies fk_rp_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiencies
    ADD CONSTRAINT fk_rp_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_proficiency_options fk_rpo_proficiency; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiency_options
    ADD CONSTRAINT fk_rpo_proficiency FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: race_proficiency_options fk_rpo_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_proficiency_options
    ADD CONSTRAINT fk_rpo_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_subraces fk_rs_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_subraces
    ADD CONSTRAINT fk_rs_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_subraces fk_rs_subrace; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_subraces
    ADD CONSTRAINT fk_rs_subrace FOREIGN KEY (subrace_id) REFERENCES public.subraces(id) ON DELETE CASCADE;


--
-- Name: race_traits fk_rt_race; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_traits
    ADD CONSTRAINT fk_rt_race FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE CASCADE;


--
-- Name: race_traits fk_rt_trait; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.race_traits
    ADD CONSTRAINT fk_rt_trait FOREIGN KEY (trait_id) REFERENCES public.traits(id) ON DELETE CASCADE;


--
-- Name: rules_subsections fk_rules_subsections_subsections; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections
    ADD CONSTRAINT fk_rules_subsections_subsections FOREIGN KEY (rules_id) REFERENCES public.rules(subsections) ON DELETE CASCADE;


--
-- Name: subfeatures fk_subfeatures_feature; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subfeatures
    ADD CONSTRAINT fk_subfeatures_feature FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: subfeatures fk_subfeatures_feature_specific; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subfeatures
    ADD CONSTRAINT fk_subfeatures_feature_specific FOREIGN KEY (subfeature_id) REFERENCES public.feature_specific(subfeature_id) ON DELETE CASCADE;


--
-- Name: subrace_proficiencies fk_subrace_proficiencies_to_proficiencies; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_proficiencies
    ADD CONSTRAINT fk_subrace_proficiencies_to_proficiencies FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: subrace_proficiencies fk_subrace_proficiencies_to_subraces; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_proficiencies
    ADD CONSTRAINT fk_subrace_proficiencies_to_subraces FOREIGN KEY (subrace_id) REFERENCES public.subraces(id) ON DELETE CASCADE;


--
-- Name: subrace_traits fk_subrace_traits_to_subraces; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_traits
    ADD CONSTRAINT fk_subrace_traits_to_subraces FOREIGN KEY (subrace_id) REFERENCES public.subraces(id) ON DELETE CASCADE;


--
-- Name: subrace_traits fk_subrace_traits_to_traits; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subrace_traits
    ADD CONSTRAINT fk_subrace_traits_to_traits FOREIGN KEY (trait_id) REFERENCES public.traits(id) ON DELETE CASCADE;


--
-- Name: subraces fk_subraces_to_ability_scores; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces
    ADD CONSTRAINT fk_subraces_to_ability_scores FOREIGN KEY (ability_score_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: subraces fk_subraces_to_races; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subraces
    ADD CONSTRAINT fk_subraces_to_races FOREIGN KEY (race_id) REFERENCES public.races(id) ON DELETE SET NULL;


--
-- Name: traits fk_traits_parent; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT fk_traits_parent FOREIGN KEY (parent) REFERENCES public.traits(id) ON DELETE SET NULL;


--
-- Name: traits fk_traits_proficiency; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT fk_traits_proficiency FOREIGN KEY (proficiencies) REFERENCES public.proficiencies(id) ON DELETE SET NULL;


--
-- Name: traits fk_traits_subrace; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits
    ADD CONSTRAINT fk_traits_subrace FOREIGN KEY (subrace_id) REFERENCES public.subraces(id) ON DELETE SET NULL;


--
-- Name: level_detail_features level_detail_features_feature_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail_features
    ADD CONSTRAINT level_detail_features_feature_id_fkey FOREIGN KEY (feature_id) REFERENCES public.features(id) ON DELETE CASCADE;


--
-- Name: level_detail_features level_detail_features_level_detail_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.level_detail_features
    ADD CONSTRAINT level_detail_features_level_detail_id_fkey FOREIGN KEY (level_detail_id) REFERENCES public.level_detail(features_id) ON DELETE CASCADE;


--
-- Name: levels levels_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE CASCADE;


--
-- Name: levels levels_subclass_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.levels
    ADD CONSTRAINT levels_subclass_id_fkey FOREIGN KEY (subclass_id) REFERENCES public.subclasses(id) ON DELETE SET NULL;


--
-- Name: monster_actions monster_actions_damage_type_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_actions
    ADD CONSTRAINT monster_actions_damage_type_fkey FOREIGN KEY (damage_type) REFERENCES public.damage_types(id) ON DELETE SET NULL;


--
-- Name: monster_actions monster_actions_monster_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_actions
    ADD CONSTRAINT monster_actions_monster_id_fkey FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: monster_condition_immunities monster_condition_immunities_condition_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_condition_immunities
    ADD CONSTRAINT monster_condition_immunities_condition_id_fkey FOREIGN KEY (condition_id) REFERENCES public.conditions(id) ON DELETE SET NULL;


--
-- Name: monster_condition_immunities monster_condition_immunities_monster_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_condition_immunities
    ADD CONSTRAINT monster_condition_immunities_monster_id_fkey FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: monster_legendary_actions monster_legendary_actions_damage_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_legendary_actions
    ADD CONSTRAINT monster_legendary_actions_damage_type_id_fkey FOREIGN KEY (damage_type_id) REFERENCES public.damage_types(id) ON DELETE SET NULL;


--
-- Name: monster_legendary_actions monster_legendary_actions_dc_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_legendary_actions
    ADD CONSTRAINT monster_legendary_actions_dc_type_id_fkey FOREIGN KEY (dc_type_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: monster_legendary_actions monster_legendary_actions_monster_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_legendary_actions
    ADD CONSTRAINT monster_legendary_actions_monster_id_fkey FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: monster_proficiencies monster_proficiencies_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_proficiencies
    ADD CONSTRAINT monster_proficiencies_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE SET NULL;


--
-- Name: monster_reactions monster_reactions_damage_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_reactions
    ADD CONSTRAINT monster_reactions_damage_type_id_fkey FOREIGN KEY (damage_type_id) REFERENCES public.damage_types(id) ON DELETE SET NULL;


--
-- Name: monster_reactions monster_reactions_dc_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_reactions
    ADD CONSTRAINT monster_reactions_dc_type_id_fkey FOREIGN KEY (dc_type_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: monster_reactions monster_reactions_monster_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_reactions
    ADD CONSTRAINT monster_reactions_monster_id_fkey FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: monster_spells monster_spells_monster_special_ability_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_spells
    ADD CONSTRAINT monster_spells_monster_special_ability_id_fkey FOREIGN KEY (monster_special_ability_id) REFERENCES public.monsters_special_abilities(id) ON DELETE CASCADE;


--
-- Name: monster_spells monster_spells_spell_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monster_spells
    ADD CONSTRAINT monster_spells_spell_id_fkey FOREIGN KEY (spell_id) REFERENCES public.spells(id) ON DELETE CASCADE;


--
-- Name: monsters_special_abilities monsters_special_abilities_damage_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities
    ADD CONSTRAINT monsters_special_abilities_damage_type_id_fkey FOREIGN KEY (damage_type_id) REFERENCES public.damage_types(id) ON DELETE SET NULL;


--
-- Name: monsters_special_abilities monsters_special_abilities_dc_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities
    ADD CONSTRAINT monsters_special_abilities_dc_type_id_fkey FOREIGN KEY (dc_type_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: monsters_special_abilities monsters_special_abilities_monster_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities
    ADD CONSTRAINT monsters_special_abilities_monster_id_fkey FOREIGN KEY (monster_id) REFERENCES public.monsters(id) ON DELETE CASCADE;


--
-- Name: monsters_special_abilities monsters_special_abilities_spellcasting_ability_score_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.monsters_special_abilities
    ADD CONSTRAINT monsters_special_abilities_spellcasting_ability_score_id_fkey FOREIGN KEY (spellcasting_ability_score_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: rules_subsections rules_subsections_rule_sections_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rules_subsections
    ADD CONSTRAINT rules_subsections_rule_sections_id_fkey FOREIGN KEY (rule_sections_id) REFERENCES public.rule_sections(id);


--
-- Name: spells_classes spells_classes_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes
    ADD CONSTRAINT spells_classes_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: spells_classes spells_classes_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_classes
    ADD CONSTRAINT spells_classes_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(classes_id) ON DELETE CASCADE;


--
-- Name: spells spells_damage_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT spells_damage_type_id_fkey FOREIGN KEY (damage_type_id) REFERENCES public.damage_types(id) ON DELETE SET NULL;


--
-- Name: spells spells_dc_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT spells_dc_id_fkey FOREIGN KEY (dc_id) REFERENCES public.ability_scores(id) ON DELETE SET NULL;


--
-- Name: spells spells_school_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells
    ADD CONSTRAINT spells_school_id_fkey FOREIGN KEY (school_id) REFERENCES public.magic_schools(id) ON DELETE SET NULL;


--
-- Name: spells_subclasses spells_subclasses_required_feature_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_required_feature_id_fkey FOREIGN KEY (required_feature_id) REFERENCES public.features(id) ON DELETE SET NULL;


--
-- Name: spells_subclasses spells_subclasses_required_level_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_required_level_id_fkey FOREIGN KEY (required_level_id) REFERENCES public.levels(id) ON DELETE SET NULL;


--
-- Name: spells_subclasses spells_subclasses_spells_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_spells_id_fkey FOREIGN KEY (spells_id) REFERENCES public.spells(classes_id) ON DELETE CASCADE;


--
-- Name: spells_subclasses spells_subclasses_subclasses_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.spells_subclasses
    ADD CONSTRAINT spells_subclasses_subclasses_id_fkey FOREIGN KEY (subclasses_id) REFERENCES public.subclasses(id);


--
-- Name: subclasses_class subclasses_class_classes_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class
    ADD CONSTRAINT subclasses_class_classes_id_fkey FOREIGN KEY (classes_id) REFERENCES public.classes(id);


--
-- Name: subclasses subclasses_class_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses
    ADD CONSTRAINT subclasses_class_id_fkey FOREIGN KEY (class_id) REFERENCES public.classes(id) ON DELETE SET NULL;


--
-- Name: subclasses_class subclasses_class_subclasses_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subclasses_class
    ADD CONSTRAINT subclasses_class_subclasses_id_fkey FOREIGN KEY (subclasses_id) REFERENCES public.subclasses(id);


--
-- Name: trait_options trait_options_option_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options
    ADD CONSTRAINT trait_options_option_id_fkey FOREIGN KEY (option_id) REFERENCES public.traits(trait_proficiency_id) ON DELETE SET NULL;


--
-- Name: trait_options trait_options_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options
    ADD CONSTRAINT trait_options_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE SET NULL;


--
-- Name: trait_options trait_options_spell_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options
    ADD CONSTRAINT trait_options_spell_id_fkey FOREIGN KEY (spell_id) REFERENCES public.spells(id) ON DELETE SET NULL;


--
-- Name: trait_options trait_options_subtrait_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trait_options
    ADD CONSTRAINT trait_options_subtrait_id_fkey FOREIGN KEY (subtrait_id) REFERENCES public.traits(id) ON DELETE SET NULL;


--
-- Name: traits_proficiencies traits_proficiencies_proficiency_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_proficiencies
    ADD CONSTRAINT traits_proficiencies_proficiency_id_fkey FOREIGN KEY (proficiency_id) REFERENCES public.proficiencies(id) ON DELETE CASCADE;


--
-- Name: traits_proficiencies traits_proficiencies_trait_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.traits_proficiencies
    ADD CONSTRAINT traits_proficiencies_trait_id_fkey FOREIGN KEY (trait_id) REFERENCES public.traits(id) ON DELETE CASCADE;


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
-- PostgreSQL database dump complete
--

