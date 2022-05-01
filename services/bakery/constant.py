class Constant:
    class ProjectRoles:
        GIVER = 'knowledge_giver'
        TAKER = 'knowledge_taker'
        LINE_MANAGER = 'line_manager'
        KNOWLEDGE_FACILITATOR = "knowledge_facilitator"
        MODERATOR = 'moderator'
        EXPERT_EDITOR = "expert_editor"  # TODO: not created in backend at the moment

    class Category:
        NAME = "Name"
        DESCRIPTION = "Description"
        ID = "Id"
        SHEET_CATEGORIES = "Categories"
        SHEET_QUESTIONS = "Questions"
        DEFAULT = "Default"

    class Question:
        TEXT = "Text"
        DESCRIPTION = "Description"
        ID = "Id"
        CATEGORY_ID = "Category_id"
        TAGS = "Tags"

    class Organization:
        ORGANIZATION_ID = "organization_id"
        ORGANIZATION_NAME = "organization_name"
        DEPARTMENTS = "departments"
        JOB_NAMES = "job_names"
        BUSINESS_UNITS = "business_units"
        KNOWLEDGE_DOMAINS = "knowledge_domains"
        CREATED_BY = "created_by"
        BLOB_PATH = "path"
        SHEET_QUESTIONS = "questions"
        SHEET_CATEGORIES = "categories"
        IS_MASTER_ORGANIZATION = "is_master_organization"
        MASTER_ORGANIZATION_ID = "master_organization_id"

    class EventActions:
        EMAIL_NOTIFICATION = "email_notification"
        PROJECT_PUBLISHED = "project_published"
        DELETED_PROJECT = "deleted_project"
        RESTORE_PROJECT = "restore_project"
        REMOVE_PROJECT = "remove_project"
        INDEX_PROJECT = "index_project"
        PROJECT_TIMELINE_EXPIRATION = "project_timeline_expiration"

    class ConfigKey:
        DB_USER_NAME = "db_user_name"
        DB_HOST = "db_host"
        DB_PASSWORD = "db_password"
        DB_NAME = "db_name"
        DB_URL = "db_url"
        KA_TOPIC = "topic"
        ADMIN_STORAGE_NAME = "admin_storage_account_name"
        ADMIN_STORAGE_KEY = "admin_storage_account_key"
        STORAGE_ACCOUNT_NAME = "storage_account_name"
        STORAGE_ACCOUNT_KEY = "storage_account_key"
        KA_SERVICE_BUS = "ka_service_bus"
        KA_SERVICE_BUS_NAME = "ka_service_bus_name"
        MASTER_DATA_CONTAINER = "master_data_container"
        PROJECT_DELETION_EXPIRY = "project_deletion_expiry"
        CLEAN_PROJECT_RETRY_HOURS = "clean_project_retry_hours"
        KA_SEARCH_INDEX_BUS = "ka_search_index_bus"
        KA_SEARCH_INDEX_QNAME = "ka_search_index_qname"
        PLATFORM_NOTIFICATION_LIMIT = "platform_notification_limit"
        ADMIN_NAME = "admin_name"
        DEFAULT_USER_NAME = "default_user_name"
        NOTIFICATION_TIMELINE_DAYS = "notification_timeline_days"
        LOG_INSTRUMENTATION_KEY = "log_instrumentation_key"
        TRACE_ID = "trace_id"
        CORS_ORIGINS = "cors_origins"
        CDN_NAME = "cdn_name"
        HELP_PROJECT_NAME = "help_project_name"

    class FilterKey:
        PARTICIPANT_EMAIL = "participant_email"
        OVERDUE = "overdue"
        OWNERSHIP = "ownership"
        REPOSITORY = "repository"

    class RecentKEY:
        PROJECT = "project"
        CATEGORY = "location"

    class ProjectContentAction:
        CONTENT_UPDATED = "content_updated"
