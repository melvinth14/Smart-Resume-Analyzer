-- Storage policies for resumes bucket
-- Ensure the bucket exists before running this migration.

alter table storage.objects enable row level security;

create policy "resumes_bucket_select_own"
on storage.objects for select
using (
  bucket_id = 'resumes'
  and auth.uid() = owner
);

create policy "resumes_bucket_insert_own"
on storage.objects for insert
with check (
  bucket_id = 'resumes'
  and auth.uid() = owner
);

create policy "resumes_bucket_update_own"
on storage.objects for update
using (
  bucket_id = 'resumes'
  and auth.uid() = owner
);

create policy "resumes_bucket_delete_own"
on storage.objects for delete
using (
  bucket_id = 'resumes'
  and auth.uid() = owner
);
