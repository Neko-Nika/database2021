/*-------------------------------------GAMES---------------------------------------------*/
CREATE OR REPLACE FUNCTION add_game(in name text, in genre text, in version float)
    returns void
    language sql
    as $$

    insert into "Games" values (name, genre, version)

$$;

CREATE OR REPLACE FUNCTION delete_game(in name1 text)
    returns void
    language sql
    as $$

    delete from "Games" where name = name1

$$;

CREATE OR REPLACE FUNCTION get_games()
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Games".name,
                'genre', "Games".genre,
				'version', "Games".version
				)) from "Games");
		end
$$;

CREATE OR REPLACE FUNCTION delete_games()
    returns void
    language sql
    as $$

    truncate "Games"

$$;

CREATE OR REPLACE FUNCTION find_games_by_genre(in genre1 text)
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Games".name,
                'genre', "Games".genre,
				'version', "Games".version
				)) from "Games" where genre = genre1);
		end
$$;

CREATE OR REPLACE FUNCTION delete_games_by_genre(in genre1 text)
    returns void
    language sql
    as $$

    delete from "Games" where genre = genre1

$$;

CREATE OR REPLACE FUNCTION update_game_version(in new float, in name1 text)
    returns void
    language sql
    as $$

    update "Games" set version = new where name = name1

$$;
/*----------------------------------------------------------------------------*/


/*-------------------------------------PUBLISHERS---------------------------------------------*/
CREATE OR REPLACE FUNCTION add_publisher(in name text, in country text, in f_date date)
    returns void
    language sql
    as $$

    insert into "Publishers" values (name, country, f_date)

$$;

CREATE OR REPLACE FUNCTION delete_publisher(in name1 text)
    returns void
    language sql
    as $$

    delete from "Publishers" where name = name1

$$;

CREATE OR REPLACE FUNCTION get_publishers()
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Publishers".name,
                'country', "Publishers".country,
				'foundation_date', "Publishers".foundation_date
				)) from "Publishers");
		end
$$;

CREATE OR REPLACE FUNCTION delete_publishers()
    returns void
    language sql
    as $$

    truncate "Publishers"

$$;

CREATE OR REPLACE FUNCTION find_publishers_by_country(in country1 text)
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Publishers".name,
                'country', "Publishers".country,
				'foundation_date', "Publishers".foundation_date
				)) from "Publishers" where country = country1);
		end
$$;

CREATE OR REPLACE FUNCTION delete_publishers_by_country(in country1 text)
    returns void
    language sql
    as $$

    delete from "Publishers" where country = country1

$$;

CREATE OR REPLACE FUNCTION update_publisher_name(in new text, in name1 text)
    returns void
    language sql
    as $$

    update "Publishers" set name = new where name = name1

$$;
/*----------------------------------------------------------------------------*/


/*-------------------------------------CREATORS---------------------------------------------*/
CREATE OR REPLACE FUNCTION add_creator(in name text, in country text, in email text)
    returns void
    language sql
    as $$

    insert into "Creators" values (name, country, email)

$$;

CREATE OR REPLACE FUNCTION delete_creator(in name1 text)
    returns void
    language sql
    as $$

    delete from "Creators" where name = name1

$$;

CREATE OR REPLACE FUNCTION get_creators()
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Creators".name,
                'country', "Creators".country,
				'email', "Creators".email
				)) from "Creators");
		end
$$;

CREATE OR REPLACE FUNCTION delete_creators()
    returns void
    language sql
    as $$

    truncate "Creators"

$$;

CREATE OR REPLACE FUNCTION find_creators_by_country(in country1 text)
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
				'name', "Creators".name,
                'country', "Creators".country,
				'email', "Creators".email
				)) from "Creators" where country = country1);
		end
$$;

CREATE OR REPLACE FUNCTION delete_creators_by_country(in country1 text)
    returns void
    language sql
    as $$

    delete from "Creators" where country = country1

$$;

CREATE OR REPLACE FUNCTION update_creator_name(in new text, in name1 text)
    returns void
    language sql
    as $$

    update "Creators" set name = new where name = name1

$$;
/*----------------------------------------------------------------------------*/


/*-------------------------------------PUBLICATIONS---------------------------------------------*/
CREATE OR REPLACE FUNCTION add_publication(in game_name text, in publisher_name text, in creator_name text, date date, platform text)
    returns void
    language sql
    as $$

    insert into "Publications" (game_name, publisher_name, creator_name, date, platform)
    values (game_name, publisher_name, creator_name, date, platform)

$$;

CREATE OR REPLACE FUNCTION delete_publication(in id1 integer)
    returns void
    language sql
    as $$

    delete from "Publications" where id = id1

$$;

CREATE OR REPLACE FUNCTION get_publications()
    returns json
    language plpgsql 
    as $$
		begin 
			return (select json_agg(json_build_object(
                'id', "Publications".id,
				'game_name', "Publications".game_name,
                'publisher_name', "Publications".publisher_name,
				'creator_name', "Publications".creator_name,
                'date', "Publications".date,
                'platform', "Publications".platform
				)) from "Publications");
		end
$$;

CREATE OR REPLACE FUNCTION delete_publications()
    returns void
    language sql
    as $$

    truncate "Publications"

$$;

CREATE OR REPLACE FUNCTION update_publication_platform(in new text, in id1 integer)
    returns void
    language sql
    as $$

    update "Publications" set platform = new where id = id1

$$;
/*----------------------------------------------------------------------------*/
