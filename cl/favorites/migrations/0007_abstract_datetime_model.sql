-- Django sqlmigrate command created the following unnecessary and
-- weird commands.  The migration involves no actual sql and only alters
-- the help text on the model.  This is being left for posterity.

-- BEGIN;
-- --
-- -- Alter field date_created on usertag
-- --
-- ALTER TABLE "favorites_usertag" ALTER COLUMN "date_created" SET DEFAULT '2020-12-23T15:01:58.015561+00:00'::timestamptz;
-- ALTER TABLE "favorites_usertag" ALTER COLUMN "date_created" DROP DEFAULT;
-- --
-- -- Alter field date_modified on usertag
-- --
-- ALTER TABLE "favorites_usertag" ALTER COLUMN "date_modified" SET DEFAULT '2020-12-23T15:01:58.061692+00:00'::timestamptz;
-- ALTER TABLE "favorites_usertag" ALTER COLUMN "date_modified" DROP DEFAULT;
-- COMMIT;