# Supabase Setup Checklist

## 1) Create Project
- Create a new project in Supabase.
- Save the project URL and API keys.

## 2) Enable Auth
- Enable Email/Password auth (default).
- Optional: disable "Confirm email" for faster local testing.

## 3) Create Storage Bucket
- Create a bucket named `resumes`.
- Set bucket to private if you plan to use signed URLs.

## 4) Run Migrations (in order)
- Open SQL Editor in Supabase.
- Run:
  1. `supabase/migrations/001_init.sql`
  2. `supabase/migrations/002_rls.sql`
  3. `supabase/migrations/003_storage_policies.sql`
  4. `supabase/migrations/004_indexes.sql`
  5. `supabase/migrations/005_add_storage_path.sql`
  6. `supabase/migrations/006_add_resume_text.sql`
  7. `supabase/migrations/007_add_analysis_scores.sql`

## 5) RLS + Storage Policies
- RLS is enabled via `002_rls.sql`.
- Storage policies are added via `003_storage_policies.sql` for the `resumes` bucket.

## 6) Set Env Vars
Frontend (`frontend/.env.local`):
- `NEXT_PUBLIC_SUPABASE_URL=...`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY=...`

Backend (`backend/.env`):
- `SUPABASE_URL=...`
- `SUPABASE_SERVICE_ROLE_KEY=...`

## 7) Smoke Test
- Insert a row into `resumes` via the dashboard.
- Upload a file to the `resumes` bucket.
