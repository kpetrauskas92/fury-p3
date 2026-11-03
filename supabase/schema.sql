-- FURY shared leaderboard.
-- Run this once in the Supabase SQL editor (Dashboard -> SQL Editor -> New query).
--
-- Anyone can read the leaderboard. Nobody can write to the table directly:
-- players are created and scored only through the functions below,
-- which validate the input.

create table if not exists public.players (
  name text not null check (name ~ '^[A-Z][a-z]{2,9}$'),
  city text not null check (city ~ '^[A-Z][a-z]{2,9}$'),
  score integer not null default 0 check (score >= 0),
  created_at timestamptz not null default now(),
  primary key (name, city)
);

alter table public.players enable row level security;

drop policy if exists "Leaderboard is public" on public.players;
create policy "Leaderboard is public"
  on public.players for select
  using (true);

grant select on public.players to anon, authenticated;


-- Looks up a player and their leaderboard rank.
create or replace function public.find_player(p_name text, p_city text)
returns table (name text, city text, score integer, rank bigint)
language sql
stable
set search_path = public
as $$
  select p.name, p.city, p.score,
         (select count(*) + 1 from players q where q.score > p.score)
  from players p
  where p.name = initcap(p_name) and p.city = initcap(p_city);
$$;


-- Registers a new player with 100 bonus points.
-- Returns false if the player already exists.
create or replace function public.register_player(p_name text, p_city text)
returns boolean
language plpgsql
security definer
set search_path = public
as $$
begin
  insert into players (name, city, score)
  values (initcap(p_name), initcap(p_city), 100)
  on conflict do nothing;
  return found;
end;
$$;


-- Adds one game's points to a player's total and returns the new total.
-- 130 is the most a single game can give (10 hits * 10 points * 1.3).
create or replace function public.add_score(p_name text, p_city text, p_points integer)
returns integer
language plpgsql
security definer
set search_path = public
as $$
declare
  new_score integer;
begin
  if p_points is null or p_points < 0 or p_points > 130 then
    raise exception 'invalid score: %', p_points;
  end if;

  update players
  set score = score + p_points
  where name = initcap(p_name) and city = initcap(p_city)
  returning score into new_score;

  if new_score is null then
    raise exception 'player not found';
  end if;
  return new_score;
end;
$$;

revoke all on function public.register_player(text, text) from public;
revoke all on function public.add_score(text, text, integer) from public;
grant execute on function public.find_player(text, text) to anon, authenticated;
grant execute on function public.register_player(text, text) to anon, authenticated;
grant execute on function public.add_score(text, text, integer) to anon, authenticated;
