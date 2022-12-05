CREATE TABLE IF NOT EXISTS feedback (
    id uuid NOT NULL DEFAULT gen_random_uuid(),
    created_at timestamptz NOT NULL DEFAULT now(),
    first_name varchar NOT NULL,
    last_name varchar NOT NULL,
    patronym varchar,
    phone varchar NOT NULL,
    feedback_text text NOT NULL
);
