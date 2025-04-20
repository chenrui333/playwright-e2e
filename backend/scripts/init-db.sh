#!/bin/sh

set -e

sqlite3 /data/coursework.db ".read /sql/teacher.sql"
sqlite3 /data/coursework.db ".read /sql/course.sql"
sqlite3 /data/coursework.db ".read /sql/student.sql"
