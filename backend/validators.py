# | Function              | Purpose                                        |
# | --------------------- | ---------------------------------------------- |
# | `require_fields`      | Check JSON has all required keys               |
# | `is_valid_int`        | Ensure IDs are integers                        |
# | `is_non_empty_string` | Names/majors/emails must not be blank          |
# | `is_valid_email`      | Simple email check                             |
# | `is_valid_major`      | Validate major from an allowed list            |
# | `student_exists`      | Prevent inserting sessions for missing student |
# | `tutor_exists`        | Prevent orphan session records                 |
