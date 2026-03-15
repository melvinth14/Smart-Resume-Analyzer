create table resumes (
  id uuid primary key default gen_random_uuid(),
  user_id uuid references auth.users,
  resume_url text,
  job_description text,
  ats_score integer,
  created_at timestamp default now()
);

create table analysis (
  id uuid primary key default gen_random_uuid(),
  resume_id uuid references resumes(id),
  matched_skills text[],
  missing_skills text[],
  suggestions text,
  created_at timestamp default now()
);
