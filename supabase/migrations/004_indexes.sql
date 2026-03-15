-- Helpful indexes for common queries
create index if not exists resumes_user_id_idx on resumes (user_id);
create index if not exists resumes_created_at_idx on resumes (created_at desc);
create index if not exists analysis_resume_id_idx on analysis (resume_id);
create index if not exists analysis_created_at_idx on analysis (created_at desc);
