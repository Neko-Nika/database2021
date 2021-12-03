CREATE OR REPLACE FUNCTION init_tables()
    returns void
    language sql
    as $$

    create table if not exists "Games" (
        name text not null primary key,
        genre text not null,
        version float not null
    );

    create table if not exists "Creators" (
        name text not null primary key,
        country text not null,
        email text not null
    );

    create table if not exists "Publishers" (
        name text not null primary key,
        country text not null,
        foundation_date date not null
    );

    create table if not exists "Publications" (
        id serial not null primary key,
        game_name text not null,
        publisher_name text not null,
        creator_name text not null,
        date date not null,
        platform text not null
    );

    create index if not exists genre on "Games" (genre);
    create index if not exists country1 on "Creators" (country);
    create index if not exists country2 on "Publishers" (country);

    create or replace function update_publisher()
            returns trigger as $u1$
            begin 
                if old.name != new.name then
                    update "Publications" set publisher_name = new.name
                    where publisher_name = old.name;
                end if;
                return new;
            end;
        $u1$ language plpgsql;

    drop trigger if exists trigger_publisher on "Publishers";
    create trigger trigger_publisher after update on "Publishers"
        for row execute procedure update_publisher();


    create or replace function update_creator()
            returns trigger as $u2$
            begin 
                if old.name != new.name then
                    update "Publications" set creator_name = new.name
                    where creator_name = old.name;
                end if;
                return new;
            end;
        $u2$ language plpgsql;

    drop trigger if exists trigger_creator on "Creators";
    create trigger trigger_creator after update on "Creators"
        for row execute procedure update_creator();

$$;