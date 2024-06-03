CREATE TABLE katalog (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  parent_id INTEGER NOT NULL
);

CREATE TABLE documents
(
    id SERIAL PRIMARY KEY,
    name text NOT NULL,
    format text NOT NULL,
    size integer NOT NULL,
    hash text NOT NULL,
    parent_katalog_id integer NOT NULL
)