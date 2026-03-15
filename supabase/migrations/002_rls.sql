-- Enable RLS
alter table resumes enable row level security;
alter table analysis enable row level security;

-- Resumes: only owner can read/write
create policy "resumes_select_own"
on resumes for select
using (auth.uid() = user_id);

create policy "resumes_insert_own"
on resumes for insert
with check (auth.uid() = user_id);

create policy "resumes_update_own"
on resumes for update
using (auth.uid() = user_id);

create policy "resumes_delete_own"
on resumes for delete
using (auth.uid() = user_id);

-- Analysis: only access rows tied to user's resumes
create policy "analysis_select_own"
on analysis for select
using (
  exists (
    select 1 from resumes
    where resumes.id = analysis.resume_id
      and resumes.user_id = auth.uid()
  )
);

create policy "analysis_insert_own"
on analysis for insert
with check (
  exists (
    select 1 from resumes
    where resumes.id = analysis.resume_id
      and resumes.user_id = auth.uid()
  )
);

create policy "analysis_update_own"
on analysis for update
using (
  exists (
    select 1 from resumes
    where resumes.id = analysis.resume_id
      and resumes.user_id = auth.uid()
  )
);

create policy "analysis_delete_own"
on analysis for delete
using (
  exists (
    select 1 from resumes
    where resumes.id = analysis.resume_id
      and resumes.user_id = auth.uid()
  )
);
